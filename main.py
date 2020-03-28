from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime, date
from pydantic import BaseModel

import pandas as pd


class Patient(BaseModel):
    name: str
    age: int
    ageGroup: int
    birthday: date
    gender: str
    address: str
    contactNumber: int
    disposition: str
    isForTesting: bool
    boothNum: int
    officer: str
    timestamp: datetime
    symptoms: list = []
    comorbidities: list = []
    travel: list = []


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


@app.get("/")
async def render_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

@app.post("/store_to_excel/")
async def create_item(patient: Patient):
    try:
        df = pd.read_csv('covid_patients.csv')
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df.append(patient.dict(), ignore_index=True)
    except:
        df = pd.DataFrame.from_dict(patient.dict())
    df.to_csv("covid_patients.csv")
    return status.HTTP_201_CREATED


if __name__ == "__main__":
    app.run(debug=True)
