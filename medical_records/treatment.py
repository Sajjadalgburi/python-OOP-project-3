from person import Person

# Stores patient health information, test results, diagnoses, and prescriptions.

class Treatment:
  def __init__(self, patient: Person, treatment_type: str, date: str, cost: float) -> None:
    self.patient = patient  # Store the patient associated with the record
    self.treatment_type = treatment_type
    self.date = date
    self.cost = cost

  #  Record a treatment for a patient.
  def record_treatment(self, diagnosis: str) -> None:
    pass
  
  # View details of a specific treatment.
  def view_treatment_details(self) -> None:
    pass