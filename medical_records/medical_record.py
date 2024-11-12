from person import Person

# Stores patient health information, test results, diagnoses, and prescriptions.

class MedicalRecord:
  def __init__(self, patient: Person, test_results: list[str], diagnoses: list[str], prescriptions: list[str]) -> None:
    self.patient = patient  # Store the patient associated with the record
    self.test_results = test_results
    self.prescriptions = prescriptions
    self.diagnoses = diagnoses

  def add_diagnosis(self, diagnosis: str) -> None:
    pass
  
  def add_prescription(self, prescription: str) -> None:
    pass