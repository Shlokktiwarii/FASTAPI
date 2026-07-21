from pydantic import BaseModel
class Address(BaseModel):
    city: str
    state: str
    pin:int

class Student(BaseModel):
    name: str
    address: Address

address_dict = {'city': 'lucknow', 'state': 'uttar pradesh', 'pin': '226001'}
address1 = Address(**address_dict)
student_dict = {'name': 'shlok', 'address': address1}
student1 = Student(**student_dict)

print(student1.address.pin)

temp = student1.model_dump(exclude={'address':['state']})
print(temp)
print(type(temp))
    