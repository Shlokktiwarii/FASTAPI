from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator , model_validator , computed_field
from typing import Annotated, Dict, List, Optional

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=5, title='created a name', description='Given test')]
    rollno: int
    marks: Annotated[float, Field(strict=True)]
    files: List[str]
    subject: Optional[Dict[str, int]] = None
    email: EmailStr
    linkedin_url: AnyUrl
    pass_percentage: int = Field(gt=33)
    contacts: int 
    lowestscore: int

    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['hdfc.com', 'pnb.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value
    
    @field_validator('rollno',mode='after')
    @classmethod
    def rollno_checker(cls , value):
        if 0<value<100:
            return value
        else:
            raise ValueError('roll no is incorrect')
        
    @model_validator(mode='after')
    def evaluator(self):
        if self.rollno < 100 and self.contacts > 0:
            return self
        raise ValueError('Not an ideal model')
        
    @computed_field
    @property
    def averages(self) -> float:
        return round(self.marks / (self.lowestscore ** 2), 2)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.rollno)
    print(patient.files)
    print(patient.marks)
    print(patient.subject)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.pass_percentage)
    print(patient.averages)


patient1 = {
    'name': 'shlok',
    'rollno': '13',
    'marks': 44,
    'lowestscore':10, 
    'files': ['Maths', 'Chem', 'Phy'],
    'subject': {'maths': 44},
    'email': 'shlok@pnb.com',
    'linkedin_url': 'https://linkedin.com',
    'pass_percentage': 62,
    'contacts':55,

}

patient2 = Patient(**patient1)
insert_patient(patient2)
