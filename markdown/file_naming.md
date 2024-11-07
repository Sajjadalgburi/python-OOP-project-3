## 2. File Naming Conventions

### Use Snake Case for Files

- Use lowercase letters with underscores between words, e.g., `medical_record.py`, `appointment.py`.
- Avoid hyphens or camel case, as snake case is the standard in Python.

### Group by Purpose

- Name files according to the functionality they contain, providing clear context for developers to find relevant code.
- **Example**: For handling billing logic, include files like `billing_manager.py` and `insurance_checker.py` in a `billing` directory.

### Tests

- Use a `tests/` directory for unit and integration tests.
- Start test files with `test_` and match the file they’re testing, e.g., `test_hospital.py` for `hospital.py`.
- Use a naming convention like `test_functionality` for test methods and functions for clarity.

### Utilities

- Place general-purpose helpers and utilities in a `utils/` folder.
- Name files according to function, such as `database.py` for database handling and `logger.py` for logging utilities.

## 3. Module Naming Patterns

### Core Classes

- Classes that serve as core entities (`Patient`, `Doctor`, `Nurse`) should go in a `core` or similarly named directory, with each main class in its own file.
- **Example**: `core/patient.py`, `core/doctor.py`, `core/nurse.py`.

### Managers and Controllers

- Files that manage complex operations or serve as intermediaries for class interactions (e.g., scheduling, billing) should use a suffix like `_manager.py` or `_controller.py`.
- **Example**: `schedule_manager.py`, `billing_manager.py`.

## 4. Interface and Presentation Layer

- For interfaces or any front-end component like a CLI, group related files in an `interfaces/` directory.
- Use descriptive names like `cli_interface.py` for command-line logic and `patient_portal.py` for patient-facing functionalities.

---

Following these conventions will help keep your project organized, scalable, and easy to maintain. Let me know if you'd like more details on any specific section!
