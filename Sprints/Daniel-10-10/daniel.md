## Alertamento De Queries Custo e Processamento via Cloud Functions 
### Objetivo
Este script em Node.js foi desenvolvido para automatizar o envio de notificações por e-mail com base em alertas recebidos de uma plataforma de monitoramento, como o BigQuery. A função principal, bigQueryAlertHandler, processa esses alertas e envia e-mails personalizados conforme o tipo de evento detectado.

### Funcionamento Do Script
1. Decodificação da Mensagem de Alerta
O script recebe mensagens codificadas em base64 contendo dados de alertas. Ele converte esses dados para o formato JSON, extraindo informações relevantes, como a descrição do alerta e seu tipo.
2. Configuração do Serviço de E-mail
Para enviar e-mails, o script utiliza a biblioteca nodemailer configurada para o serviço Gmail. As credenciais de autenticação (e-mail e senha) são especificadas diretamente no código para permitir o envio das mensagens.
3. Definição das Opções de E-mail
O e-mail é enviado de uma conta configurada para um destinatário específico
4. Personalização da Mensagem
O script detecta dois tipos principais de alerta: BigQueryUsageLimit: Envia um e-mail informando que o limite de uso de bytes foi excedido.
BigQuerySlowQuery: Envia um e-mail notificando que uma consulta lenta foi detectada.
5. Envio de E-mail
Após a definição da mensagem, o e-mail é enviado ao destinatário. Se houver erros no envio, eles são registrados no console; caso contrário, o sucesso do envio é confirmado com uma resposta positiva.

![alt text](<img/Cloud Run 5.png>)

![alt text](<img/Imagem 2 Cloud Run.png>)



## Forma Que Chega no Email o Alerta
![alt text](<img/Alerta Gmail Cloud Run 3.png>)

## Topico Pub/Sub
É um serviço de mensageria assíncrona que facilita a comunicação entre sistemas distribuídos. A ideia central é que um produtor de mensagens (publisher) publica eventos em tópicos, e consumidores (subscribers) se inscrevem nesses tópicos para receber esses eventos em tempo real.

No contexto de alertas no Google Cloud, o Pub/Sub pode ser usado para:

Monitoramento em Tempo Real: Pode integrar com sistemas de monitoramento (como Google Cloud Monitoring ou outras ferramentas) para gerar alertas em tempo real quando determinados eventos ou métricas são atingidos. Por exemplo, se o uso de CPU de uma máquina virtual ultrapassar um limite, um alerta pode ser publicado em um tópico Pub/Sub.

Distribuição de Alertas: Você pode configurar o Google Cloud Monitoring para enviar notificações de alertas via Pub/Sub. Isso permite distribuir esses alertas para diferentes sistemas ou canais (como funções serverless, filas de mensagens, APIs externas etc.).

Automação de Respostas: A partir do recebimento dos alertas via Pub/Sub, pode-se acionar automações, como escalar automaticamente a infraestrutura, reiniciar instâncias, ou até mesmo enviar mensagens para equipes por meio de diferentes sistemas de notificação (ex.: SMS, Slack).

Integração com Outros Serviços: O Pub/Sub pode ser integrado com outros serviços do Google Cloud, como o Cloud Functions, para processar os alertas e realizar ações específicas, como rodar scripts, registrar logs, ou modificar recursos de infraestrutura automaticamente.

![alt text](<img/Pub Sub 4.png>)