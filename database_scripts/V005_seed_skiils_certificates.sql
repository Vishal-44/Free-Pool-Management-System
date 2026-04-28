-- ---------------------------------------------------------------
-- SKILLS
-- ---------------------------------------------------------------
INSERT INTO skills (name, domain) VALUES
    -- Programming Languages
    ('Python',                    'Programming Languages'),
    ('Java',                      'Programming Languages'),
    ('JavaScript',                'Programming Languages'),
    ('TypeScript',                'Programming Languages'),
    ('C++',                       'Programming Languages'),
    ('Go',                        'Programming Languages'),
    ('Rust',                      'Programming Languages'),
    ('Kotlin',                    'Programming Languages'),
    ('Swift',                     'Programming Languages'),

    -- Web Development
    ('React',                     'Web Development'),
    ('Angular',                   'Web Development'),
    ('Vue.js',                    'Web Development'),
    ('Node.js',                   'Web Development'),
    ('Django',                    'Web Development'),
    ('FastAPI',                   'Web Development'),
    ('Spring Boot',               'Web Development'),
    ('HTML & CSS',                'Web Development'),
    ('REST API Design',           'Web Development'),
    ('GraphQL',                   'Web Development'),

    -- Cloud & DevOps
    ('AWS',                       'Cloud & DevOps'),
    ('Microsoft Azure',           'Cloud & DevOps'),
    ('Google Cloud Platform',     'Cloud & DevOps'),
    ('Docker',                    'Cloud & DevOps'),
    ('Kubernetes',                'Cloud & DevOps'),
    ('Terraform',                 'Cloud & DevOps'),
    ('CI/CD Pipelines',           'Cloud & DevOps'),
    ('Linux Administration',      'Cloud & DevOps'),
    ('Ansible',                   'Cloud & DevOps'),

    -- Data & Databases
    ('SQL',                       'Data & Databases'),
    ('PostgreSQL',                'Data & Databases'),
    ('MySQL',                     'Data & Databases'),
    ('MongoDB',                   'Data & Databases'),
    ('Redis',                     'Data & Databases'),
    ('Elasticsearch',             'Data & Databases'),
    ('Data Modelling',            'Data & Databases'),

    -- Data Science & AI
    ('Machine Learning',          'Data Science & AI'),
    ('Deep Learning',             'Data Science & AI'),
    ('Natural Language Processing','Data Science & AI'),
    ('Data Analysis',             'Data Science & AI'),
    ('Data Visualization',        'Data Science & AI'),
    ('Apache Spark',              'Data Science & AI'),

    -- Quality Assurance
    ('Manual Testing',            'Quality Assurance'),
    ('Automation Testing',        'Quality Assurance'),
    ('Selenium',                  'Quality Assurance'),
    ('Cypress',                   'Quality Assurance'),
    ('Performance Testing',       'Quality Assurance'),
    ('API Testing',               'Quality Assurance'),

    -- Security
    ('Cybersecurity Fundamentals','Security'),
    ('Penetration Testing',       'Security'),
    ('Network Security',          'Security'),
    ('Identity & Access Management','Security'),
    ('SIEM Tools',                'Security'),

    -- Project & Product Management
    ('Agile & Scrum',             'Project & Product Management'),
    ('JIRA',                      'Project & Product Management'),
    ('Product Roadmapping',       'Project & Product Management'),
    ('Risk Management',           'Project & Product Management'),
    ('Stakeholder Management',    'Project & Product Management'),

    -- Soft Skills
    ('Communication',             'Soft Skills'),
    ('Leadership',                'Soft Skills'),
    ('Problem Solving',           'Soft Skills'),
    ('Team Collaboration',        'Soft Skills'),
    ('Time Management',           'Soft Skills'),

    -- Finance & Accounting
    ('Financial Modelling',       'Finance & Accounting'),
    ('Budgeting & Forecasting',   'Finance & Accounting'),
    ('Taxation',                  'Finance & Accounting'),
    ('Auditing',                  'Finance & Accounting'),
    ('SAP FICO',                  'Finance & Accounting'),

    -- Marketing & Sales
    ('Digital Marketing',         'Marketing & Sales'),
    ('SEO & SEM',                 'Marketing & Sales'),
    ('Content Marketing',         'Marketing & Sales'),
    ('CRM Tools',                 'Marketing & Sales'),
    ('Market Research',           'Marketing & Sales'),
    ('Sales Forecasting',         'Marketing & Sales'),

    -- HR & Legal
    ('Talent Acquisition',        'HR & Legal'),
    ('Employee Engagement',       'HR & Legal'),
    ('Employment Law',            'HR & Legal'),
    ('Contract Drafting',         'HR & Legal'),
    ('Compliance Management',     'HR & Legal');


-- ---------------------------------------------------------------
-- CERTIFICATIONS
-- ---------------------------------------------------------------
-- CertificationLevel enum values assumed: BEGINNER, INTERMEDIATE, ADVANCED
-- (adjust values to match your actual CertificationLevel enum if different)

INSERT INTO certifications (name, certification_level) VALUES
    -- Cloud
    ('AWS Certified Cloud Practitioner',               'BEGINNER'),
    ('AWS Certified Solutions Architect – Associate',  'INTERMEDIATE'),
    ('AWS Certified Solutions Architect – Professional','ADVANCED'),
    ('AWS Certified DevOps Engineer – Professional',   'ADVANCED'),
    ('Microsoft Azure Fundamentals (AZ-900)',          'BEGINNER'),
    ('Microsoft Azure Administrator (AZ-104)',         'INTERMEDIATE'),
    ('Microsoft Azure Solutions Architect (AZ-305)',   'ADVANCED'),
    ('Google Cloud Associate Cloud Engineer',          'INTERMEDIATE'),
    ('Google Cloud Professional Data Engineer',        'ADVANCED'),

    -- DevOps & Infrastructure
    ('Certified Kubernetes Administrator (CKA)',       'ADVANCED'),
    ('Certified Kubernetes Application Developer (CKAD)','INTERMEDIATE'),
    ('HashiCorp Certified: Terraform Associate',       'INTERMEDIATE'),
    ('Docker Certified Associate (DCA)',               'INTERMEDIATE'),
    ('Red Hat Certified Engineer (RHCE)',              'ADVANCED'),

    -- Development
    ('Oracle Certified Professional: Java SE Developer','INTERMEDIATE'),
    ('Python Institute PCEP (Entry-Level)',            'BEGINNER'),
    ('Python Institute PCAP (Associate)',              'INTERMEDIATE'),
    ('Meta Front-End Developer Certificate',           'INTERMEDIATE'),

    -- Data & AI
    ('Google Professional Machine Learning Engineer',  'ADVANCED'),
    ('IBM Data Science Professional Certificate',      'INTERMEDIATE'),
    ('Microsoft Azure AI Engineer (AI-102)',           'ADVANCED'),
    ('Databricks Certified Data Engineer Associate',   'INTERMEDIATE'),

    -- Security
    ('CompTIA Security+',                             'BEGINNER'),
    ('Certified Ethical Hacker (CEH)',                'INTERMEDIATE'),
    ('Certified Information Systems Security Professional (CISSP)', 'ADVANCED'),
    ('CompTIA CySA+',                                 'INTERMEDIATE'),

    -- Quality Assurance
    ('ISTQB Foundation Level',                        'BEGINNER'),
    ('ISTQB Advanced Level Test Analyst',             'ADVANCED'),

    -- Project Management
    ('Project Management Professional (PMP)',          'ADVANCED'),
    ('Certified ScrumMaster (CSM)',                   'INTERMEDIATE'),
    ('PMI Agile Certified Practitioner (PMI-ACP)',    'INTERMEDIATE'),
    ('PRINCE2 Foundation',                            'BEGINNER'),
    ('PRINCE2 Practitioner',                          'ADVANCED'),

    -- Finance & HR
    ('Chartered Financial Analyst (CFA) Level 1',     'BEGINNER'),
    ('Chartered Financial Analyst (CFA) Level 2',     'INTERMEDIATE'),
    ('Certified Public Accountant (CPA)',              'ADVANCED'),
    ('SHRM Certified Professional (SHRM-CP)',          'INTERMEDIATE'),
    ('SHRM Senior Certified Professional (SHRM-SCP)', 'ADVANCED');


-- ---------------------------------------------------------------
-- CERTIFICATION_SKILL_MAPS
-- ---------------------------------------------------------------

-- AWS Certified Cloud Practitioner → AWS
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Cloud Practitioner'),
     (SELECT id FROM skills WHERE name = 'AWS'));

-- AWS Solutions Architect Associate → AWS, Docker, Linux Administration
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Solutions Architect – Associate'),
     (SELECT id FROM skills WHERE name = 'AWS')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Solutions Architect – Associate'),
     (SELECT id FROM skills WHERE name = 'Docker')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Solutions Architect – Associate'),
     (SELECT id FROM skills WHERE name = 'Linux Administration'));

-- AWS Solutions Architect Professional → AWS, Terraform, Kubernetes
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Solutions Architect – Professional'),
     (SELECT id FROM skills WHERE name = 'AWS')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Solutions Architect – Professional'),
     (SELECT id FROM skills WHERE name = 'Terraform')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified Solutions Architect – Professional'),
     (SELECT id FROM skills WHERE name = 'Kubernetes'));

-- AWS Certified DevOps Engineer → AWS, CI/CD Pipelines, Docker, Kubernetes, Ansible
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'AWS Certified DevOps Engineer – Professional'),
     (SELECT id FROM skills WHERE name = 'AWS')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified DevOps Engineer – Professional'),
     (SELECT id FROM skills WHERE name = 'CI/CD Pipelines')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified DevOps Engineer – Professional'),
     (SELECT id FROM skills WHERE name = 'Docker')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified DevOps Engineer – Professional'),
     (SELECT id FROM skills WHERE name = 'Kubernetes')),
    ((SELECT id FROM certifications WHERE name = 'AWS Certified DevOps Engineer – Professional'),
     (SELECT id FROM skills WHERE name = 'Ansible'));

-- Azure Fundamentals → Microsoft Azure
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure Fundamentals (AZ-900)'),
     (SELECT id FROM skills WHERE name = 'Microsoft Azure'));

-- Azure Administrator → Microsoft Azure, Linux Administration
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure Administrator (AZ-104)'),
     (SELECT id FROM skills WHERE name = 'Microsoft Azure')),
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure Administrator (AZ-104)'),
     (SELECT id FROM skills WHERE name = 'Linux Administration'));

-- Azure Solutions Architect → Microsoft Azure, Terraform
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure Solutions Architect (AZ-305)'),
     (SELECT id FROM skills WHERE name = 'Microsoft Azure')),
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure Solutions Architect (AZ-305)'),
     (SELECT id FROM skills WHERE name = 'Terraform'));

-- GCP Associate Cloud Engineer → Google Cloud Platform
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Google Cloud Associate Cloud Engineer'),
     (SELECT id FROM skills WHERE name = 'Google Cloud Platform'));

-- GCP Professional Data Engineer → Google Cloud Platform, Apache Spark, Data Modelling
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Google Cloud Professional Data Engineer'),
     (SELECT id FROM skills WHERE name = 'Google Cloud Platform')),
    ((SELECT id FROM certifications WHERE name = 'Google Cloud Professional Data Engineer'),
     (SELECT id FROM skills WHERE name = 'Apache Spark')),
    ((SELECT id FROM certifications WHERE name = 'Google Cloud Professional Data Engineer'),
     (SELECT id FROM skills WHERE name = 'Data Modelling'));

-- CKA → Kubernetes, Docker, Linux Administration
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Certified Kubernetes Administrator (CKA)'),
     (SELECT id FROM skills WHERE name = 'Kubernetes')),
    ((SELECT id FROM certifications WHERE name = 'Certified Kubernetes Administrator (CKA)'),
     (SELECT id FROM skills WHERE name = 'Docker')),
    ((SELECT id FROM certifications WHERE name = 'Certified Kubernetes Administrator (CKA)'),
     (SELECT id FROM skills WHERE name = 'Linux Administration'));

-- CKAD → Kubernetes, Docker
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Certified Kubernetes Application Developer (CKAD)'),
     (SELECT id FROM skills WHERE name = 'Kubernetes')),
    ((SELECT id FROM certifications WHERE name = 'Certified Kubernetes Application Developer (CKAD)'),
     (SELECT id FROM skills WHERE name = 'Docker'));

-- Terraform Associate → Terraform
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'HashiCorp Certified: Terraform Associate'),
     (SELECT id FROM skills WHERE name = 'Terraform'));

-- Docker Certified Associate → Docker
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Docker Certified Associate (DCA)'),
     (SELECT id FROM skills WHERE name = 'Docker'));

-- RHCE → Linux Administration, Ansible
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Red Hat Certified Engineer (RHCE)'),
     (SELECT id FROM skills WHERE name = 'Linux Administration')),
    ((SELECT id FROM certifications WHERE name = 'Red Hat Certified Engineer (RHCE)'),
     (SELECT id FROM skills WHERE name = 'Ansible'));

-- Oracle Java → Java
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Oracle Certified Professional: Java SE Developer'),
     (SELECT id FROM skills WHERE name = 'Java'));

-- PCEP → Python
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Python Institute PCEP (Entry-Level)'),
     (SELECT id FROM skills WHERE name = 'Python'));

-- PCAP → Python
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Python Institute PCAP (Associate)'),
     (SELECT id FROM skills WHERE name = 'Python'));

-- Meta Front-End Developer → React, JavaScript, HTML & CSS
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Meta Front-End Developer Certificate'),
     (SELECT id FROM skills WHERE name = 'React')),
    ((SELECT id FROM certifications WHERE name = 'Meta Front-End Developer Certificate'),
     (SELECT id FROM skills WHERE name = 'JavaScript')),
    ((SELECT id FROM certifications WHERE name = 'Meta Front-End Developer Certificate'),
     (SELECT id FROM skills WHERE name = 'HTML & CSS'));

-- Google ML Engineer → Machine Learning, Deep Learning, Google Cloud Platform
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Google Professional Machine Learning Engineer'),
     (SELECT id FROM skills WHERE name = 'Machine Learning')),
    ((SELECT id FROM certifications WHERE name = 'Google Professional Machine Learning Engineer'),
     (SELECT id FROM skills WHERE name = 'Deep Learning')),
    ((SELECT id FROM certifications WHERE name = 'Google Professional Machine Learning Engineer'),
     (SELECT id FROM skills WHERE name = 'Google Cloud Platform'));

-- IBM Data Science → Python, Data Analysis, Machine Learning, Data Visualization
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'IBM Data Science Professional Certificate'),
     (SELECT id FROM skills WHERE name = 'Python')),
    ((SELECT id FROM certifications WHERE name = 'IBM Data Science Professional Certificate'),
     (SELECT id FROM skills WHERE name = 'Data Analysis')),
    ((SELECT id FROM certifications WHERE name = 'IBM Data Science Professional Certificate'),
     (SELECT id FROM skills WHERE name = 'Machine Learning')),
    ((SELECT id FROM certifications WHERE name = 'IBM Data Science Professional Certificate'),
     (SELECT id FROM skills WHERE name = 'Data Visualization'));

-- Azure AI Engineer → Microsoft Azure, Natural Language Processing, Machine Learning
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure AI Engineer (AI-102)'),
     (SELECT id FROM skills WHERE name = 'Microsoft Azure')),
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure AI Engineer (AI-102)'),
     (SELECT id FROM skills WHERE name = 'Natural Language Processing')),
    ((SELECT id FROM certifications WHERE name = 'Microsoft Azure AI Engineer (AI-102)'),
     (SELECT id FROM skills WHERE name = 'Machine Learning'));

-- Databricks Data Engineer → Apache Spark, SQL, Python
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Databricks Certified Data Engineer Associate'),
     (SELECT id FROM skills WHERE name = 'Apache Spark')),
    ((SELECT id FROM certifications WHERE name = 'Databricks Certified Data Engineer Associate'),
     (SELECT id FROM skills WHERE name = 'SQL')),
    ((SELECT id FROM certifications WHERE name = 'Databricks Certified Data Engineer Associate'),
     (SELECT id FROM skills WHERE name = 'Python'));

-- CompTIA Security+ → Cybersecurity Fundamentals, Network Security
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'CompTIA Security+'),
     (SELECT id FROM skills WHERE name = 'Cybersecurity Fundamentals')),
    ((SELECT id FROM certifications WHERE name = 'CompTIA Security+'),
     (SELECT id FROM skills WHERE name = 'Network Security'));

-- CEH → Penetration Testing, Network Security, Cybersecurity Fundamentals
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Certified Ethical Hacker (CEH)'),
     (SELECT id FROM skills WHERE name = 'Penetration Testing')),
    ((SELECT id FROM certifications WHERE name = 'Certified Ethical Hacker (CEH)'),
     (SELECT id FROM skills WHERE name = 'Network Security')),
    ((SELECT id FROM certifications WHERE name = 'Certified Ethical Hacker (CEH)'),
     (SELECT id FROM skills WHERE name = 'Cybersecurity Fundamentals'));

-- CISSP → Cybersecurity Fundamentals, Identity & Access Management, Network Security, SIEM Tools
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Certified Information Systems Security Professional (CISSP)'),
     (SELECT id FROM skills WHERE name = 'Cybersecurity Fundamentals')),
    ((SELECT id FROM certifications WHERE name = 'Certified Information Systems Security Professional (CISSP)'),
     (SELECT id FROM skills WHERE name = 'Identity & Access Management')),
    ((SELECT id FROM certifications WHERE name = 'Certified Information Systems Security Professional (CISSP)'),
     (SELECT id FROM skills WHERE name = 'Network Security')),
    ((SELECT id FROM certifications WHERE name = 'Certified Information Systems Security Professional (CISSP)'),
     (SELECT id FROM skills WHERE name = 'SIEM Tools'));

-- CompTIA CySA+ → SIEM Tools, Cybersecurity Fundamentals
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'CompTIA CySA+'),
     (SELECT id FROM skills WHERE name = 'SIEM Tools')),
    ((SELECT id FROM certifications WHERE name = 'CompTIA CySA+'),
     (SELECT id FROM skills WHERE name = 'Cybersecurity Fundamentals'));

-- ISTQB Foundation → Manual Testing, API Testing
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'ISTQB Foundation Level'),
     (SELECT id FROM skills WHERE name = 'Manual Testing')),
    ((SELECT id FROM certifications WHERE name = 'ISTQB Foundation Level'),
     (SELECT id FROM skills WHERE name = 'API Testing'));

-- ISTQB Advanced → Automation Testing, Performance Testing, Selenium
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'ISTQB Advanced Level Test Analyst'),
     (SELECT id FROM skills WHERE name = 'Automation Testing')),
    ((SELECT id FROM certifications WHERE name = 'ISTQB Advanced Level Test Analyst'),
     (SELECT id FROM skills WHERE name = 'Performance Testing')),
    ((SELECT id FROM certifications WHERE name = 'ISTQB Advanced Level Test Analyst'),
     (SELECT id FROM skills WHERE name = 'Selenium'));

-- PMP → Agile & Scrum, Risk Management, Stakeholder Management
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Project Management Professional (PMP)'),
     (SELECT id FROM skills WHERE name = 'Agile & Scrum')),
    ((SELECT id FROM certifications WHERE name = 'Project Management Professional (PMP)'),
     (SELECT id FROM skills WHERE name = 'Risk Management')),
    ((SELECT id FROM certifications WHERE name = 'Project Management Professional (PMP)'),
     (SELECT id FROM skills WHERE name = 'Stakeholder Management'));

-- CSM → Agile & Scrum, JIRA
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Certified ScrumMaster (CSM)'),
     (SELECT id FROM skills WHERE name = 'Agile & Scrum')),
    ((SELECT id FROM certifications WHERE name = 'Certified ScrumMaster (CSM)'),
     (SELECT id FROM skills WHERE name = 'JIRA'));

-- PMI-ACP → Agile & Scrum, Product Roadmapping, Risk Management
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'PMI Agile Certified Practitioner (PMI-ACP)'),
     (SELECT id FROM skills WHERE name = 'Agile & Scrum')),
    ((SELECT id FROM certifications WHERE name = 'PMI Agile Certified Practitioner (PMI-ACP)'),
     (SELECT id FROM skills WHERE name = 'Product Roadmapping')),
    ((SELECT id FROM certifications WHERE name = 'PMI Agile Certified Practitioner (PMI-ACP)'),
     (SELECT id FROM skills WHERE name = 'Risk Management'));

-- PRINCE2 Foundation → Risk Management, Stakeholder Management
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'PRINCE2 Foundation'),
     (SELECT id FROM skills WHERE name = 'Risk Management')),
    ((SELECT id FROM certifications WHERE name = 'PRINCE2 Foundation'),
     (SELECT id FROM skills WHERE name = 'Stakeholder Management'));

-- PRINCE2 Practitioner → Risk Management, Stakeholder Management, Product Roadmapping
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'PRINCE2 Practitioner'),
     (SELECT id FROM skills WHERE name = 'Risk Management')),
    ((SELECT id FROM certifications WHERE name = 'PRINCE2 Practitioner'),
     (SELECT id FROM skills WHERE name = 'Stakeholder Management')),
    ((SELECT id FROM certifications WHERE name = 'PRINCE2 Practitioner'),
     (SELECT id FROM skills WHERE name = 'Product Roadmapping'));

-- CFA Level 1 → Financial Modelling, Budgeting & Forecasting
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Chartered Financial Analyst (CFA) Level 1'),
     (SELECT id FROM skills WHERE name = 'Financial Modelling')),
    ((SELECT id FROM certifications WHERE name = 'Chartered Financial Analyst (CFA) Level 1'),
     (SELECT id FROM skills WHERE name = 'Budgeting & Forecasting'));

-- CFA Level 2 → Financial Modelling, Auditing, Taxation
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Chartered Financial Analyst (CFA) Level 2'),
     (SELECT id FROM skills WHERE name = 'Financial Modelling')),
    ((SELECT id FROM certifications WHERE name = 'Chartered Financial Analyst (CFA) Level 2'),
     (SELECT id FROM skills WHERE name = 'Auditing')),
    ((SELECT id FROM certifications WHERE name = 'Chartered Financial Analyst (CFA) Level 2'),
     (SELECT id FROM skills WHERE name = 'Taxation'));

-- CPA → Auditing, Taxation, SAP FICO
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'Certified Public Accountant (CPA)'),
     (SELECT id FROM skills WHERE name = 'Auditing')),
    ((SELECT id FROM certifications WHERE name = 'Certified Public Accountant (CPA)'),
     (SELECT id FROM skills WHERE name = 'Taxation')),
    ((SELECT id FROM certifications WHERE name = 'Certified Public Accountant (CPA)'),
     (SELECT id FROM skills WHERE name = 'SAP FICO'));

-- SHRM-CP → Talent Acquisition, Employee Engagement, Compliance Management
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'SHRM Certified Professional (SHRM-CP)'),
     (SELECT id FROM skills WHERE name = 'Talent Acquisition')),
    ((SELECT id FROM certifications WHERE name = 'SHRM Certified Professional (SHRM-CP)'),
     (SELECT id FROM skills WHERE name = 'Employee Engagement')),
    ((SELECT id FROM certifications WHERE name = 'SHRM Certified Professional (SHRM-CP)'),
     (SELECT id FROM skills WHERE name = 'Compliance Management'));

-- SHRM-SCP → Talent Acquisition, Employee Engagement, Employment Law, Compliance Management
INSERT INTO certification_skill_maps (certification_id, skill_id) VALUES
    ((SELECT id FROM certifications WHERE name = 'SHRM Senior Certified Professional (SHRM-SCP)'),
     (SELECT id FROM skills WHERE name = 'Talent Acquisition')),
    ((SELECT id FROM certifications WHERE name = 'SHRM Senior Certified Professional (SHRM-SCP)'),
     (SELECT id FROM skills WHERE name = 'Employee Engagement')),
    ((SELECT id FROM certifications WHERE name = 'SHRM Senior Certified Professional (SHRM-SCP)'),
     (SELECT id FROM skills WHERE name = 'Employment Law')),
    ((SELECT id FROM certifications WHERE name = 'SHRM Senior Certified Professional (SHRM-SCP)'),
     (SELECT id FROM skills WHERE name = 'Compliance Management'));