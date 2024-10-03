# Métricas de Armazenamento e Faturamento de Dados

### Criando Gráficos de Monitoramento no GCP com Stackdriver Monitoring

#### Passo 2: Acessando o Google Cloud Monitoring
1. No **Monitoring**, clique em **Dashboards** no menu lateral.
2. Se já existir um dashboard, você pode editá-lo. Caso contrário, clique em **Create Dashboard** para criar um novo.

#### Passo 3: Adicionando um Gráfico
1. Após abrir ou criar um dashboard, clique em **Add Chart**.
2. Escolha o tipo de gráfico, como o **Time Series Line Chart**.

#### Passo 4: Configurando a Métrica
1. Na seção **Metric**, selecione o **tipo de recurso** e a **métrica** que deseja monitorar. Exemplos:
   - **Bytes Faturados por Projeto**: `BigQuery > Billing Data > Billed bytes`, filtrando por **projeto**.
   - **Bytes Armazenados por Dataset**: `BigQuery > Storage > Stored bytes`, categorizando por **dataset**.
   - **Linhas Carregadas por Projeto**: `BigQuery > Loaded rows`.
2. Refine os filtros para métricas específicas, como projetos, datasets ou intervalos de tempo.

#### Passo 5: Personalizando o Gráfico
1. Na aba **Visualization**, ajuste opções como cores, legendas e intervalo de tempo (ex.: último dia, semana, mês).
2. Selecione a **agregação** correta. Por exemplo, use `Soma` para métricas como **Bytes Armazenados** ou **Bytes Faturados**.

#### Passo 6: Definindo Alertas (Opcional)
1. Para monitoramento proativo, vá até **Alerting** e crie uma **política de alerta**.
2. Defina um **limite** para a métrica (ex.: 90% de uso de armazenamento).
3. Configure notificações, como alertas por **e-mail**, **SMS** ou **Webhook**.

### Gráficos Gerados

#### Bytes Faturados por Projeto [SOMA]
Esse gráfico mostra a quantidade total de bytes faturados ao longo do tempo, organizados por projeto. Ele ajuda a acompanhar os custos de armazenamento e processamento de dados.

#### Bytes Armazenados por Dataset [SOMA]
Exibe os bytes armazenados em diferentes datasets, categorizados por áreas como "Campaigns" e "Purchases". Essa métrica facilita a identificação de quais dados ocupam mais espaço, ajudando na otimização de armazenamento.

#### Bytes Escaneados, Faturados e Carregados por Projeto [SOMA]
Este gráfico compara bytes escaneados, faturados e carregados por projeto, oferecendo uma visão clara do ciclo de vida dos dados e ajudando a identificar gargalos ou excessos.

#### Linhas Carregadas por Projeto [SOMA]
Mostra o número de linhas de dados carregadas por projeto ao longo do tempo, essencial para entender o volume de dados processados e armazenados.

#### Contagem de Tabelas por Projeto [SOMA]
Este gráfico acompanha a criação e manutenção de tabelas por projeto ao longo do tempo, permitindo uma visão clara da estrutura de dados.

#### Contagem de Trabalhos por Projeto [SOMA]
Exibe a quantidade de trabalhos em execução ao longo do tempo, separados por projeto, facilitando o monitoramento da carga de trabalho e eficiência dos processos.

#### Logs: Gravidade ERROR ou INFO
Gráfico que mostra logs com gravidade "ERROR" ou "INFO", permitindo monitorar falhas e eventos rotineiros do sistema.

#### Políticas de Alertas Configuradas
Políticas de alertas foram configuradas para monitorar eventos críticos, com notificações automáticas quando certos limites são atingidos, como uso excessivo de armazenamento ou geração de logs "ERROR", garantindo que a equipe seja informada rapidamente.

![Exemplo de Gráfico](img/Screenshot%20from%202024-09-26%2018-57-04.png)

![Gráficos de Logs](img/Screenshot%20from%202024-09-26%2018-57-22.png)

![Alertas Configurados](img/Screenshot%20from%202024-09-26%2017-34-25.png)