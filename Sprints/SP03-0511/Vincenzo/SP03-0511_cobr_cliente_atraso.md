``` mermaid
sequenceDiagram
    participant User as User
    participant ProcessLog as get_processo_log
    participant CampoTable as cobranca_campo_customizavel
    participant Loja as Campo Loja
    participant Colchao as Campo Colchao
    participant Colmar as Campo Colmar
    participant Contrato as Campo Contrato
    participant ClienteTable as cobranca_cliente
    participant InfoCli as Info Cliente
    participant Assessoria as Campo Assessoria
    participant Cartao as Tabela Cartao
    participant Conta as Tabela Conta
    participant ContaCartao as Tabela ContaCartao
    participant NewTable as cobr_cliente_atraso
    participant LogProcess as insert_processo_log

    User->>ProcessLog: Call get_processo_log
    ProcessLog-->>User: Retorna parametros
    User->>CampoTable: Consulta campos customizáveis
    CampoTable-->>User: Retorna valores de campos
    User->>Loja: Filtro por Campo CODIGOLOJA
    User->>Colchao: Filtro por Campo COLCHAO
    User->>Colmar: Filtro por Campo COLMAR
    User->>Contrato: Filtro por Campo CONTRATO_ORIGINAL
    User->>ClienteTable: Consulta dados de clientes em atraso
    ClienteTable-->>User: Retorna dados de cliente
    User->>InfoCli: Monta tabela InfoCli
    InfoCli-->>User: Tabela InfoCli
    User->>Assessoria: Consulta nome assessoria
    Assessoria-->>User: Retorna assessoria
    User->>Cartao: Consulta Cartao
    Cartao-->>User: Retorna Cartao
    User->>Conta: Consulta Conta
    Conta-->>User: Retorna Conta
    User->>ContaCartao: Associação Conta e Cartao
    ContaCartao-->>User: Retorna relacionamento
    User->>NewTable: Cria tabela cobr_cliente_atraso
    NewTable-->>User: Tabela criada
    User->>LogProcess: Call insert_processo_log
    LogProcess-->>User: Log de processo atualizado

    Note over User, ProcessLog: Pre Operations
    Note over User, NewTable: Criação e Transformação dos Dados
    Note over User, LogProcess: Post Operations

``` 