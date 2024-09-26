from datetime import date, datetime
from faker import Faker
from models import FictionalPerson, FictionalAccount, FictionalCard
from schemas import bigquery_schema_person, bigquery_schema_account, bigquery_schema_card
import random
from google.cloud import bigquery
from google.api_core.exceptions import NotFound

project_id = 'sapient-cycling-434419-u0'
dataset_name = 'data_mock'
table_person = f"{project_id}.{dataset_name}.persons"
table_account = f"{project_id}.{dataset_name}.account"
table_card = f"{project_id}.{dataset_name}.card"
num_rows = 10

client = bigquery.Client(project=project_id)

def check_and_create_table(client, table_id, schema):
    try:
        client.get_table(table_id)  # Tenta pegar a tabela
        print(f"Tabela {table_id} já existe.")
    except NotFound:
        # Cria a tabela se ela não existir
        table = bigquery.Table(table_id, schema=schema)
        client.create_table(table)
        print(f"Tabela {table_id} criada com sucesso.")

fake = Faker(['pt_BR'])

def generate_person():
    person = FictionalPerson(
        id_pessoa=str(fake.unique.random_int(min=1, max=1002)),
        nome=fake.unique.name(),
        cpf=fake.cpf(),
        data_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=70),
        sexo=fake.random_element(elements=["M", "F"]),
        estado_civil=fake.random_element(elements=["Solteiro", "Casado", "Divorciado", "Viúvo"]),
        nacionalidade=fake.country(),
        endereco=fake.address(),
        telefone=fake.phone_number(),
        email=fake.email(),
        data_criacao_registro=fake.date_time_this_decade()
    )

    return person

persons = [generate_person() for _ in range(1000)]

fake.unique.clear()

def generate_account():
    person = random.sample(persons, 1)[0]

    account = FictionalAccount(
        id_conta=str(fake.unique.random_int(min=1, max=10000)),
        num_conta=str(fake.unique.random_number(digits=8)),
        tipo_conta=fake.random_element(elements=["Corrente", "Poupança"]),
        status_conta=fake.random_element(elements=["Ativa", "Inativa", "Bloqueada"]),
        data_abertura=fake.date_time_this_decade(),
        data_encerramento=None,
        saldo_conta=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
        id_cliente=person.id_pessoa,
        data_ultima_movimentacao=fake.date_time_this_year()
    )

    return account

accounts = [generate_account() for _ in range(2000)]

fake.unique.clear()

def generate_card():
    account = random.sample(accounts, 1)[0]

    card = FictionalCard(
        id_cartao=str(fake.unique.random_int(min=1, max=10000)),
        id_produto_cartao=None,
        num_cartao=fake.credit_card_number(),
        num_seq_via_cartao=str(fake.random_int(min=1, max=9)),
        id_conta=account.id_conta,
        num_cpf_cliente=account.id_cliente,
        cod_tip_portador=fake.random_element(elements=["Titular", "Adicional"]),
        num_bin=str(fake.unique.random_number(digits=6)),
        cod_loja_emis_cartao=None,
        id_cliente_so=account.id_cliente,
        dth_emis_cartao=fake.date_time_this_decade(),
        dth_embs_cartao=None,
        dth_valid_cartao=fake.date_this_decade(),
        dth_desbloqueio=None,
        cod_sit_cartao=str(fake.random_int(min=1, max=5)),
        des_sit_cartao=fake.random_element(elements=["Ativo", "Bloqueado", "Cancelado"]),
        dth_sit_cartao=fake.date_time_this_year(),
        cod_estagio_cartao=str(fake.random_int(min=1, max=3)),
        des_estagio_cartao=fake.random_element(elements=["Normal", "Em Análise"]),
        dth_estagio_cartao=fake.date_time_this_year(),
        flg_embs_loja=fake.random_element(elements=["Sim", "Não"]),
        flg_cartao_cancelado=fake.random_element(elements=["Sim", "Não"]),
        flg_cartao_provisorio=fake.random_element(elements=["Sim", "Não"]),
        flg_conta_cancelada=None,
        dth_ult_atu_so=fake.date_time_this_year(),
        num_seq_ult_alteracao=str(fake.unique.random_int(min=1, max=10000)),
        dth_inclusao_reg=fake.date_time_this_year(),
        pt_nomeplastico=fake.name()
    )

    return card

cards = [generate_card() for _ in range(3500)]

def serialize_dates(row):
    for key, value in row.items():
        if isinstance(value, datetime):
            row[key] = value.isoformat()  # Converte datetime para string
    return row


# Função que insere dados falsos na tabela
def insert_fake_data(table_id, num_rows):
    if table_id == table_person:
        rows_to_insert = [generate_person().model_dump() for _ in range(num_rows)]
    elif table_id == table_account:
        rows_to_insert = [generate_account().model_dump() for _ in range(num_rows)]
    elif table_id == table_card:
        rows_to_insert = [generate_card().model_dump() for _ in range(num_rows)]
    
    # Serializa os campos datetime
    rows_to_insert = [serialize_dates(row) for row in rows_to_insert]
    
    # Insere os dados no BigQuery
    errors = client.insert_rows_json(table_id, rows_to_insert)  # API request
    
    if errors == []:
        print(f"Dados inseridos com sucesso na tabela {table_id}.")
    else:
        print(f"Erros ao inserir dados: {errors}")


check_and_create_table(client, table_person, bigquery_schema_person)
check_and_create_table(client, table_account, bigquery_schema_account)
check_and_create_table(client, table_card, bigquery_schema_card)

insert_fake_data(table_person, num_rows)
insert_fake_data(table_account, num_rows)
insert_fake_data(table_card, num_rows)