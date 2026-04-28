from fastapi import FastAPI
import json
from datetime import datetime
from pydantic import BaseModel



app = FastAPI()


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

@app.delete("/del")
def delete_st(student_id:str):
    data = read_data()
    del data[student_id]
    write_data(data)
    return {"message" : "deleted"}