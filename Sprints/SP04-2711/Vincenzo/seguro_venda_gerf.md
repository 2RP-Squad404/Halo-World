``` mermaid

sequenceDiagram
    %% Este diagrama representa o processo de 'seguro_venda_gerf_artigo'.
    Note over Usuário, Sistema: Esta rotina ETL gera dados de vendas de seguros incluindo informações detalhadas de artigos.

    participant Usuário as Usuário Externo
    participant Sistema as Sistema Interno
    participant BancoDados as Banco de Dados

    Usuário->>Sistema: Inicia o Processo
    activate Sistema
    Sistema->>BancoDados: Consulta Dados de Produtos e Vendas
    activate BancoDados
    BancoDados-->>Sistema: Retorna Dados Consolidados
    deactivate BancoDados
    Sistema->>Sistema: Processa e Consolida Informações
    Sistema-->>Usuário: Retorna Relatório de Vendas e Artigos
    deactivate Sistema

```