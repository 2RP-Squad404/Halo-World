# CATÁLOGO - SQL

Catálogo das funções principais encontradas nos scripts SQLX do DataForm.

## CAST
Tenta realizar a conversão de uma coluna/valor de um determinado tipo para outro:

```sql
CAST('123' AS INT64) -- converte o valor em STRING para inteiro

CAST(id_adesao_seguro AS INT64) -- converte a coluna (do tipo STRING) para o tipo inteiro.
```

Caso a coluna/valor não seja compatível ao novo tipo, a query não roda, causando um erro de compilação.

### _SAFE_CAST_
Similar ao CAST, porém, quando a operação é impossível de realizar (coluna/valor é incompatível ao novo tipo), joga NULL.

```sql
SELECT SAFE_CAST("apple" AS INT64) AS not_a_number

/*--------------*
 | not_a_number |
 +--------------+
 | NULL         |
 *--------------*/
 ```

**OBS: NÃO utilizar o SAFE_CAST nos scripts, a não ser em caso de teste. Após realização do teste, voltar ao CAST normal.**

## CURRENT_DATE / CURRENT_TIMESTAMP
Retorna o dia de hoje no tipo de dado DATE (a mesma lógca se aplica ao CURRENT_TIMESTAMP()):

```sql
SELECT CURRENT_DATE() AS the_date;

/*--------------*
 | the_date     |
 +--------------+
 | 2024-11-24   |
 *--------------*/
```

## SPLIT
Separa uma string de acordo com um delimitador específico passado como parâmetro:

```sql
SELECT SPLIT("texto-de-exemplo", "-") AS exemplo

/*-----------*
 | exemplo   |
 +-----------+
 | texto     |
 | de        |
 | exemplo   |
 *-----------*/
```

## SUM
Retorna a soma dos valores não-nulos de uma coluna ou de um agregado de valores.

```sql
SELECT SUM(x) AS sum
FROM UNNEST([1, 2, 3, 4, 5, 4, 3, 2, 1]) AS x;

/*-----*
 | sum |
 +-----+
 | 25  |
 *-----*/
 ```

## ROW_NUMBER
Numera as linhas de uma tabela para cada partição determinada. Possui os seguintes parâmetros:
- PARTITION BY
  -  Colunas que, para cada item dentro delas, terão uma numeração própria.
     -  Ex: se particiono pela coluna "nomes", a função agrupa todas as ocorrências do nome "João" e numera essas linhas. Para o nome "Maria", a numeração recomeça, ignorando a do "João".
- ORDER BY
  - Ordena a numeração por determinadas colunas. Pode ser feito de forma crescente ou decrescente.
  - **Esse parâmetro é opcional.**

```sql
WITH finishers AS
 (SELECT 'Sophia Liu' as name,
  TIMESTAMP '2016-10-18 2:51:45' as finish_time,
  'F30-34' as division
  UNION ALL SELECT 'Lisa Stelzner', TIMESTAMP '2016-10-18 2:54:11', 'F35-39'
  UNION ALL SELECT 'Nikki Leith', TIMESTAMP '2016-10-18 2:59:01', 'F30-34'
  UNION ALL SELECT 'Lauren Matthews', TIMESTAMP '2016-10-18 3:01:17', 'F35-39'
  UNION ALL SELECT 'Desiree Berry', TIMESTAMP '2016-10-18 3:05:42', 'F35-39'
  UNION ALL SELECT 'Suzy Slane', TIMESTAMP '2016-10-18 3:06:24', 'F35-39'
  UNION ALL SELECT 'Jen Edwards', TIMESTAMP '2016-10-18 3:06:36', 'F30-34'
  UNION ALL SELECT 'Meghan Lederer', TIMESTAMP '2016-10-18 2:59:01', 'F30-34')
SELECT name,
  finish_time,
  division,
  ROW_NUMBER() OVER (PARTITION BY division ORDER BY finish_time ASC) AS finish_rank
FROM finishers;

/*-----------------+------------------------+----------+-------------*
 | name            | finish_time            | division | finish_rank |
 +-----------------+------------------------+----------+-------------+
 | Sophia Liu      | 2016-10-18 09:51:45+00 | F30-34   | 1           |
 | Meghan Lederer  | 2016-10-18 09:59:01+00 | F30-34   | 2           |
 | Nikki Leith     | 2016-10-18 09:59:01+00 | F30-34   | 3           |
 | Jen Edwards     | 2016-10-18 10:06:36+00 | F30-34   | 4           |
 | Lisa Stelzner   | 2016-10-18 09:54:11+00 | F35-39   | 1           |
 | Lauren Matthews | 2016-10-18 10:01:17+00 | F35-39   | 2           |
 | Desiree Berry   | 2016-10-18 10:05:42+00 | F35-39   | 3           |
 | Suzy Slane      | 2016-10-18 10:06:24+00 | F35-39   | 4           |
 *-----------------+------------------------+----------+-------------*/
```

## FORMAT_DATE
Formata um valor do tipo DATE para um formato específico. A documentação que contém todos os tipos de formatação existentes pode ser encontrada [clicando aqui!](https://cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time)

Exemplos:

```sql
SELECT FORMAT_DATE('%x', DATE '2008-12-25') AS US_format;

/*------------*
 | US_format  |
 +------------+
 | 12/25/08   |
 *------------*/
```

```sql
SELECT FORMAT_DATE('%b-%d-%Y', DATE '2008-12-25') AS formatted;

/*-------------*
 | formatted   |
 +-------------+
 | Dec-25-2008 |
 *-------------*/
```

```sql
SELECT FORMAT_DATE('%b %Y', DATE '2008-12-25') AS formatted;

/*-------------*
 | formatted   |
 +-------------+
 | Dec 2008    |
 *-------------*/
```

## COALESCE
Retorna, dentre um agrupamento de valores (ou uma coluna), o primeiro valor não-nulo:

```sql
SELECT COALESCE('A', 'B', 'C') as result

/*--------*
 | result |
 +--------+
 | A      |
 *--------*/
```

```sql
SELECT COALESCE(NULL, 'B', 'C') as result

/*--------*
 | result |
 +--------+
 | B      |
 *--------*/
```

## SUBSTR
Extrai uma parte de uma string passada como parâmetro. Possui os seguintes parâmetros:
  - value
    - String em que se vai extrair a substring.
  - position
    - Número do caractere inicial que a substring vai começar.
  - length
    - Quantidade de caracteres que a substring vai ter.

Exemplos:

```sql
SELECT SUBSTR('apple', 2) AS example

/*---------*
 | example |
 +---------+
 | pple    |
 *---------*/
```

```sql
SELECT SUBSTR('apple', 2, 2) AS example

/*---------*
 | example |
 +---------+
 | pp      |
 *---------*/
```

## CONCAT
Concatena diversos valores em uma única string:

```sql
SELECT CONCAT('Summer', ' ', 1923) as release_date;

/*---------------------*
 | release_date        |
 +---------------------+
 | Summer 1923         |
 *---------------------*/
```

## ROUND
Utilizado para arredondar valores.

Se apenas um número decimal é passado como parâmetro, arredonda para o próximo inteiro.

Se um número inteiro for passado como parâmetro depois do número decimal, arredonda o número decimal para o número de casas decimais especificadas no número inteiro.

Exemplos de diversos casos podem ser [encontrados aqui!](https://cloud.google.com/bigquery/docs/reference/standard-sql/mathematical_functions#round)

## CASE
Funciona exatamente como um if else:

```sql
WITH Numbers AS (
  SELECT 90 as A, 2 as B UNION ALL
  SELECT 50, 6 UNION ALL
  SELECT 20, 10
)
SELECT
  A,
  B,
  CASE
    WHEN A > 60 THEN 'red'
    WHEN B = 6 THEN 'blue'
    ELSE 'green'
    END
    AS result
FROM Numbers

/*------------------*
 | A  | B  | result |
 +------------------+
 | 90 | 2  | red    |
 | 50 | 6  | blue   |
 | 20 | 10 | green  |
 *------------------*/
```

## DATE_TRUNC
Tunca (arredonda) uma data para uma granularidade especificada.

As granularidades aceitas podem ser:
  - DAY
  - WEEK
  - MONTH
  - YEAR
  - entre outros

Visualize [aqui](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#date_trunc_granularity_date) todas as opções possíveis!

```sql
SELECT DATE_TRUNC(DATE '2008-12-25', MONTH) AS month;

/*------------*
 | month      |
 +------------+
 | 2008-12-01 | -- truncou a data para o primeiro dia do mês 
 *------------*/ 
```

## TIMESTAMP_SUB
Subtrai um intervalo específico de uma data formatada no tipo TIMESTAMP.

```sql
SELECT
  TIMESTAMP("2008-12-25 15:30:00+00") AS original,
  TIMESTAMP_SUB(TIMESTAMP "2008-12-25 15:30:00+00", INTERVAL 10 MINUTE) AS earlier;

-- Mostra a data 10 minutos mais cedo
/*-------------------------+-------------------------*
 | original                | earlier                 |
 +-------------------------+-------------------------+
 | 2008-12-25 15:30:00 UTC | 2008-12-25 15:20:00 UTC |
 *-------------------------+-------------------------*/
```

## PARSE_TIMESTAMP
Converte uma string para um TIMESTAMP. Todos os tipos de conversão podem ser encontrados [clicando aqui!](https://cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time)

```sql
SELECT PARSE_TIMESTAMP("%c", "Thu Dec 25 07:30:00 2008") AS parsed;

/*-------------------------*
 | parsed                  |
 +-------------------------+
 | 2008-12-25 07:30:00 UTC |
 *-------------------------*/
```

## REGEXP_REPLACE
A função tem o seguinte escopo:

```sql
REGEXP_REPLACE(value, regexp, replacement)
```

Ela retorna uma string onde todas as substrings de `value` que combinam com a expressão regular (regex) `regexp` são substituídas por `replacement`.

```sql
SELECT REGEXP_REPLACE('# Heading', r'^# ([a-zA-Z0-9\s]+$)', '<h1>\\1</h1>') AS html

/*--------------------------*
 | html                     |
 +--------------------------+
 | <h1>Heading</h1>         | -- O regex aplicado detecta quaisquer
 |                          | -- caracteres que precedem um # e os coloca
 |                          | -- dentro de um <h1></h1>
 *--------------------------*/
```

## IFNULL
Detecta se um determinado valor é nulo. Se sim, o substitui com o segundo valor passado como parâmetro:

```sql
SELECT IFNULL(NULL, 0) as result

/*--------*
 | result |
 +--------+
 | 0      |
 *--------*/
```

## MAX
Retorna o maior valor não-nulo em um conjuto de dados / coluna:

```sql
SELECT MAX(x) AS max
FROM UNNEST([8, 37, 55, 4]) AS x;

/*-----*
 | max |
 +-----+
 | 55  |
 *-----*/
```