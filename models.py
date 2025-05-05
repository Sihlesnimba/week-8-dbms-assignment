from pydantic import BaseModel

class Student(BaseModel):
    first_name: str
    last_name: str
    email: str

class Course(BaseModel):
    course_name: str
    course_code: str
