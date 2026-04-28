-- Create custom enum types
CREATE TYPE certification_level AS ENUM ('BEGINNER', 'INTERMEDIATE', 'ADVANCED', 'EXPERT');
CREATE TYPE project_status AS ENUM ('ONGOING', 'COMPLETED', 'READY', 'TERMINATED');
CREATE TYPE employee_status AS ENUM ('WORKING', 'LEFT');
CREATE TYPE employee_skill_level AS ENUM ('BEGINNER', 'INTERMEDIATE', 'ADVANCED', 'EXPERT');