``` mermaid
sequenceDiagram
    participant Usuário as Usuário
    participant Log as Registrar Log
    participant Dados as Consultar Dados
    participant Consolidar as Consolidar Informações
    participant Finalizar as Finalizar Processo

    Usuário->>Log: Obter informações iniciais
    Log-->>Usuário: Parâmetros recebidos
    Usuário->>Dados: Buscar e filtrar dados (parcelas, pagamentos e acordos)
    Dados-->>Usuário: Dados consolidados
    Usuário->>Consolidar: Montar tabela final
    Consolidar-->>Usuário: Tabela montada
    Usuário->>Finalizar: Atualizar log
    Finalizar-->>Usuário: Processo concluído

    Note over Usuário, Log: Preparação
    Note over Usuário, Consolidar: Processamento de Dados
    Note over Usuário, Finalizar: Conclusão



```