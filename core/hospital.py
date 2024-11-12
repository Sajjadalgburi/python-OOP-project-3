from typing import Literal

# Acts as a central hub, managing core functionalities and linking classes.
class Hospital:
    def __init__(
        self,
        name: str,
        location: str,
        departments: list[str],
    ) -> None:
        self.name = name
        self.location = location
        self.departments = departments if departments is not None else [
            'Emergency',
            'Surgery',
            'Cardiology', # specializes in heart and cardiovascular health
            'Pediatrics', # provides care for children and adolescents.
        ] 
        self.__nurse_list = []
        self.__patient_list = []
        self.__doctor_list = []
        self.appointments = [] # stores all appointments made
        

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
    
    #  list of the allpast appointments
    def past_appointments(self):
        pass
    
    # list of the future appointments
    def future_appointments(self):
        pass
    
    def access_catalog(self, input: Literal["Doctors", "Nurses", "Patients"] = "Doctors"):
        valid_inputs = ["Doctors", "Nurses", "Patients"]
        
        if input not in valid_inputs:
            raise TypeError('input must be "Doctors", "Nurses", or "Patients"')
        
        # Mapping input to corresponding list
        catalog = {
            "Doctors": self.__doctor_list,
            "Nurses": self.__nurse_list,
            "Patients": self.__patient_list
        }
        
        print(f"\nAll of the {input.lower()} in the hospital system: ")
        for person in catalog[input]:
            print(person)
