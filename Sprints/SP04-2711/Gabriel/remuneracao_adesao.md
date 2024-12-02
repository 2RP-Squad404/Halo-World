```mermaid
sequenceDiagram
    participant Processo as Processo Principal
    participant BigQuery as BigQuery
    participant Parametros as Tabela parametros
    participant Vterm as Tabela v_termometro_pfin_seguro
    participant Logs as Log de Processamento

    Processo->>Logs: Busca informações de logs de execuções anteriores
    
    Logs-->>Processo: Retorna os dados de logs anteriores.

    Processo->>Parametros: Seleciona os parâmetros dos pertencentes ao grupo "PRODUTIVIDADE ADESAO"

    Processo->>Vterm: Seleciona dados onde o indicador da flag é "A".

    Processo->>BigQuery: Seleciona dados unificados. 

    Processo->>Logs: Atualiza processo_log com a contagem de linhas e o status de sucesso da execução.
```