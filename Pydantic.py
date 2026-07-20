from pydantic import BaseModel , EmailStr , AnyUrl , Field 
from typing import List, Dict , Optional ,Annotated
class Patient(BaseModel):
    # type hints
    name:  Annotated[str,Field(max_length=5, title='created a name ',description='Given test')]  #meta-data added
    rollno: int
    marks: Annotated[float,Field(strict=True)]
    files: List[str]
    subject: Optional[Dict[str,int]] = None
    email: EmailStr
    linkedin_url : AnyUrl
    pass_percentage : int =Field(gt=33)
def insert_patient(patient: Patient):
    
    print(patient.name)
    print(patient.rollno)
    print(patient.files)
    print(patient.marks)
    print(patient.subject)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.pass_percentage)
patient1 = {'name':'shlok','rollno':123,'marks':44,
            'files':['Maths', 'Chem', 'Phy'],
            'subject':{'maths':'44'},
            'email': 'shlokt@gmail.com',
            'linkedin_url':'https://linkedin.com',
            'pass_percentage':'62'
            }

# pydantic object
patient2 = Patient(**patient1) 

insert_patient(patient2)