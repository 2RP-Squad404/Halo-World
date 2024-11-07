```mermaid
sequenceDiagram
    participant Processo as Processo Principal
    participant BigQuery as BigQuery
    participant ClienteEmail as ClienteEmail Table
    participant Logs as Log de Processamento

    Processo->>BigQuery: DECLARE variáveis (nom_processo, nom_tabela, etc.)
    note right of Processo: Variáveis como 'nom_processo', 'nom_tabela' e as datas de movimento ('dat_ini_movimento', 'dat_fim_movimento') são declaradas para controlar o fluxo do processo e definir os parâmetros da execução.

    Processo->>Logs: CALL `get_processo_log` com parâmetros iniciais
    note right of Logs: A função `get_processo_log` é chamada para buscar informações de logs de execuções anteriores. Essas informações ajudam a identificar a última data processada (dth_ult_data_processada) e o horário de início da execução atual (dth_inicio_execucao).

    Logs->>Processo: Retorna dados de log e define dth_ult_data_processada e dth_inicio_execucao
    note over Processo,BigQuery: Os dados retornados pelo log são utilizados para definir o ponto de início da carga incremental, prevenindo a duplicação de dados.

    Processo->>BigQuery: SET before_rows_count a partir do row_count de 'cobranca_telefone_cliente'
    note right of BigQuery: O número de linhas antes da operação é armazenado na variável 'before_rows_count' para que a diferença de novas linhas seja calculada ao final da carga.

    Processo->>ClienteTel: Executa CTEs (tel_all, tel_cel, tel_res, tel_com)
    note right of ClienteTel: Cada CTE realiza uma extração específica: 'tel_all' obtém os IDs e a data de referência dos clientes; 'tel_cel' extrai números de celulares; 'tel_res' extrai números residenciais; 'tel_com' extrai números comerciais. Tudo isso dentro do período definido pelas variáveis 'dat_ini_movimento' e 'dat_fim_movimento'.

    ClienteTel->>BigQuery: Query para telefones (celular, residencial, comercial)
    note right of BigQuery: As consultas extraem as informações de telefones (celular, residencial e comercial) da tabela de clientes, consolidando todos os dados dentro do intervalo de datas especificado.

    Processo->>BigQuery: Realiza LEFT JOIN entre tel_all, tel_cel, tel_res, tel_com
    note over Processo,BigQuery: O LEFT JOIN combina as informações de cada tipo de telefone (celular, residencial, comercial) com a tabela principal de IDs de clientes ('tel_all'). Isso garante que todos os dados estejam centralizados em um único conjunto de resultados.

    Processo->>BigQuery: SET after_rows_count da tabela 'cobranca_telefone_cliente'
    note right of BigQuery: O número de linhas após a execução é contado e armazenado em 'after_rows_count' para calcular quantas novas linhas foram adicionadas durante o processo de carga.

    Processo->>BigQuery: SET atual_ult_data_processada com o último dat_referencia processado
    note right of BigQuery: A data de referência mais recente processada é definida na variável 'atual_ult_data_processada'. Isso garante que, nas execuções futuras, o processo comece a partir dessa data.

    Processo->>Logs: CALL `insert_processo_log` (nom_processo, nom_tabela, contagem de linhas e sucesso)
    note right of Logs: O processo finaliza registrando as informações no log de processamento. Isso inclui o nome do processo, o número de linhas adicionadas e o status de sucesso "EXECUÇÃO FINALIZADA COM SUCESSO".



```