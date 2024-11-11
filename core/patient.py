from person import *


class Patient(Person):
    def __init__(
        self,
        name: str,
        age: int,
        gender: Literal["Male", "Female"],
        contact_info: ContactInfo,
        medical_history: list[dict] = None,
        insurance_details: list[dict] = None,
    ) -> None:
        super().__init__(name, age, gender, contact_info)
        # Initialize medical history, defaulting to an empty list if none provided
        self.medical_history = medical_history if medical_history is not None else []

        # Initialize insurance details, defaulting to an empty list if none provided
        self.insurance_details = (
            insurance_details if insurance_details is not None else []
        )

    def view_appointments(self) -> None:
        pass

    def request_appointment(self) -> None:
        pass
