class Patient:
    def __init__(
        self, medical_history: list[dict] = None, insurance_details: list[dict] = None
    ) -> None:
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
