from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    rollno: int

def insert_patient(patient: Patient):
    
    print(patient.name)
    print(patient.rollno)

patient1 = {'name':'shlok','rollno':'123'}

patient2 = Patient(**patient1)

insert_patient(patient2)