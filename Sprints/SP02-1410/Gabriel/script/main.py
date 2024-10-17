import json
from google.cloud import bigquery
from google.cloud.exceptions import BadRequest

def validate_table_creation(event, context):    
    ''' Valida se a tabela possui particionamento e clustering. Se não possuir, ela não é criada.
        event -> dados do job de criação de tabela
     '''

    # Converter os dados decodificados para JSON 
    table_info = json.loads(event.decode('utf-8'))
    
    # Separa o ID do da tabela do JSON
    brute_id = table_info["protoPayload"]
    brute_id = brute_id['authorizationInfo'][0]
    # O ID bruto vem no formato: projeto/id_projeto/dataset/id_dataset/tabela/id_tabela 
    brute_id = brute_id['resource'].split('/')
    table_id = f"{brute_id[1]}.{brute_id[3]}.{brute_id[5]}"

    # Conectar ao BigQuery
    client = bigquery.Client()

    # Obter informações sobre a tabela criada
    table = client.get_table(table_id)

    # Verificar se a tabela possui particionamento e clustering
    partition_field = table.time_partitioning.field if table.time_partitioning else False
    clustering_fields = table.clustering_fields if table.clustering_fields else False

    # Validação do particionamento
    if not partition_field:
        client.delete_table(table_id)
        raise ValueError(f"A tabela {table_id} foi criada sem particionamento obrigatório.")
        return
    
    # Validação do clustering
    if not clustering_fields or len(clustering_fields) == 0:
        client.delete_table(table_id)
        raise ValueError(f"A tabela {table_id} foi criada sem clustering obrigatório.")
        return

    return f"Tabela {table_id} validada com particionamento e clustering corretos."