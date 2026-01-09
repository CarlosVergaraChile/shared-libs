# Shared Libraries - CarlosVergaraChile Ecosystem

Central repository for shared libraries and utilities across all 25 repositories in the ecosystem.

## Structure

```
shared-libs/
├── python/          # Python utilities
│   ├── educore/      # Core education utilities
│   ├── analytics/    # Analytics helpers
│   └── security/     # Security utilities
├── go/              # Go utilities
│   ├── eduapi/       # API utilities
│   ├── cache/        # Caching helpers
│   └── messaging/    # Message queue wrappers
└── js/              # JavaScript/TypeScript utilities
    ├── components/  # Reusable UI components
    ├── hooks/       # React hooks
    └── utils/       # Utility functions
```

## Python Libraries

### educore
Core education data models and utilities.

```python
from educore import Student, Course, Enrollment, Assessment
from educore import validate_email, validate_phone
from educore.decorators import cache, retry, log_call
```

**Models:**
- `Student`: Student profile and information
- `Course`: Course definition with metadata
- `Enrollment`: Student course enrollment
- `Assessment`: Student assessment results

**Validators:**
- `validate_email()`: Email format validation
- `validate_phone()`: Phone number validation
- `validate_course_code()`: Course code validation

**Decorators:**
- `@cache`: Caching decorator for functions
- `@retry`: Retry logic for failing operations
- `@log_call`: Automatic logging of function calls

### analytics
Analytics and reporting utilities.

### security
Security utilities including encryption and validation.

## Go Libraries

### eduapi
HTTP API utilities and helpers.

### cache
Caching abstractions for Redis and in-memory caching.

### messaging
Message queue wrappers for RabbitMQ and Kafka.

## JavaScript/TypeScript Libraries

### components
Reusable React components for the UI ecosystem.

### hooks
Custom React hooks for common patterns.

### utils
Utility functions for frontend development.

## Installation

### Python
```bash
pip install -e python/educore
```

### Go
```bash
go get github.com/CarlosVergaraChile/shared-libs/go/eduapi
```

### JavaScript
```bash
npm install CarlosVergaraChile/shared-libs#main
```

## Usage Examples

### Python
```python
from educore import Student, validate_email
from educore.decorators import cache

@cache(ttl=3600)
def get_student(student_id: str) -> Student:
    # Cached function
    pass

email = "student@university.edu"
if validate_email(email):
    student = Student(
        student_id="STU001",
        first_name="John",
        last_name="Doe",
        email=email
    )
```

### Go
```go
import "github.com/CarlosVergaraChile/shared-libs/go/eduapi"

handler := eduapi.NewRequestValidator()
if err := handler.Validate(request); err != nil {
    // Handle validation error
}
```

### JavaScript
```typescript
import { useStudentData } from '@/hooks/useStudentData';
import { StudentCard } from '@/components/StudentCard';

function StudentDashboard() {
    const { student, loading } = useStudentData();
    return <StudentCard student={student} loading={loading} />;
}
```

## Contributing

1. Create a new branch for your feature
2. Implement the library utility
3. Add unit tests (min 80% coverage)
4. Update relevant documentation
5. Submit a pull request

## Testing

```bash
# Python
cd python && pytest --cov

# Go
go test ./...

# JavaScript
npm test
```

## Versioning

Follows Semantic Versioning (MAJOR.MINOR.PATCH)

## License

MIT License - See LICENSE file

## Support

For questions or issues, please open an issue on GitHub or contact the architecture team.
