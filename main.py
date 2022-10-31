from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import pandas as pd

class Member(BaseModel):
    name: str
    age: int
    birthdate: date

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HIHIHI"}

@app.post("/newMember/")
async def new_member(member: Member, role) -> bool:
    print(f"New member is {member.age} years old.")
    df = pd.DataFrame(member)
    df.to_csv(member.name)
    if member.age > 30:
        print(f"You're fired {member.name}")
    return True if member.age <=30 else False

@app.get("/member/{name}")
async def get_member(name: str) -> Member:
    df = pd.read_csv(name)
    return df
