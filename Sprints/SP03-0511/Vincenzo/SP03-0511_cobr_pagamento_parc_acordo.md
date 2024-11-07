``` mermaid
sequenceDiagram
    participant Processo as Processo Principal
    participant BigQuery as Banco de Dados BigQuery
    participant ClienteEmail as Tabela de Emails do Cliente
    participant Logs as Registro de Processamento

    Processo ->> Logs: Inicia processo de log\n(CALL get_processo_log)
    Processo ->> BigQuery: Verifica contagem de linhas da tabela\n(SELECT row_count FROM __TABLES__ WHERE table_id = 'cobr_pagamento_parc_acordo')
    Processo ->> BigQuery: Executa query de agregação de informações\n(WITH parcela, p0, p1, pagamento, val, prox, quebra, acordo_base, liq, final AS (...) SELECT * FROM final)
    BigQuery -->> Processo: Retorna resultados da query
    Processo ->> BigQuery: Atualiza contagem de linhas após processamento\n(SELECT row_count FROM __TABLES__ WHERE table_id = 'cobr_pagamento_parc_acordo')
    Processo ->> BigQuery: Obtém data mais recente de processamento\n(SELECT max(dat_processamento) FROM cobr_pagamento_parc_acordo WHERE dat_processamento >= dth_ult_data_processada AND dat_referencia BETWEEN dat_ini_movimento AND dat_fim_movimento LIMIT 1)
    Processo ->> Logs: Registra conclusão do processo\n(CALL insert_processo_log\n"EXECUÇÃO FINALIZADA COM SUCESSO")
```