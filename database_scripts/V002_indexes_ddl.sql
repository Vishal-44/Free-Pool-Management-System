CREATE INDEX IF NOT EXISTS idx_email ON employees(email);
CREATE INDEX IF NOT EXISTS idx_status ON employees(status);


CREATE INDEX IF NOT EXISTS idx_name ON departments(name);

CREATE INDEX IF NOT EXISTS idx_name ON designations(name);
CREATE INDEX IF NOT EXISTS idx_department_id ON designations(department_id);

CREATE INDEX IF NOT EXISTS idx_name ON skills(name);
CREATE INDEX IF NOT EXISTS idx_domain ON skills(domain);

CREATE INDEX IF NOT EXISTS idx_name ON certifications(name);
CREATE INDEX IF NOT EXISTS idx_certification_level ON certifications(certification_level);

CREATE INDEX IF NOT EXISTS idx_certification_id ON certification_skill_maps(certification_id);
CREATE INDEX IF NOT EXISTS idx_skill_id ON certification_skill_maps(skill_id);

CREATE INDEX IF NOT EXISTS idx_employee_id ON employee_skill_maps(employee_id);
CREATE INDEX IF NOT EXISTS idx_skill_id ON employee_skill_maps(skill_id);
CREATE INDEX IF NOT EXISTS idx_skill_level ON employee_skill_maps(skill_level);

CREATE INDEX IF NOT EXISTS idx_employee_id ON employee_certification_maps(employee_id);
CREATE INDEX IF NOT EXISTS idx_certification_id ON employee_certification_maps(certification_id);

CREATE INDEX IF NOT EXISTS idx_name ON projects(name);
CREATE INDEX IF NOT EXISTS idx_status ON projects(status);

CREATE INDEX IF NOT EXISTS idx_employee_id ON designation_records(employee_id);
CREATE INDEX IF NOT EXISTS idx_designation_id ON designation_records(designation_id);

CREATE INDEX IF NOT EXISTS idx_project_id ON project_employee_maps(project_id);
CREATE INDEX IF NOT EXISTS idx_employee_id ON project_employee_maps(employee_id);