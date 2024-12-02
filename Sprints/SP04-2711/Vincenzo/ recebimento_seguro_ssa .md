``` mermaid
sequenceDiagram
    %% Este diagrama representa o processo de 'recebimento_seguro_ssa'.
    Note over Usuário, Sistema: Este script gerencia o recebimento seguro de dados de seguros do sistema SSA.

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
    Sistema-->>Usuário: Envia Resultado
    deactivate Sistema

```