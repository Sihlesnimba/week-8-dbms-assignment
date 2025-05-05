from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Session
from database import Base, SessionLocal

class StudentDB(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class CourseDB(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)
    course_code = Column(String(10), unique=True, nullable=False)

def get_students():
    db = SessionLocal()
    students = db.query(StudentDB).all()
    db.close()
    return students

def create_student(student):
    db = SessionLocal()
    student_obj = StudentDB(**student.dict())
    db.add(student_obj)
    db.commit()
    db.refresh(student_obj)
    db.close()
    return student_obj

def get_courses():
    db = SessionLocal()
    courses = db.query(CourseDB).all()
    db.close()
    return courses

def create_course(course):
    db = SessionLocal()
    course_obj = CourseDB(**course.dict())
    db.add(course_obj)
    db.commit()
    db.refresh(course_obj)
    db.close()
    return course_obj
