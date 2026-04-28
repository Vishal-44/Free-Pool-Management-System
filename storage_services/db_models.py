from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Index,
    Enum
)
from sqlalchemy.orm import relationship, validates

from storage_services.types import (
    CertificationLevel,
    ProjectStatus,
    EmployeeStatus,
    EmployeeSkillLevel
)

Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        Index('idx_admin_username', 'username'),
        Index('idx_admin_email', 'email'),
    )


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    # One department has many designations
    designations = relationship(
        'Designation',
        back_populates='department'
    )

    __table_args__ = (
        Index('idx_department_name', 'name'),
    )


class Designation(Base):
    __tablename__ = 'designations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    # Many designations belong to one department
    department = relationship('Department', back_populates='designations')

    # One designation can appear in many designation records (employees holding it)
    designation_records = relationship(
        'DesignationRecord',
        back_populates='designation'
    )

    __table_args__ = (
        Index('idx_designation_name', 'name'),
        Index('idx_designation_department_id', 'department_id'),
    )


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    status = Column(Enum(EmployeeStatus), default=EmployeeStatus.WORKING, nullable=False)
    description = Column(String(255), nullable=True)

    # ── Relationships ─────────────────────────────────────────────────────────

    # Full designation history, ordered chronologically
    designation_records = relationship(
        'DesignationRecord',
        back_populates='employee',
        order_by='DesignationRecord.start_date',
        cascade='all, delete-orphan'
    )

    skill_maps = relationship(
        'EmployeeSkillMap',
        back_populates='employee',
        cascade='all, delete-orphan'
    )

    certification_maps = relationship(
        'EmployeeCertificationMap',
        back_populates='employee',
        cascade='all, delete-orphan'
    )

    project_maps = relationship(
        'ProjectEmployeeMap',
        back_populates='employee',
        cascade='all, delete-orphan'
    )

    __table_args__ = (
        Index('idx_employee_email', 'email'),
        Index('idx_employee_status', 'status'),
    )

    # ── Convenience properties ────────────────────────────────────────────────

    @property
    def current_designation_record(self):
        """Return the active DesignationRecord (end_date is None)."""
        return next(
            (r for r in self.designation_records if r.end_date is None),
            None
        )

    @property
    def current_designation(self):
        """Return the active Designation object, or None."""
        record = self.current_designation_record
        return record.designation if record else None

    @property
    def current_department(self):
        """Return the active Department, resolved via Designation, or None."""
        designation = self.current_designation
        return designation.department if designation else None


class DesignationRecord(Base):
    """
    Tracks an employee's designation history.

    Each row represents one period during which an employee held a designation.
    The active record has end_date = None.  On promotion / department transfer,
    close the current record (set end_date) and insert a new open record.

    Typical workflows
    -----------------
    Onboard employee:
        record = DesignationRecord(
            employee=emp, designation=designation, start_date=date.today()
        )
        session.add(record)

    Promote employee:
        current = emp.current_designation_record
        current.end_date = date.today()
        session.add(DesignationRecord(
            employee=emp, designation=new_designation, start_date=date.today()
        ))

    Get full history:
        emp.designation_records          # ordered by start_date (asc)

    Get current role:
        emp.current_designation          # Designation object
        emp.current_department           # Department object
    """
    __tablename__ = 'designation_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    designation_id = Column(Integer, ForeignKey('designations.id'), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)   # None = currently active

    # Many records belong to one employee / one designation
    employee = relationship('Employee', back_populates='designation_records')
    designation = relationship('Designation', back_populates='designation_records')

    __table_args__ = (
        Index('idx_desig_record_employee_id', 'employee_id'),
        Index('idx_desig_record_designation_id', 'designation_id'),
    )


class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    domain = Column(String(255), nullable=False)

    __table_args__ = (
        Index('idx_skill_name', 'name'),
        Index('idx_skill_domain', 'domain'),
    )


class Certification(Base):
    __tablename__ = 'certifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    certification_level = Column(Enum(CertificationLevel), nullable=False)

    __table_args__ = (
        Index('idx_certification_name', 'name'),
        Index('idx_certification_level', 'certification_level'),
    )


class CertificationSkillMap(Base):
    __tablename__ = 'certification_skill_maps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    certification_id = Column(Integer, ForeignKey('certifications.id'), nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)

    __table_args__ = (
        Index('idx_cert_skill_map_certification_id', 'certification_id'),
        Index('idx_cert_skill_map_skill_id', 'skill_id'),
    )


class EmployeeSkillMap(Base):
    __tablename__ = 'employee_skill_maps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)
    skill_level = Column(Enum(EmployeeSkillLevel), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    employee = relationship('Employee', back_populates='skill_maps')
    skill = relationship('Skill')

    __table_args__ = (
        Index('idx_emp_skill_map_employee_id', 'employee_id'),
        Index('idx_emp_skill_map_skill_id', 'skill_id'),
        Index('idx_emp_skill_map_skill_level', 'skill_level'),
    )


class EmployeeCertificationMap(Base):
    __tablename__ = 'employee_certification_maps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    certification_id = Column(Integer, ForeignKey('certifications.id'), nullable=False)
    certificate_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    employee = relationship('Employee', back_populates='certification_maps')
    certification = relationship('Certification')

    __table_args__ = (
        Index('idx_emp_cert_map_employee_id', 'employee_id'),
        Index('idx_emp_cert_map_certification_id', 'certification_id'),
    )


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.READY, nullable=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    employee_maps = relationship(
        'ProjectEmployeeMap',
        back_populates='project',
        cascade='all, delete-orphan'
    )

    __table_args__ = (
        Index('idx_project_name', 'name'),
        Index('idx_project_status', 'status'),
    )


class ProjectEmployeeMap(Base):
    __tablename__ = 'project_employee_maps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    feedback = Column(String(255), nullable=True)

    employee = relationship('Employee', back_populates='project_maps')
    project = relationship('Project', back_populates='employee_maps')

    __table_args__ = (
        Index('idx_proj_emp_map_project_id', 'project_id'),
        Index('idx_proj_emp_map_employee_id', 'employee_id'),
    )