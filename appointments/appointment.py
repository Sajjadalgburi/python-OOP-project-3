from typing import Literal
from person import Person


# Class to manage appointments, scheduling, rescheduling, and cancellations.
class Appointment:
    def __init__(
        self,
        appointment_date: str,
        patient: Person,
        doctor: Person,
        status: Literal["Scheduled", "Rescheduled", "Completed", "Canceled"],
    ) -> None:
        self.appointment_date = appointment_date
        self.patient = patient.name
        self.doctor = doctor.name
        self.status = status

    def schedule(self):
        self.status = "Scheduled"
        print(
            f"Appointment scheduled for {self.patient.name} with Dr. {
                self.doctor.name} on {self.appointment_date}"
        )

    def reschedule(self, new_date: str):
        self.appointment_date = new_date
        self.status = "Rescheduled"
        print(f"Appointment rescheduled to {self.appointment_date}")

    def cancel_schedule(self):
        self.status = "Canceled"
        print(
            f"Appointment for {self.patient.name} on {
                self.appointment_date} has been canceled"
        )
