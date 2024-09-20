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

"""
[{
  "id_cartao": "45595555",
  "id_produto_cartao": null,
  "num_cartao": "6505XXXXXXXX9955",
  "num_seq_via_cartao": "1",
  "id_conta": "26511437",
  "num_cpf_cliente": "45678912345",
  "cod_tip_portador": "1",
  "num_bin": "650567",
  "cod_loja_emis_cartao": null,
  "id_cliente_so": "12349531",
  "dth_emis_cartao": "2024-08-11 07:36:38.000000 UTC",
  "dth_embs_cartao": "2024-08-12 05:00:00.000000 UTC",
  "dth_valid_cartao": "2032-08-31 00:00:00.000000 UTC",
  "dth_desbloqueio": null,
  "cod_sit_cartao": "2",
  "des_sit_cartao": "BLOQUEADO",
  "dth_sit_cartao": "2024-08-11 07:37:00.000000 UTC",
  "cod_estagio_cartao": "4",
  "des_estagio_cartao": "ENCAMINHADO",
  "dth_estagio_cartao": "2024-08-12 05:00:00.000000 UTC",
  "flg_embs_loja": "N",
  "flg_cartao_cancelado": "N",
  "flg_cartao_provisorio": "N",
  "flg_conta_cancelada": null,
  "dth_ult_atu_so": "2024-08-12 05:00:20.000000 UTC",
  "num_seq_ult_alteracao": "62",
  "dth_inclusao_reg": "2024-08-15 04:18:47.000000 UTC",
  "pt_nomeplastico": "SAMUEL NUNES",
  "ca_arquivolote": "CPEM120824",
  "ca_id_imagem": null,
  "bc_responsavel": "[IRIS]_1056",
  "ca_codigocancelamento": null,
  "ca_flaggeracartasenha": "0",
  "pt_id_imagem": null
}]
"""

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

