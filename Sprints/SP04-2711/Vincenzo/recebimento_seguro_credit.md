``` mermaid 

sequenceDiagram
    %% Este diagrama representa o processo de 'recebimento_seguro_credit'.
    Note over Usuário, Sistema: Esta rotina ETL consolida dados de recebimento de seguros de crédito de diferentes fontes.

    participant Usuário as Usuário Externo
    participant Sistema as Sistema Interno
    participant BancoDados as Banco de Dados

    Usuário->>Sistema: Inicia o Processo
    activate Sistema
    Sistema->>BancoDados: Consulta Dados
    activate BancoDados
    BancoDados-->>Sistema: Retorna Dados
    deactivate BancoDados
    Sistema->>Sistema: Processa Dados
    Sistema-->>Usuário: Envia Resultado Consolidado
    deactivate Sistema

```