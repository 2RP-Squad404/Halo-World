from datetime import date
from faker import Faker
from models import FictionalPerson, FictionalCard, FictionalAccount
import random
from google.cloud import bigquery

client = bigquery.Client()

project_id = 'sapient-cycling-434419-u0'
dataset_name = 'data_mock'

table_id = f"{project_id}.{dataset_name}.persons"

schema = [
    bigquery.SchemaField("person_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("email", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("gender", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("birth_date", "DATE", mode="NULLABLE"),
    bigquery.SchemaField("address", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("salary", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("cpf", "STRING", mode="REQUIRED"),
]

# Cria a tabela com o esquema definido
table = bigquery.Table(table_id, schema=schema)

table = client.create_table(table)

print(f"Tabela {table_id} criada com sucesso.")

fake = Faker(['pt_BR'])

def generate_person():
    person = FictionalPerson(
        person_id=fake.unique.random_int(min=1, max=1002, step=1),
        name=fake.unique.name(),
        email=fake.unique.email(),
        gender=fake.passport_gender(),
        birth_date=fake.date(
            end_datetime=date(day=1, month=1, year=2000)),
        address=fake.address(),
        salary=fake.random_number(digits=4),
        cpf=fake.cpf()
    )

    return person

persons = [generate_person() for _ in range(1000)]

fake.unique.clear()

def generate_account():
    person = random.sample(persons, 1)[0]

    account = FictionalAccount(
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=0, max=10),
        due_day=fake.random_int(min=1, max=30),
        person_id= 0,
        balance=fake.random_number(digits=4),
        avaliable_balance=fake.random_number(digits=3)
    )
    return account

accounts = [generate_account() for _ in range(2000)]

fake.unique.clear()

def generate_card():
    account = random.sample(accounts, 1)[0]

    card = FictionalCard(
        card_id=fake.unique.random_int(min=1, max=4002, step=1),
        card_number=fake.credit_card_number(),
        account_id= 0,
        status_id=fake.random_int(min=0, max=10),
        limit=fake.random_number(digits=3),
        expiration_date=fake.credit_card_expire()
    )

    return card

cards = [generate_card() for _ in range(3500)]

for _ in range(10):
    person = random.sample(persons, 1)[0]
    print(person.model_dump_json())

    account = random.sample(accounts, 1)[0]
    print(account.model_dump_json())

    card = random.sample(cards, 1)[0]
    print(card.model_dump_json())

