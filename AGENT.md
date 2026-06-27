# Agent Guide

## Project Overview

This is a FastAPI backend for the Free Pool Management App. It manages admins,
employees, designations, departments, skills, certifications, project
assignments, authentication, and employee profile updates.

The codebase is intentionally layered:

- `routers/`: FastAPI route definitions and request-level validation.
- `services/`: business rules and orchestration.
- `repositories/`: SQLAlchemy queries and persistence.
- `storage_services/`: database engine/session setup, ORM models, file uploads,
  and enum types.
- `serializers/`: Pydantic request/response models.
- `middlewares/`: JWT authentication and role authorization decorators.
- `constants/`: messages, env-backed settings, and other shared constants.
- `utils/`: mapping, password, JSON, auth, and employee helpers.
- `database_scripts/`: SQL DDL/index/seed scripts. Apply them in numeric order.

## Run And Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Required environment variables:

```text
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
JWT_SECRET_KEY
```

Optional environment variables:

```text
DATABASE_HOST=localhost
DATABASE_PORT=5432
AUTHENTICATION_SERVICE=jwt
JWT_ALGORITHM=HS256
JWT_EXPIRY=3600
UPLOAD_DIR=uploads
```

Run locally:

```powershell
uvicorn main:app --reload
```

Useful endpoints:

- `GET /health`
- `POST /auth/login`
- `POST /auth/employee/login`
- `GET /docs`

## Current API Surface

Implemented routers currently include:

- `auth_router`: admin login and employee login.
- `admin_router`: authenticated role-neutral skill listing, employee search,
  employee list, and single employee onboard.
- `employee_router`: employee profile update with optional image upload and
  skills JSON.

The Jira backlog contains more backend stories than are currently implemented.
When adding those features, preserve the existing router -> service ->
repository pattern.

## Architecture Conventions

Keep route handlers thin. They should parse inputs, apply route-specific
validation, call a service, and return `APIResponse` through `JSONResponse`.

Put business rules in services. Examples already present:

- `AdminService.onboard_employee` checks duplicates, validates designation,
  generates a password, and delegates persistence.
- `EmployeeService.update_profile` handles upload orchestration and skill JSON
  parsing before calling the repository.

Put database access in repositories. Repositories inherit `DatabaseService` and
use `with self.get_session() as session:` for transaction handling. The context
manager commits on success and rolls back on exceptions.

Use Pydantic serializers for request and response shapes. API responses are
wrapped in `serializers.response.APIResponse`.

Use custom exceptions from `exceptions.py` for expected failures. `main.py`
registers handlers that convert these to consistent API responses.

## Authentication And Authorization

Authentication is global middleware:

- `AuthenticationMiddleware` skips paths listed in
  `constants.middleware_constant.UNAUTHENTICATED_ENDPOINTS`.
- Protected endpoints require `Authorization: Bearer <token>`.
- Endpoints without a role decorator are still authenticated unless explicitly
  listed as unauthenticated; use this for read-only data that both admins and
  employees can access.
- JWT claims must include `email`; middleware stores claims on
  `request.state.user`.

Role checks are decorators in `middlewares/authorization.py`:

- `@requires_admin_role()`
- `@requires_employee_role()`

Decorated handlers must accept `request: Request` so the decorator can read
`request.state.user`.

## Database Notes

The database is PostgreSQL via SQLAlchemy. Connection settings come from
`constants/database_constants.py`.

ORM models live in `storage_services/db_models.py`. Important active-record
conventions:

- Current employee designation: `DesignationRecord.end_date is None`.
- Current project assignment: `ProjectEmployeeMap.end_date is None`.
- Working employee: `Employee.status == EmployeeStatus.WORKING`.

Seed and migration scripts are in `database_scripts/`:

1. `V000_enums_ddl.sql`
2. `V001__database_ddl.sql`
3. `V002_indexes_ddl.sql`
4. `V003_seed_departments.sql`
5. `V004_seed_designations.sql`
6. `V005_seed_skiils_certificates.sql`
7. `V006_seed_admin.sql`

Note the existing filename typo `skiils`; do not rename it unless the migration
workflow is being intentionally changed.

## File Uploads

`FileUploadService` writes files to `UPLOAD_DIR` and returns `/uploads/<name>`.
Allowed content types are:

- `image/jpeg`
- `image/png`
- `image/webp`

Max upload size is 5 MB. If adding certification proof upload support, update
the allowed types deliberately because Jira mentions PDF/PNG/JPEG but the
current shared upload service does not allow PDF.

## Coding Guidelines

- Prefer existing constants for response and exception messages.
- Keep enum values aligned with `storage_services/types.py`.
- Use eager loading (`selectinload`, `joinedload`) when repository responses need
  relationships after the session closes.
- Be careful returning ORM objects after session commit; attributes needed by
  callers should be loaded before leaving the repository method.
- Avoid placing SQLAlchemy query logic in services or routers.
- Keep generated passwords hashed in storage and return the plain generated
  password only in onboarding responses.
- Admin login currently compares the stored password directly; employee login
  uses bcrypt verification. Treat changes to auth behavior carefully.

## Verification

There is no test suite in the repository at the time this guide was written.
For backend changes, at minimum:

```powershell
python -m compileall .
uvicorn main:app --reload
```

Then exercise the affected endpoints through `/docs`, curl, or an API client.
Any endpoint requiring auth needs a valid JWT and the correct role.
