from fastapi import FastAPI
import json
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class student(BaseModel):
    name : str
    course : str
    marks : float

def read_data():
    with open("students.json","r") as file:
        data = json.load(file)
        return data

def write_data(data):
    with open("students.json","w") as file:
        data = json.dump(data,file,indent=4)
        return data


@app.get("/")
def greet():
    return {"message" :"welcome to fastapi"}

@app.get("/student")
def student_get(student_id:str):
    data = read_data()
    return data[student_id]

@app.post("/add_student")
def add_student(student_id:str,student:student):
    data = read_data()
    pydantic_obj = student.model_dump()
    data[student_id] = pydantic_obj
    write_data(data)
    return {"message" : "student added"}


@app.delete("/del")
def delete_st(student_id:str):
    data = read_data()
    del data[student_id]
    write_data(data)
    return {"message" : "deleted"}