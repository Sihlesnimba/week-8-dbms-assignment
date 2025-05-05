from fastapi import FastAPI, HTTPException
from models import Student, Course
from database import engine, SessionLocal, Base
from crud import *

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/students")
def list_students():
    return get_students()

@app.post("/students")
def add_student(student: Student):
    return create_student(student)

@app.get("/courses")
def list_courses():
    return get_courses()

@app.post("/courses")
def add_course(course: Course):
    return create_course(course)
