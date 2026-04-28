from enum import Enum

class CertificationLevel(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    EXPERT = "EXPERT"

class ProjectStatus(Enum):
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"
    READY = "READY"
    TERMINATED = "TERMINATED"

class EmployeeStatus(Enum):
    WORKING = "WORKING"
    LEFT = "LEFT"

class EmployeeSkillLevel(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    EXPERT = "EXPERT"
