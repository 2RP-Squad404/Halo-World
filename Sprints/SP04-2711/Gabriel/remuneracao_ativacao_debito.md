```mermaid
sequenceDiagram
    participant Processo as Processo Principal
    participant BigQuery as BigQuery
    participant Parametros as Tabela parametros
    participant Vterm as Tabela v_termometro_pfin_cartao
    participant Logs as Log de Processamento

    Processo->>Logs: Busca informações de logs de execuções anteriores
    
    Logs-->>Processo: Retorna os dados de logs anteriores.

    Processo->>Parametros: Seleciona indicadores de remuneração das contas digitais.

    Processo->>Vterm: Seleciona as ativações de débito e a quantidade prevista e real dos indicadores para cada ativação entre as datas predefinidas.

    Processo->>BigQuery: Seleciona dados unificados. 

    Processo->>Logs: Atualiza processo_log com a contagem de linhas e o status de sucesso da execução.
```