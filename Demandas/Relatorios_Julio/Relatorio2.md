**Tarefa: Implementar labels e tagueamentos em um processo Dataform**

*Por que é Possível Atribuir Labels a Queries no BigQuery, mas Não a Processos no Dataform*

A diferença fundamental entre atribuir labels a queries no BigQuery e processos no Dataform reside na natureza e no propósito de cada um:

Queries no BigQuery
Ad-hoc: As consultas são executadas de forma isolada e não são parte de um fluxo de trabalho definido.
Temporárias: Os resultados da consulta são geralmente utilizados para análise imediata e não são armazenados de forma persistente.
Gerenciamento de recursos: O BigQuery permite atribuir labels para fins de gerenciamento de recursos, como cobrança e controle de acesso.
Processos no Dataform
Declarativos: Os processos são definidos por arquivos SQLX que descrevem a estrutura e as transformações dos dados.
Persistentes: Os resultados dos processos são geralmente armazenados em tabelas ou views.
Gerenciamento de pipelines: O Dataform é focado em gerenciar pipelines de dados, não em consultas individuais.


Por que não há suporte para labels diretamente em processos no Dataform?

Natureza declarativa: Os processos no Dataform são definidos por arquivos SQLX, que são essencialmente scripts. Atribuir labels a scripts não é uma prática comum em ferramentas de desenvolvimento de software.
Foco em pipelines: O Dataform é projetado para gerenciar pipelines de dados como um todo, não para controlar consultas individuais. As labels são mais úteis para gerenciar recursos e controlar o acesso a consultas.

Labels são como rótulos para consultas individuais no BigQuery, enquanto tags são como etiquetas para processos completos no Dataform.
Ambas as ferramentas oferecem mecanismos para organizar e categorizar seus recursos, mas com diferentes objetivos e níveis de granularidade.


*Exemplo*

Imagine que você tem um projeto de análise de vendas. No BigQuery, você poderia usar labels como "departamento_vendas", "ano_2023", "regiao_sul" para organizar suas consultas. No Dataform, você poderia usar tags como "processo_etl_vendas", "modelo_previsao_vendas" para categorizar seus processos.