CREATE OR REPLACE VIEW `sapient-cycling-434419-u0.Purchases.v_compras_clientes` AS
WITH location_ranking AS (
    SELECT
        client_id,
        purchase_location,
        COUNT(*) AS location_count,
        ROW_NUMBER() OVER (PARTITION BY client_id ORDER BY COUNT(*) DESC) AS rn
    FROM
        `sapient-cycling-434419-u0.Purchases.Purchases`
    GROUP BY
        client_id,
        purchase_location
)
SELECT
    p.client_id,
    SUM(p.price * p.amount * (1 - p.discount_applied)) AS total_price,
    lr.purchase_location AS most_purchase_location,
    MIN(p.purchase_datetime) AS first_purchase,
    MAX(p.purchase_datetime) AS last_purchase,
    FORMAT_DATE('%Y-%m-%d', CURRENT_DATE()) AS date_today,
    CAST(FORMAT_DATE('%m%Y', CURRENT_DATE()) AS INT64) AS anomes_today
FROM
    `sapient-cycling-434419-u0.Purchases.Purchases` p
JOIN
    location_ranking lr
    ON p.client_id = lr.client_id AND lr.rn = 1
GROUP BY
    p.client_id, lr.purchase_location;


SELECT * FROM `sapient-cycling-434419-u0.Purchases.v_compras_clientes` LIMIT 10
