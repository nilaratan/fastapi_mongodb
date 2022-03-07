from fastapi import APIRouter
from config.database import conn
from schemas.student_serialise import student_entity, students_entity
from models.student import Student
from bson import ObjectId

student = APIRouter()


@student.get("/")
def find_all():
    std = students_entity(conn.studentdb.student.find())
    return std


@student.get("/{id}")
def find_one(id: str):
    std = student_entity(conn.studentdb.student.find_one({"_id": ObjectId(id)}))
    return std

@student.post("/")
def create(student:Student):
    std = conn.studentdb.student.insert_one(dict(student))
    return {"details": "resource create successfully"}

@student.put("/{id}")
def update(id: str, student: Student):
    conn.studentdb.student.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(student)})
    return student_entity(conn.studentdb.student.find_one({"_id": ObjectId(id)}))

@student.delete("/{id}")
def delete(id: str):
    return student_entity(conn.studentdb.student.find_one_and_delete({"_id": ObjectId(id)}))
