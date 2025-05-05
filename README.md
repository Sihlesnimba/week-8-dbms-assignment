# Student Records Management System

## Description
This project is a student record management system that allows users to manage students and their course enrollments. It is split into two parts:

- **Question 1:** A MySQL database with SQL script
- **Question 2:** A CRUD API built using FastAPI (Python) connected to MySQL

## How to Run

1. Import the `student_records.sql` file into your MySQL database.
2. Update the MySQL connection string in `database.py`.
3. Run the API using:

```bash
uvicorn main:app --reload
```

## ERD Screenshot
![ERD](https://via.placeholder.com/500x300?text=Student+Records+ERD)
