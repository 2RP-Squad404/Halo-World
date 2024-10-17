
# Implementando obrigatoriedade de Particionamento e Clustering com Cloud Functions


### Como funciona:
1. Uma Cloud Function é acionada quando uma nova tabela é criada.
2. A função verifica se a tabela possui as configurações corretas de particionamento e clustering.
3. Se as configurações estiverem ausentes, a função aplica automaticamente as configurações necessárias.

---

## Exemplo de Código de Cloud Function (Python)

```python
from google.cloud import bigquery

def verificar_particionamento_clustering(event, context):
    client = bigquery.Client()
    dataset_id = event['dataset_id']
    table_id = event['table_id']

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    if not table.time_partitioning:
        # Adiciona particionamento e clustering
        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="purchase_datetime"
        )
        table.clustering_fields = ["purchase_datetime", "product_id"]
        client.update_table(table, ["time_partitioning", "clustering_fields"])
        print(f"Tabela {table_id} atualizada com particionamento e clustering.")
```

### Passos:
1. Crie uma nova **Cloud Function** no Google Cloud Console.
2. Defina o gatilho como Pub/Sub ou eventos do BigQuery (por exemplo, quando uma nova tabela for criada).
3. Use o código acima na função para verificar e aplicar particionamento e clustering.
4. Teste criando uma nova tabela no BigQuery e observe se a função aplica as configurações necessárias.

---

## Alternativa: Implementação com Container no Cloud Run

Outra abordagem é utilizar um container com uma aplicação que verifique periodicamente as tabelas no BigQuery e aplique as configurações de particionamento e clustering quando necessário.

### Passo a Passo para Implementação via Container no Cloud Run:

1. **Criar o Container:**
   - No seu projeto local, crie um diretório para o código do seu container.
   - Escreva o código Python (similar ao código da Cloud Function) que verifica as tabelas e aplica particionamento e clustering.

   Exemplo de `app.py`:

   ```python
   from google.cloud import bigquery

   def verificar_tabelas():
       client = bigquery.Client()
       dataset_id = "seu_dataset"
       tables = client.list_tables(dataset_id)

       for table in tables:
           table_ref = client.dataset(dataset_id).table(table.table_id)
           table = client.get_table(table_ref)

           if not table.time_partitioning:
               # Aplica particionamento e clustering
               table.time_partitioning = bigquery.TimePartitioning(
                   type_=bigquery.TimePartitioningType.DAY,
                   field="purchase_datetime"
               )
               table.clustering_fields = ["purchase_datetime", "product_id"]
               client.update_table(table, ["time_partitioning", "clustering_fields"])
               print(f"Tabela {table.table_id} atualizada com particionamento e clustering.")
   ```

2. **Criar o Dockerfile:**
   - No mesmo diretório, crie um arquivo `Dockerfile` para criar a imagem do container.

   Exemplo de `Dockerfile`:

   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app
   COPY . /app

   RUN pip install google-cloud-bigquery

   CMD ["python", "app.py"]
   ```

3. **Construir e Enviar a Imagem para o Container Registry:**
   - No terminal, execute os comandos abaixo para construir e enviar a imagem para o Google Container Registry:

   ```bash
   gcloud builds submit --tag gcr.io/SEU_PROJETO/verificador-particionamento-clustering
   ```

4. **Implantar no Cloud Run:**
   - Após enviar a imagem para o Container Registry, implante no Cloud Run:

   ```bash
   gcloud run deploy verificador-tabelas --image gcr.io/SEU_PROJETO/verificador-particionamento-clustering --region us-central1
   ```

5. **Configurar o Trigger Automático:**
   - Configure o Cloud Run para ser acionado periodicamente usando o Cloud Scheduler, ou defina um gatilho baseado em eventos de criação de tabelas via Pub/Sub.

---


