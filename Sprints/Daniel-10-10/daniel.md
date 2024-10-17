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

![alt text](<img/Imagem 1 Cloud Run.png>)

![alt text](<img/Imagem 2 Cloud Run.png>)

## Forma Que Chega no Email o Alerta
![alt text](<img/Alerta Gmail Cloud Run 3.png>)

## Topico Pub/Sub
![alt text](<img/Pub Sub 4.png>)