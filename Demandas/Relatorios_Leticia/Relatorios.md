## Gerenciamento de memória por usuário nominal e de serviço no BigQuery. 💻📊

✅ **Teste que deu certo**:

### Reduzir o número de Bytes por consulta
- Entrar no seu projeto do BigQuery;
- Abrir uma tabela para fazer alguma consulta;
- Entrar na configuração da consulta e limitar o número de bytes cobrados. 

Com esses passos acima, assim que algum usuário executar uma consulta acima do limite elá dará um erro e não seguirá com a consulta. 

**Ex.**: 

![consulta](img/consulta.png)
![configuração](img/configuracao.png)
![bytes](img/bytes.png)
![erro](img/erro.png)


🔎 **Outra possível opção**:

### Reduzir o valor da cota
- APIS e serviços ativados ou pelo IAM;
- Filtrar pelo serviço que deseja (no caso BigQuery);
- Cotas e limites do sistema ;
- Selecionar e colocar o valor da cota que deseja.

**Ex.**: 

![cotas](img/apis_e_servicos_cotas.png)
![cotas](img/cotas.png)
![cotas](img/novo_valor_cotas.png)


📚 **Link das documentações utilizadas**:

- [Cotas e Limites](https://cloud.google.com/bigquery/quotas?hl=pt_br)

- [Restringir o número de Bytes](https://cloud.google.com/bigquery/docs/best-practices-costs?hl=pt-br#restrict-bytes-billed)

