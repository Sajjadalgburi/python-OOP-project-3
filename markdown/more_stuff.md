# Hospital Management System - Class Structure

## 1. `Hospital`

Acts as a central hub, managing core functionalities and linking classes.

### Attributes

- `name`
- `location`
- `departments`
- `staff_list`
- `patient_list`
- `appointments`

### Methods

- `add_department()`: Add a new department to the hospital.
- `add_staff()`: Register a new staff member.
- `add_patient()`: Register a new patient.
- `view_schedule()`: Display the schedule for doctors and nurses.
- `generate_reports()`: Generate reports for hospital administration.

---

## 2. `Person` (Abstract Base Class)

Defines shared attributes and methods for all people (e.g., patients, doctors, nurses).

### Attributes

- `name`
- `age`
- `gender`
- `contact_info`

### Methods

- `update_contact_info()`: Update the contact information of a person.

---

### Subclasses of `Person`

### **Patient**

Contains unique patient attributes and methods.

#### Attributes

- `medical_history`
- `insurance_details`
- `appointments`

#### Methods

- `view_appointments()`: View the patient's upcoming appointments.
- `request_appointment()`: Request a new appointment.
- `view_medical_history()`: View a summary of the patient’s medical history.

---

### **Doctor**

Specialized attributes and methods for doctors.

#### Attributes

- `specialization`
- `license_number`
- `schedule`
- `patients`

#### Methods

- `view_patient_history()`: View the medical history of a specific patient.
- `prescribe_medication()`: Prescribe medication for a patient.
- `update_schedule()`: Update the doctor's schedule.

---

### **Nurse**

Attributes and methods unique to nurses.

#### Attributes

- `assigned_patients`
- `schedule`

#### Methods

- `administer_medication()`: Administer medication to a patient.
- `record_vitals()`: Record a patient's vital signs.
- `update_schedule()`: Update the nurse's schedule.

---

## 3. `Appointment`

Manages appointment scheduling, rescheduling, and cancellations.

### Attributes

- `appointment_date`
- `patient`
- `doctor`
- `status`

### Methods

- `schedule_appointment()`: Schedule a new appointment.
- `reschedule_appointment()`: Reschedule an existing appointment.
- `cancel_appointment()`: Cancel an appointment.
- `check_conflicts()`: Check for schedule conflicts for doctors.

---

## 4. `MedicalRecord`

Stores patient health information, test results, diagnoses, and prescriptions.

### Attributes

- `patient`
- `test_results`
- `diagnoses`
- `prescriptions`

### Methods

- `add_diagnosis()`: Add a new diagnosis.
- `add_prescription()`: Add a new prescription for the patient.
- `view_record()`: View the patient's medical record (limited access).

---

## 5. `Treatment`

Represents treatments or procedures provided to patients.

### Attributes

- `patient`
- `treatment_type`
- `date`
- `cost`

### Methods

- `record_treatment()`: Record a treatment for a patient.
- `view_treatment_details()`: View details of a specific treatment.

---

## Essential Features

### Appointment Management

- **Scheduling**: Patients can schedule, reschedule, or cancel appointments.
- **Conflict Checking**: Ensure no overlap in a doctor’s schedule.

### Medical Records Access

- **Limited Access**: Only doctors and nurses can view/edit patient records, while patients can view a summary.

### Billing and Insurance

- **Billing Generation**: Calculate bills based on treatments and calculate out-of-pocket expenses.
- **Insurance Coverage Check**: Confirm if a treatment is covered by insurance.

### Staff Assignment

- **Nurse Assignments**: Assign nurses to patients on a per-need or shift basis.

---

## Advanced Options

### Notification System

- Notify patients about upcoming appointments or test results.

### Shift Management for Staff

- Track and manage doctors’ and nurses’ shifts for proper scheduling.

### Patient Portal Interface

- Build a CLI where patients and staff can log in and access specific information.
