const nodemailer = require('nodemailer');

exports.bigQueryAlertHandler = (message, context) => {
    // Configuração do serviço de e-mail (Gmail, por exemplo)
    let transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'vincenzo.amendola142004@gmail.com',
            pass: 'pcpq uhce bgan bjuy'  // Certifique-se de usar uma senha de aplicativo do Gmail
        }
    });

    // Decodificando os dados da mensagem
    let alertData;
    try {
        alertData = JSON.parse(Buffer.from(message.data, 'base64').toString());
    } catch (error) {
        console.error('Erro ao decodificar a mensagem:', error);
        return;
    }

    // Verifica se o JSON possui as informações necessárias
    if (alertData && alertData.protoPayload && alertData.protoPayload.serviceData && alertData.protoPayload.serviceData.jobCompletedEvent) {
        const jobStats = alertData.protoPayload.serviceData.jobCompletedEvent.job.jobStatistics;
        const totalProcessedBytes = parseInt(jobStats.totalProcessedBytes, 10);
        const limitBytes = 1048576; // 1 MB como limite de teste

        // Verifica se a query excede o limite de bytes
        if (totalProcessedBytes > limitBytes) {
            console.log(`Alerta: Query excedeu o limite de bytes (${totalProcessedBytes} bytes)`);

            // Definindo as opções de e-mail com base nos dados recebidos
            let mailOptions = {
                from: 'vincenzo.amendola142004@gmail.com',
                to: alertData.protoPayload.authenticationInfo.principalEmail, // Utiliza o campo principalEmail do payload
                subject: 'Alerta do BigQuery: Limite de Bytes Excedido',
                text: `A query executada excedeu o limite de bytes permitido. Total processado: ${totalProcessedBytes} bytes.`
            };

            // Enviar o e-mail
            transporter.sendMail(mailOptions, (error, info) => {
                if (error) {
                    return console.log(`Erro ao enviar email: ${error}`);
                }
                console.log(`Email enviado: ${info.response}`);
            });
        } else {
            console.log('Query dentro do limite de bytes permitido.');
        }
    } else {
        console.error('JSON inválido ou incompleto. Não foi possível obter informações da query.');
    }
};