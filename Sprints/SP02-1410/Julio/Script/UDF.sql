-- Criar a função UDF que recebe a data inicial e final da query
CREATE OR REPLACE FUNCTION `seu_projeto.sua_dataset.valida_intervalo`(
  start_date DATE, 
  end_date DATE
)
RETURNS STRING
AS (
  CASE 
    -- se o intervalo for maior que 2 meses retorna um erro, se não, retorna "Consult válida"
    WHEN DATE_DIFF(end_date, start_date, MONTH) > 2 THEN 'ERRO: O intervalo não pode ser maior que 2 meses.'
    ELSE 'Consulta válida.'
  END
);


