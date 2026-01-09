"""EDU-CORE: Core education utilities and helpers.

Core functionality for the educational ecosystem.
"""

__version__ = "1.0.0"
__author__ = "CarlosVergaraChile"

from .models import (
    Student,
    Course,
    Enrollment,
    Assessment,
)

from .validators import (
    validate_email,
    validate_phone,
    validate_course_code,
)

from .decorators import (
    retry,
    cache,
    log_call,
)

__all__ = [
    'Student',
    'Course',
    'Enrollment',
    'Assessment',
    'validate_email',
    'validate_phone',
    'validate_course_code',
    'retry',
    'cache',
    'log_call',
]
