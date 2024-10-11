**Limite de retrocesso de tempo de particionamento por consulta**

Uma das maneiras de limitar o usuário de realizar determinadas queries é criando uma função UDF (User Defined Function) no BigQuery, vou mostrar como fiz:

*1º passo: Encontrar a tabela particionada no BigQuery e criar uma consulta em nova guia*

![alt text](/Sprints/SP02-1410/Julio/Img/limite_query01.png)

*2º passo: Executar o seguinte script para criar uma função de validação*

[Execute este script](/Sprints/SP02-1410/Julio/Script/UDF.sql)

Será criado uma função, dentro de Rotinas que não permite ao usuário executar uma query que englobe um período maior que 2 meses

---------------------------------------------------------------------------------------------------

*Testando na prática*

![alt text](/Sprints/SP02-1410/Julio/Img/printErroQuery.png)

Nesse caso retorna erro pois o intervalo de tempo é maior que 2 meses

![alt text](/Sprints/SP02-1410/Julio/Img/PrintCertoQuery.png)

Nesse caso a consulta é realizada com sucesso pois o intervalo é menor ou igual a 2 meses

---------------------------------------------------------------------------------------------------

**Comparação de bytes processados e faturados entre uma tabela e uma view particionada com o limite**

*Na tabela:*

![alt text](/Sprints/SP02-1410/Julio/Img/BytesTabela.png)

---------------------------------------------------------------------------------------------------

*Na view:*

![alt text](/Sprints/SP02-1410/Julio/Img/BytesView.png)
