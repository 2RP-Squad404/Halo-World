# Validando preços do BigQuery
A própria documentação do GCP fornece essa query, onde é possível visualizar, nas últimas consultas, métricas importantes como:

![metricas](./Gabriel/img/metricas.png)

- Data em que o job foi realizado
- Duração do job em segundos
- Tipo do job
- **Bytes cobrados pelo job**
- **Média de slots alocados**
- **Número máximo de slots em determinada etapa do projeto**

## Diferenciando modelos de cobrança

A partir da consulta anterior, é possível analisar a forma de cobrança a ser escolhida.

Utilizar o modelo sob-demanda do BQ está intrinsicamente ligado à quantidade de dados processada continuamente pelo seu projeto.

**Em projetos pequenos com pouco volume de dados envolvido no processamento o modelo sob-demanda é essencial**:

![ondemand](./Gabriel/img/ondemand2.png)

Já o modelo de capacidade de computação está intrinsicamente ligado ao uso de slots por job.

Queries de maior complexidade de processamento computacional exigem mais slots na sua execução. Quando se quer **mais capacidade de processamento** ou em casos em que **o volume de dados excede a capacidade computacional** o modelo de capacidade se mostra muito mais benéfico economicamente.

![capacity](./Gabriel/img/capacity.png)

## Rotina para comparação de preços
Para uma exemplificação de caso onde os diferentes tipos de preço se destacam em relação aos outros:

Na nossa rotina ETL padrão, que geramos 4 `views` relacionadas às tabelas `Campaigns` e `Purchases`, o DataForm cobra 40MB (10MB de cada `view`) para cada execução da rotina.

![rotina1](./Gabriel/img/rotina1.png)

Se fôssemos utilizar o modelo sob-demanda do BQ para rodar esse job a cada 5 minutos durante 30 dias ininterruptos, por exemplo, pagaríamos por `345.600` GB consumidos, resultando em uma cobrança final de **$2,16 p/ mês** + o preço de armazenamento dos dados:

![ondemandex1](./Gabriel/img/ondemandex1.png)

Se fôssemos utilizar o modelo por capacidade de computação, por outro lado:

- O job demora cerca de 1 seg para ser realizado:
  - A cobrança de slots é feita por, no mínimo, 1 min
  - Os slots são alocados de 100 em 100
  - Ou seja, para cada execução do job, o BQ cobra um minuto de 100 slots

- Preço do slot por hora: `$0,04`
  - Preço da hora de 100 slots: `$4`
  - Preço do minuto de 100 slots (o que vai ser cobrado por execução): `4 / 60 = $0,066`
  - Preço por hora executando a cada 5 min: `0,066 * 12 = $0,8`
  - Preço por dia: `0,8 * 24 = $19,2`

**Preço por mês: `19,2 * 30 = $576` + preço do storage**

![capacityex1](./Gabriel/img/capacityex1.png)

Nesse exemplo, seria muito inviável utilizar o modelo de cobrança sob capacidade de computação, por conta da baixa quantidade de dados processados por execução do job (onde o modelo sob-demanda seria muito mais benéfico).

___

Criamos posteriormente outra rotina exemplificando onde o modelo de capacidade de computação se mostraria menos custoso.

É uma rotina bem simples, que atualiza uma tabela realizando uma consulta de 36GB em uma tabela de amostras do BQ.

![rotina2](./Gabriel/img/rotina2.png)

Se a mesma situação do exemplo anterior fosse replicada (onde o job seria executado a cada 5 min durante 5 dias ininterruptos) a cobrança, no modelo **sob-demanda**, seria sobre `36 * 12 * 24 * 30` = `311.040GB`.

![ondemandex2](./Gabriel/img/ondemandex2.png)

Porém, como o job continua utilizando menos de 100 slots, a cobrança acaba sendo a mesma do exemplo anterior!

![capacityex1](./Gabriel/img/capacityex1.png)

Dessa forma, nesse caso, **comprar slots é duas vezes mais eficiente do que utilizar o modelo sob-demanda.**

## Resultados

![result](./Gabriel/img/result.png)

# **Tagueamento de processos Dataform**

Adicionando tags dentro do arquivo .sqlx:

Entrar no arquivo sqlx, e no cabeçalho na parte "configs" atribuir uma tag
(Você pode atribuir tags a vários arquivos sqlx)

![alt text](/Sprints/SP01-3009/Julio/Img/image.png)

É possível rodar as consultas de arquivos sqlx através da tag atribuida, criando um fluxo de trabalho no Dataform.

![alt text](/Sprints/SP01-3009/Julio/Img/image-12.png)

Na aba "Workflow Execution Logs", é possível ver o histórico de fluxos de trabalho do Dataform

![alt text](/Sprints/SP01-3009/Julio/Img/image-11.png)


O tagueamento de processos Dataform no GCP é uma prática útil para organizar e gerenciar pipelines de dados. Ele permite:

Rastreamento: Tags ajudam a identificar e rastrear facilmente etapas e tabelas do pipeline, facilitando a depuração e o monitoramento.
Governança de dados: Classificar processos por importância, sensibilidade ou compliance, garantindo conformidade com regulamentações.
Custo e performance: Atribuir tags de custo a processos para otimizar o uso de recursos e monitorar gastos.
Automação: Facilitar a automação de processos baseados em tags, como acionamento de alertas ou relatórios.