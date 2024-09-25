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
Gerenciamento de pipelines: O Dataform é cado em gerenciar pipelines de dados, não em consultas individuais.


*Por que não há suporte para labels diretamente em processos no Dataform?*

Natureza declarativa: Os processos no Dataform são definidos por arquivos SQLX, que são essencialmente scripts. Atribuir labels a scripts não é uma prática comum em ferramentas de desenvolvimento de software.
Foco em pipelines: O Dataform é projetado para gerenciar pipelines de dados como um todo, não para controlar consultas individuais.

*O que é uma pipeline de dados*
Um pipeline de dados é uma sequência de etapas interconectadas que permitem a coleta, armazenamento, transformação, análise e visualização de dados. O objetivo principal é automatizar o fluxo contínuo de informações desde a sua origem até o destino final, facilitando a obtenção de insights valiosos e a tomada de decisões mais informadas.

Labels são como rótulos para consultas individuais no BigQuery, enquanto tags são como etiquetas para processos completos no Dataform.

*Exemplo*

Imagine que você tem um projeto de análise de vendas. No BigQuery, você poderia usar labels como "departamento_vendas", "ano_2023", "regiao_sul" para organizar suas consultas. No Dataform, você poderia usar tags como "processo_etl_vendas", "modelo_previsao_vendas" para categorizar seus processos.

config {
  type: "view",
  schema: `Purchases`,
  description: "View related to client's purchases info, like total money spent and most used platform.",

  tags: ["v_compras_clientes"],

  columns: {
    client_id: "Client's unique ID composed by numbers, letters and special characters",
    total_price: "Client's total money spent",
    most_purchase_location: "Platform most used by the client to purchase",
    first_purchase: "Client's first purchase date",
    last_purchase: "Client's last purchase date",
    date_today: "Today's date",
    anomes_today: "Today's date formated as MMYYYY and casted as a integer"
  }
}

WITH location_ranking AS (
    SELECT
        client_id,
        purchase_location,
        COUNT(*) AS location_count,
        ROW_NUMBER() OVER (PARTITION BY client_id ORDER BY COUNT(*) DESC) AS rn
    FROM
        `sapient-cycling-434419-u0.Purchases.Purchases`
    GROUP BY
        client_id,
        purchase_location
)
SELECT
    p.client_id,
    SUM(p.price * p.amount * (1 - p.discount_applied)) AS total_price,
    lr.purchase_location AS most_purchase_location,
    MIN(p.purchase_datetime) AS first_purchase,
    MAX(p.purchase_datetime) AS last_purchase,
    FORMAT_DATE('%Y-%m-%d', CURRENT_DATE()) AS date_today,
    CAST(FORMAT_DATE('%m%Y', CURRENT_DATE()) AS INT64) AS anomes_today
FROM
    `sapient-cycling-434419-u0.Purchases.Purchases` p
JOIN
    location_ranking lr
    ON p.client_id = lr.client_id AND lr.rn = 1
GROUP BY
    p.client_id, lr.purchase_location


*Como atribuir tags aos arquivos sqlx e executá-los*
Conforme o exemplo, você define a tag na parte config do seu arquivo sqlx


**Tutoriais**


*Como atribuir uma tag e rodar uma execeução de um arquivo sqlx através da tag*

Entrar no arquivo sqlx, e no cabeçalho na parte "configs" atribuir uma tag
(Você pode atribuir tags a vários arquivos sqlx)

![alt text](/Demandas/Relatorios_Julio/Img/image.png)

Depois de atribuir, clicar em "Iniciar Execução", depois em "Tags", depois "Várias Tags".

![alt text](/Demandas/Relatorios_Julio/Img/image-1.png)

Clicar em "Selection of Tags", Selecionar as tags que deseja executar, clicar em "Ok", Depois "Iniciar execução"
Para conferir se executou corretamente, ir na aba "Executions", ao lado de "Iniciar Execução"

![alt text](/Demandas/Relatorios_Julio/Img/image-2.png)

<br>
<br>

*Como rodar Fluxos de trabalho através das Tags*

Abrir Dataform e clicar no repositório existente

![alt text](/Demandas/Relatorios_Julio/Img/image-3.png)

Clicar em "Versões e Programação"

![alt text](/Demandas/Relatorios_Julio/Img/image-4.png)

Clicar em "Criar" para criar uma configuração de versão

![alt text](/Demandas/Relatorios_Julio/Img/image-5.png)

Definir ID de lançamento e Frequência, depois clicar em "Criar"

![alt text](/Demandas/Relatorios_Julio/Img/image-6.png)

Ainda em "Versões e Programação", Descendo a barra de rolamento, na parte de Configurações de fluxo de trabalho, clicar em "Criar"

![alt text](/Demandas/Relatorios_Julio/Img/image-7.png)

Definir: ID de configuração, Configuração de versão (a mesma criada anteriormente), Conta de serviço, Frequência e em "Selection of Tags", selecionar as Tags a serem executadas, depois disso, "Criar"

![alt text](/Demandas/Relatorios_Julio/Img/image-8.png)

<br>

![alt text](/Demandas/Relatorios_Julio/Img/image-9.png)

Para executar, procurar o fluxo de trabalho criado, ir em "ações", depois em "Executar agora"

![alt text](/Demandas/Relatorios_Julio/Img/image-10.png)

Na aba "Workflow Execution Logs", é possível ver o histórico de fluxos de trabalho

![alt text](/Demandas/Relatorios_Julio/Img/image-11.png)

*Importante*
<br>
Após Terminar de realizar os fluxos, é importante pausá-los para não gerar custos adicionais