"""Core data models for education system."""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class CourseStatus(str, Enum):
    """Course status enumeration."""
    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"
    INACTIVE = "inactive"


class EnrollmentStatus(str, Enum):
    """Enrollment status enumeration."""
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    DROPPED = "dropped"


@dataclass
class Student:
    """Student model."""
    student_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"


@dataclass
class Course:
    """Course model."""
    course_id: str
    code: str
    name: str
    description: str
    instructor_id: str
    status: CourseStatus = CourseStatus.DRAFT
    credits: int = 3
    capacity: int = 30
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


@dataclass
class Enrollment:
    """Enrollment model."""
    enrollment_id: str
    student_id: str
    course_id: str
    status: EnrollmentStatus = EnrollmentStatus.PENDING
    grade: Optional[float] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __str__(self) -> str:
        return f"{self.student_id} -> {self.course_id}"


@dataclass
class Assessment:
    """Assessment model."""
    assessment_id: str
    course_id: str
    student_id: str
    title: str
    score: float
    max_score: float
    assessment_type: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def percentage(self) -> float:
        """Calculate percentage score."""
        return (self.score / self.max_score * 100) if self.max_score > 0 else 0
