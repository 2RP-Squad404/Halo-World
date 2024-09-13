*** Queries e Jobs ***

Queries e jobs são termos comumente utilizados em diversos contextos, mas que possuem significados específicos dependendo do campo de aplicação. Em geral, ambos envolvem a solicitação de informações ou a execução de tarefas, mas com nuances distintas.

**Queries**

Definição: Uma query (consulta, em português) é uma pergunta ou solicitação de informações específicas a um sistema.
Objetivo: O objetivo principal de uma query é obter dados que correspondam a um critério ou condição predefinida.
Natureza: São geralmente mais simples e diretas, buscando respostas imediatas.
Exemplos:
Banco de dados: Uma query SQL (Structured Query Language) para buscar todos os clientes com idade superior a 30 anos.
Busca na web: Uma query em um motor de busca para encontrar páginas sobre um determinado tópico.
Análise de dados: Uma query em um software de BI (Business Intelligence) para visualizar as vendas de um produto em um determinado período.


**Jobs**

Definição: Um job é uma tarefa ou processo que pode envolver uma série de passos ou operações.
Objetivo: O objetivo de um job é realizar uma tarefa completa, que pode incluir várias queries ou outras ações.
Natureza: São geralmente mais complexos e podem levar mais tempo para serem concluídos.
Exemplos:
Programação: Um job em um sistema de processamento de dados para importar dados de um arquivo, processá-los e gerar um relatório.
Sistemas operacionais: Um job de impressão para enviar um documento para uma impressora.
Cloud computing: Um job em uma plataforma de computação em nuvem para treinar um modelo de machine learning.


*** Labels e Tags ***

Qual a principal diferença entre labels e tags no contexto do BigQuery?

Labels: São mais flexíveis e podem ser definidas de forma personalizada para cada recurso. Você pode criar pares chave-valor arbitrários para organizar suas tabelas de acordo com suas necessidades específicas. Por exemplo, você pode usar labels para identificar tabelas de desenvolvimento, produção, por equipe ou por projeto.
Tags: São gerenciadas centralmente pelo Resource Manager e oferecem uma forma mais padronizada de organizar recursos. As tags são definidas em um nível global e podem ser aplicadas a qualquer recurso. Elas são ideais para implementar políticas de organização e conformidade em toda a sua infraestrutura GCP.
Em resumo:

Tanto labels quanto tags podem ser usadas no BigQuery.
Labels: Oferecem maior flexibilidade e personalização.
Tags: Oferecem uma forma mais padronizada e centralizada de organizar recursos.
Quando usar cada uma?

Labels: Use labels quando precisar de uma organização mais personalizada e específica para suas tabelas.
Tags: Use tags quando precisar de uma organização mais padronizada e alinhada com as políticas da sua empresa.
Exemplo prático:

Imagine que você tem um projeto no BigQuery com diversas tabelas relacionadas a um e-commerce. Você pode utilizar:

Labels: Para identificar tabelas de diferentes equipes (team: data_engineering, team: marketing), ou para diferenciar tabelas de desenvolvimento e produção (environment: development, environment: production).
Tags: Para marcar tabelas que contêm dados pessoais e garantir a conformidade com a GDPR (compliance: gdpr), ou para alocar custos a diferentes departamentos (cost_center: marketing).
Em conclusão:

A escolha entre labels e tags dependerá das suas necessidades específicas e da forma como você deseja organizar seus dados no BigQuery. Ambas as ferramentas são valiosas e podem ser utilizadas em conjunto para obter uma organização mais completa e eficiente.

Exemplos:

Ambiente: environment: development, production
Equipe: team: data_engineering, marketing
Project: project_id:my-project
Região: region: us-central1

**Para adicionar um label a um job**
comando bq query com a sinalização --label. Para adicionar vários rótulos, repita a sinalização. A sinalização --nouse_legacy_sql indica que sua consulta está na sintaxe do GoogleSQL.

- bq query --label KEY:VALUE --nouse_legacy_sql 'QUERY'

Exemplo:
    bq query \
    --label department:shipping \
    --nouse_legacy_sql \
    'SELECT
       column1, column2
     FROM
       `mydataset.mytable`'




from google.cloud import bigquery

client = bigquery.Client()

query_job = client.query(
    """
    SELECT client_id, channel
    FROM `sapient-cycling-434419-u0.Campaigns.Campaigns`
    WHERE channel = "sms"
    ORDER BY client_id
    LIMIT 5
    """,
    labels={'channel': 'sms'}
)

results = query_job.result()
for row in results:
    print(f"client_id: {row['client_id']}, channel: {row['channel']}")



bq query --label sms:channel --nouse_legacy_sql '
SELECT client_id, channel
FROM `sapient-cycling-434419-u0.Campaigns.Campaigns`
WHERE channel = "sms"
ORDER BY client_id
LIMIT 5
'


Exemplo Prático no BigQuery:
Imagine que você tem um projeto no BigQuery com diversas tabelas relacionadas a um e-commerce. Você pode utilizar:

Labels: environment:production, team:data_engineering, dataset:sales.
Tags: cost_center:marketing, compliance:gdpr.
Dessa forma, você pode facilmente:

Identificar tabelas de produção e desenvolvimento.
Filtrar tabelas criadas pela equipe de engenharia de dados.
Alocar custos de tabelas relacionadas a marketing.
Garantir a conformidade com a GDPR para tabelas que contêm dados pessoais.
Em resumo:

As possibilidades de uso de labels e tags são vastas e dependem das necessidades específicas de cada organização. Ao utilizar esses mecanismos de forma estratégica, você pode:

Melhorar a organização: Facilitar a localização e o gerenciamento de recursos.
Otimizar custos: Identificar e otimizar o uso de recursos.
Garantir a conformidade: Cumprir com políticas de segurança e regulamentações.
Automatizar tarefas: Simplificar a gestão de recursos.