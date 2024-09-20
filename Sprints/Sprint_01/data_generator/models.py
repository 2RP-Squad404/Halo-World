from pydantic import BaseModel
from datetime import date
from sqlalchemy import Column, Integer, String, Date, Numeric

class FictionalPerson(BaseModel):
    """
    Modelo de dados que representa um evento relacionado a uma pessoa.

    Attributes:
        name (str): Nome da pessoa.
        email (str): Email da pessoa.
        gender (str): Gênero da pessoa.
        birth_date (date): Data de nascimento da pessoa.
        address (str): Endereço da pessoa.
        salary (float): Salário da pessoa.
        cpf (str): CPF da pessoa.
    """
    person_id: int
    name: str
    email: str
    gender: str
    birth_date: date
    address: str
    salary: float
    cpf: str

class FictionalAccount(BaseModel):
    account_id: int
    status_id: int
    due_day: int
    person_id: int
    balance: float
    avaliable_balance: float

class FictionalCard(BaseModel):
    card_id: int
    card_number: float
    account_id: int 
    status_id: int
    limit: float
    expiration_date: str