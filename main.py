from fastapi import FastAPI
from pydantic import BaseModel  # модуль для объявления структуры данных

app = FastAPI()


class ModelCalc(BaseModel):
    a: float
    b: float


# http://127.0.0.1:8000/
@app.post('/sum')
def sum(item: ModelCalc):
    return {'result': item.a + item.b}


@app.post('/subtract')
def subtract(item: ModelCalc):
    return {'result': item.a - item.b}


@app.post('/multiply')
def multiply(item: ModelCalc):
    return {'result': item.a * item.b}


@app.post('/divide')
def divide(item: ModelCalc):
    return {'result': item.a / item.b}