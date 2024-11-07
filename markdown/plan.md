# Hospital Management System

## Key Classes

- **Hospital**: Acts as a central hub for the hospital system.

1. **Person** (abstract base class): Shared attributes and methods for all people (patients, doctors, nurses).

   - **Patient**: Has unique attributes like `medical_history`, `insurance_details`, and methods like `view_appointments()` and `request_appointment()`.
   - **Doctor**: Includes `specialization`, `schedule`, `view_patient_history()`, and `prescribe_medication()`.
   - **Nurse**: Has access to `assigned_patients`, `schedule`, and methods like `administer_medication()` and `record_vitals()`.

2. **Appointment**: Manages appointment scheduling, rescheduling, and cancellations, linked to both `Patient` and `Doctor`.

3. **MedicalRecord**: Contains patient health information, test results, diagnoses, and prescriptions, with limited access.

4. **Treatment**: Represents treatments or procedures, linking patients to specific treatments received.

## Essential Features

### Appointment Management

- **Scheduling**: Patients can schedule, reschedule, or cancel appointments.
- **Conflict Checking**: Ensure no overlap in a doctor’s schedule.

### Medical Records Access

- Only doctors and nurses can view/edit patient records.
- Patients can view a summary of their medical history.

### Billing and Insurance

- Generate bills based on treatment, check if the treatment is covered by insurance, and calculate out-of-pocket expenses.

### Staff Assignment

- Assign nurses to patients, either for specific shifts or on a per-need basis.

## Advanced Options

- **Notification System**: Notify patients about upcoming appointments or test results.
- **Shift Management for Staff**: Track and manage doctors’ and nurses’ shifts, allowing for proper scheduling and time-off management.
- **Patient Portal Interface**: Build a simple CLI where patients and staff log in with access to their specific information.
