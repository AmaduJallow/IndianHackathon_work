from pydantic import BaseModel


class Model(BaseModel):
    pregnancies: int
    glucose: float
    diastolic: float
    triceps: float
    insulin: float
    bmi: float
    dpf: float
    age: int
