from fastapi import FastAPI
import json
from datetime import datetime
from pydantic import BaseModel
import os


app = FastAPI()


def read_data():
    with open("students.json","r") as file:
        data = json.load(file)
        return data

def write_data(data):
    with open("students.json","r") as file:
        data = json.dump(data,file,indent=4)
        return data


@app.get("/")
def greet():
    return {"message" :"welcome to fastapi"}

@app.get("/student")
def student_get(student_id:str):
    data = read_data()
    return data[student_id]

# @app.post("/student_post")
# def student_post(student_id:str,id:str,name:str):
#     data = read_data()



    