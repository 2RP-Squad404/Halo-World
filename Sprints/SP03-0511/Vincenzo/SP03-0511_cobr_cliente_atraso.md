``` mermaid
sequenceDiagram
    participant Usuário as Usuário
    participant Log as Registrar Log
    participant Campos as Buscar Campos
    participant Clientes as Consultar Clientes
    participant NovaTabela as Criar Nova Tabela
    participant Finalizar as Finalizar Processo

    Usuário->>Log: Consultar informações iniciais
    Log-->>Usuário: Parâmetros recebidos
    Usuário->>Campos: Buscar campos disponíveis
    Campos-->>Usuário: Campos retornados
    Usuário->>Clientes: Buscar dados de clientes
    Clientes-->>Usuário: Dados retornados
    Usuário->>NovaTabela: Criar tabela com dados processados
    NovaTabela-->>Usuário: Tabela criada
    Usuário->>Finalizar: Atualizar log e finalizar
    Finalizar-->>Usuário: Processo concluído

    Note over Usuário, Log: Etapa Inicial
    Note over Usuário, NovaTabela: Processamento de Dados
    Note over Usuário, Finalizar: Conclusão
```