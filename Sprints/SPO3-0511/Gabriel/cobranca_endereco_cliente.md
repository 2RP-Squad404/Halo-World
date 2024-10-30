```mermaid
sequenceDiagram
    participant Processo as Processo Principal
    participant BigQuery as BigQuery
    participant ClienteEndereco as ClienteEndereco Table
    participant Logs as Log de Processamento

    Processo->>BigQuery: DECLARE variáveis (nom_processo, nom_tabela, etc.)
    Processo->>Logs: CALL `get_processo_log` com parâmetros iniciais
    Logs->>Processo: Retorna dados de log e define dth_ult_data_processada e dth_inicio_execucao

    Processo->>BigQuery: SET before_rows_count a partir do row_count de 'cobranca_endereco_cliente'

    Processo->>ClienteEndereco: Executa a CTE ClienteEndereco para selecionar endereços principais de clientes
    ClienteEndereco->>BigQuery: Query de cliente e endereço entre dat_ini_movimento e dat_fim_movimento

    Processo->>BigQuery: Seleciona dados de cliente e endereço onde rn = 1

    Processo->>BigQuery: SET after_rows_count a partir do row_count atualizado de 'cobranca_endereco_cliente'
    Processo->>BigQuery: SET atual_ult_data_processada com o último dat_referencia processado

    Processo->>Logs: CALL `insert_processo_log` com detalhes de execução, contagem de linhas e mensagem de sucesso
```