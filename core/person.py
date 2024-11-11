from abc import ABC, abstractmethod
from typing import Literal, TypedDict


# Define a TypedDict for contact_info
class ContactInfo(TypedDict):
    email: str
    phone: str
    address: str


# Base class for people in the hospital
class Person(ABC):

    def __init__(
        self,
        name: str,
        age: int,
        gender: Literal["Male", "Female"],
        contact_info: ContactInfo,
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info

    # Abstract method for polymorphism in "Nurse" and "doctor" class
    @abstractmethod
    def access_privileges(self):
        pass
