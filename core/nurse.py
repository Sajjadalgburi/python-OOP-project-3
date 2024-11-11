class Nurse:

    def __init__(self, assigned_patients, schedule) -> None:
        self.assigned_patients = assigned_patients
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

    def administer_medication(self):
        pass

    def record_vitals(self):
        pass
