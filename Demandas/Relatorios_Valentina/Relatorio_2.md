## Particionamento : 
Divide a tabela em partes com base em alguma coluna, para ser mais preciso a analise 
## Clustering: 
Organiza os dados em cada partição, juntando linhas com valores semelhantes 

Juntar as duas coisas melhora na performasse da consulta, reduzindo quantidade de dados, contudo, menos dados são lidos abaixado o custo, e também tem permite que você gerencie e expire dados  

~~~~
CREATE TABLE 'Purchase_teste'(

purchase_id INT, 

product_name VARCHAR(255),

product_id INT, 

amount DECIMAL(10,2),

price DECIMAL(10,2),

discount_applied BOOLEAN,

payment_method VARCHAR(50),

purchase_datetime TIMESTAMP,

purchase_location VARCHAR(100),

client_id INT )
PARTITION BY DATE(purchase_datetime)
CLUSTER BY purchase_datetime
AS 
SELECT * FROM 'Purchase_teste'
~~~~



__PARTITION BY DATE (purchase_datetime)__ Otimiza consultas que filtram por data

__CLUSTER BY purchase_datetime__ : Os dados de cada partição serão agrupados por 'purchase_datetime'. Bom para consultas, pois as colunas data e hora estarão fisicamente perto. 


__IMPORTANTE:__ 
* Na maioria das vezes a coluna do CLUSTER deve ser a mesma do PARTICIONAMENTO, principalmente quando se vai fazer varias consultas filtradas pela consulta escolhida.
* __CLUSTER__ e __PARTICIONAMENTO__ pode afetar quando for adicionar dados em alguma tabela ou banco de dados hospedado em nuvem. Para melhor performance das inserções e possível a consideração de  utilizar tabelas staging (tabela para cada objeto de migração em um projeto, local temporário ) 

