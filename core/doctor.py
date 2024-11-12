from typing import Literal
from person import *

"""
General Practitioner (Family Medicine):
    Specialization: Primary care and general health.
    Typical Role: Provides comprehensive healthcare, conducts routine checkups, diagnoses common illnesses, and refers patients to specialists as needed.
    Common Attributes: Preventive care, holistic patient management.

Cardiologist (Heart Specialist):
    Specialization: Cardiovascular system.
    Typical Role: Diagnoses and treats heart conditions and related issues, including hypertension, heart disease, and arrhythmias.
    Common Attributes: Specialized equipment and tests, high expertise in cardiovascular care.

Pediatrician (age < 18):
    Specialization: Child and adolescent health.
    Typical Role: Provides medical care for infants, children, and teenagers, addressing age-specific developmental needs and health conditions.
    Common Attributes: Knowledge of pediatric growth stages, immunization schedules, and child-specific illnesses.
"""


class Doctor:

    def __init__(
        self,
        name: str,
        age: int,
        department: str,
        contact_info: ContactInfo,
        gender: Literal["Male", "Female"],
        license_number: str,  # will be a UUID
        specialization: Literal[
            "General Practitioner", "Practitioner", "Cardiologist", "Surgeon"
        ] = "General Practitioner",
        schedule: list[dict] = None,
    ) -> None:
        super().__init__(name, age, gender, contact_info)
        self.specialization = specialization
        self.schedule = (
            schedule
            if schedule is not None
            else [
                {"day": "Mon", "appointments": []},
                {"day": "Tue", "appointments": []},
                {"day": "Wed", "appointments": []},
                {"day": "Thu", "appointments": []},
                {"day": "Fri", "appointments": []},
                {"day": "Sat", "appointments": []},
                {"day": "Sun", "appointments": []},
            ]
        )
        self.license_number = license_number
        self.max_patients_per_day = 16
        self.max_hours_per_day = 10
        self.department = department if department is not None else TypeError('TypeError: department is required')

    def view_patient_history(self) -> None:
        pass

    def prescribe_medication(self) -> None:
        pass
