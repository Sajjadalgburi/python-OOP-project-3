# Acts as a central hub, managing core functionalities and linking classes.
class Hospital:
    def __init__(
        self,
        name,
        location,
    ) -> None:
        self.name = name
        self.location = location
        self.departments = None  # Not sure if this should be passed in the param?
        self.__staff_list = []
        self.__patient_list = []
        self.appointments = (
            []
        )  # does this store all past appointments that have been made?

        # Add a new department to the hospital.
        def add_department(self):
            pass

        def add_staff(self):
            pass

        def add_patient(self):
            pass

        # Display the schedule for doctors and nurses.
        def view_schedule(self):
            pass

        # Generate reports for hospital administration.
        def generate_reports(self):
            pass
