``` mermaid
sequenceDiagram
    participant User as User
    participant ProcessLog as get_processo_log
    participant Parcela as cobranca_parcela_acordo
    participant P0 as Parcela P0
    participant P1 as Parcela P1
    participant Pagamento as cobranca_pagamento_acordo
    participant Val as Valor Total Pagamento
    participant Prox as Proxima Parcela
    participant Quebra as Quebra Acordo
    participant AcordoBase as Acordo Base
    participant Liquidacao as cobranca_liquidacao_parc_acordo
    participant Final as Tabela Final
    participant NewTable as cobr_pagamento_parc_acordo
    participant LogProcess as insert_processo_log

    User->>ProcessLog: Call get_processo_log
    ProcessLog-->>User: Retorna parametros
    User->>Parcela: Consulta parcelas de acordo
    Parcela-->>User: Retorna parcelas
    User->>P0: Filtra parcelas com num_parcela_acordo = 0
    User->>P1: Filtra parcelas com num_parcela_acordo = 1
    User->>Pagamento: Consulta pagamentos de acordo
    Pagamento-->>User: Retorna pagamentos
    User->>Val: Calcula valor total pago e quantidade de parcelas pagas
    Val-->>User: Retorna soma e contagem
    User->>Prox: Consulta próximas parcelas
    Prox-->>User: Retorna próximas parcelas
    User->>Quebra: Consulta acordos quebrados
    Quebra-->>User: Retorna acordos quebrados
    User->>AcordoBase: Monta tabela de base de acordos
    AcordoBase-->>User: Tabela de base montada
    User->>Liquidacao: Consulta liquidação de parcelas
    Liquidacao-->>User: Retorna liquidações
    User->>Final: Monta tabela final com pagamentos, parcelas e acordos
    Final-->>User: Tabela final montada
    User->>NewTable: Cria tabela cobr_pagamento_parc_acordo
    NewTable-->>User: Tabela criada
    User->>LogProcess: Call insert_processo_log
    LogProcess-->>User: Log de processo atualizado

    Note over User, ProcessLog: Pre Operations
    Note over User, NewTable: Criação e Transformação dos Dados
    Note over User, LogProcess: Post Operations

```