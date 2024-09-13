CREATE OR REPLACE VIEW `sapient-cycling-434419-u0.Purchases.v_engajamento_conversao` AS

WITH engagement_data AS (
    SELECT
        vi.client_id, -- Seleciona o ID do cliente
        COUNTIF(vi.return_status IN ('open', 'click')) AS total_engagements, -- Conta as campanhas com status 'open' ou 'click'
        FORMAT_DATE('%Y-%m-%d', CURRENT_DATE()) AS date_today, -- Obtém a data atual formatada como 'YYYY-MM-DD'
        CAST(FORMAT_DATE('%m%Y', CURRENT_DATE()) AS INT64) AS anomes_today -- Obtém a data atual no formato 'MMYYYY' como um número inteiro
    FROM
        `sapient-cycling-434419-u0.Campaigns.Campaigns` vi -- Tabela de campanhas
    GROUP BY
        vi.client_id -- Agrupa os resultados por ID do cliente
)

SELECT
    vc.client_id, -- Seleciona o ID do cliente da view `v_compras_clientes`
    ed.total_engagements, -- Seleciona o total de engajamentos calculado no CTE `engagement_data`
    COALESCE(CAST(COUNT(vc.client_id) AS FLOAT64) / NULLIF(ed.total_engagements, 0), 0) AS conversion_rate, -- Calcula a taxa de conversão, evitando divisão por zero
    CONCAT('R$', FORMAT("%.2f", ROUND(vc.total_price, 2))) AS total_price, -- Arredonda o total gasto para 2 casas decimais e adiciona o símbolo "R$"
    vc.most_purchase_location, -- Seleciona o local mais utilizado para compras
    ed.date_today, -- Seleciona a data atual
    ed.anomes_today -- Seleciona a data atual no formato `MMYYYY`
FROM
    `sapient-cycling-434419-u0.Purchases.v_compras_clientes` vc -- Tabela de compras agregadas por cliente
LEFT JOIN
    engagement_data ed -- Junta os dados de engajamento dos clientes com as campanhas
    ON vc.client_id = ed.client_id -- Junta com base no ID do cliente
GROUP BY
    vc.client_id, vc.total_price, vc.most_purchase_location, ed.total_engagements, ed.date_today, ed.anomes_today;
    -- Agrupa os resultados por cliente, total gasto, local mais utilizado, total de engajamentos e datas
