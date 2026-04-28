-- IT
INSERT INTO designations (name, department_id) VALUES
    ('Software Developer',        (SELECT id FROM departments WHERE name = 'IT')),
    ('Senior Software Developer', (SELECT id FROM departments WHERE name = 'IT')),
    ('DevOps Engineer',           (SELECT id FROM departments WHERE name = 'IT')),
    ('QA Engineer',               (SELECT id FROM departments WHERE name = 'IT')),
    ('IT Manager',                (SELECT id FROM departments WHERE name = 'IT')),
    ('Systems Administrator',     (SELECT id FROM departments WHERE name = 'IT')),
    ('Database Administrator',    (SELECT id FROM departments WHERE name = 'IT')),
    ('Technical Lead',            (SELECT id FROM departments WHERE name = 'IT'));

-- Human Resources
INSERT INTO designations (name, department_id) VALUES
    ('HR Executive',              (SELECT id FROM departments WHERE name = 'Human Resources')),
    ('HR Manager',                (SELECT id FROM departments WHERE name = 'Human Resources')),
    ('Recruiter',                 (SELECT id FROM departments WHERE name = 'Human Resources')),
    ('Talent Acquisition Lead',   (SELECT id FROM departments WHERE name = 'Human Resources')),
    ('HR Business Partner',       (SELECT id FROM departments WHERE name = 'Human Resources')),
    ('Payroll Specialist',        (SELECT id FROM departments WHERE name = 'Human Resources'));

-- Finance
INSERT INTO designations (name, department_id) VALUES
    ('Accountant',                (SELECT id FROM departments WHERE name = 'Finance')),
    ('Senior Accountant',         (SELECT id FROM departments WHERE name = 'Finance')),
    ('Financial Analyst',         (SELECT id FROM departments WHERE name = 'Finance')),
    ('Finance Manager',           (SELECT id FROM departments WHERE name = 'Finance')),
    ('Auditor',                   (SELECT id FROM departments WHERE name = 'Finance')),
    ('Tax Consultant',            (SELECT id FROM departments WHERE name = 'Finance'));

-- Marketing
INSERT INTO designations (name, department_id) VALUES
    ('Marketing Executive',       (SELECT id FROM departments WHERE name = 'Marketing')),
    ('Marketing Manager',         (SELECT id FROM departments WHERE name = 'Marketing')),
    ('Content Writer',            (SELECT id FROM departments WHERE name = 'Marketing')),
    ('SEO Specialist',            (SELECT id FROM departments WHERE name = 'Marketing')),
    ('Brand Strategist',          (SELECT id FROM departments WHERE name = 'Marketing')),
    ('Social Media Manager',      (SELECT id FROM departments WHERE name = 'Marketing'));

-- Sales
INSERT INTO designations (name, department_id) VALUES
    ('Sales Executive',           (SELECT id FROM departments WHERE name = 'Sales')),
    ('Sales Manager',             (SELECT id FROM departments WHERE name = 'Sales')),
    ('Business Development Executive', (SELECT id FROM departments WHERE name = 'Sales')),
    ('Account Manager',           (SELECT id FROM departments WHERE name = 'Sales')),
    ('Pre-Sales Consultant',      (SELECT id FROM departments WHERE name = 'Sales'));

-- Operations
INSERT INTO designations (name, department_id) VALUES
    ('Operations Executive',      (SELECT id FROM departments WHERE name = 'Operations')),
    ('Operations Manager',        (SELECT id FROM departments WHERE name = 'Operations')),
    ('Process Analyst',           (SELECT id FROM departments WHERE name = 'Operations')),
    ('Supply Chain Coordinator',  (SELECT id FROM departments WHERE name = 'Operations')),
    ('Logistics Manager',         (SELECT id FROM departments WHERE name = 'Operations'));

-- Customer Support
INSERT INTO designations (name, department_id) VALUES
    ('Support Executive',         (SELECT id FROM departments WHERE name = 'Customer Support')),
    ('Senior Support Executive',  (SELECT id FROM departments WHERE name = 'Customer Support')),
    ('Support Team Lead',         (SELECT id FROM departments WHERE name = 'Customer Support')),
    ('Customer Success Manager',  (SELECT id FROM departments WHERE name = 'Customer Support')),
    ('Technical Support Engineer',(SELECT id FROM departments WHERE name = 'Customer Support'));

-- Research and Development
INSERT INTO designations (name, department_id) VALUES
    ('Research Analyst',          (SELECT id FROM departments WHERE name = 'Research and Development')),
    ('R&D Engineer',              (SELECT id FROM departments WHERE name = 'Research and Development')),
    ('Senior R&D Engineer',       (SELECT id FROM departments WHERE name = 'Research and Development')),
    ('R&D Manager',               (SELECT id FROM departments WHERE name = 'Research and Development')),
    ('Data Scientist',            (SELECT id FROM departments WHERE name = 'Research and Development')),
    ('Machine Learning Engineer', (SELECT id FROM departments WHERE name = 'Research and Development'));

-- Legal
INSERT INTO designations (name, department_id) VALUES
    ('Legal Executive',           (SELECT id FROM departments WHERE name = 'Legal')),
    ('Legal Counsel',             (SELECT id FROM departments WHERE name = 'Legal')),
    ('Compliance Officer',        (SELECT id FROM departments WHERE name = 'Legal')),
    ('Contract Manager',          (SELECT id FROM departments WHERE name = 'Legal')),
    ('Legal Manager',             (SELECT id FROM departments WHERE name = 'Legal'));

-- Administration
INSERT INTO designations (name, department_id) VALUES
    ('Admin Executive',           (SELECT id FROM departments WHERE name = 'Administration')),
    ('Admin Manager',             (SELECT id FROM departments WHERE name = 'Administration')),
    ('Office Coordinator',        (SELECT id FROM departments WHERE name = 'Administration')),
    ('Executive Assistant',       (SELECT id FROM departments WHERE name = 'Administration')),
    ('Facilities Manager',        (SELECT id FROM departments WHERE name = 'Administration'));