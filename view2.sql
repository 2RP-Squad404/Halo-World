CREATE OR REPLACE VIEW `sapient-cycling-434419-u0.Campaigns.v_interacoes_campanhas` AS
WITH received AS (
    SELECT 
        client_id,
        id_campaign, 
        COUNT(*) AS times_received, 
        ROW_NUMBER() OVER (PARTITION BY client_id ORDER BY COUNT(*) DESC) AS most_received 
    FROM 
        `sapient-cycling-434419-u0.Campaigns.Campaigns` 
    WHERE 
        return_status = "received" 
    GROUP BY 
        client_id, 
        id_campaign
),

error_quantities AS (
    SELECT 
        client_id, 
        COUNT(*) AS quantity_error 
    FROM 
        `sapient-cycling-434419-u0.Campaigns.Campaigns` 
    WHERE 
        return_status = "error" 
    GROUP BY 
        client_id
)

SELECT
    r.client_id AS client_id,
    r.id_campaign AS most_campaign,
    e.quantity_error AS quantity_error,
    CURRENT_DATE() AS date_today,
    CAST(FORMAT_DATE('%m%Y', CURRENT_DATE()) AS INT64) AS anomes_today
FROM
    received r
JOIN
    error_quantities e
ON
    r.client_id = e.client_id AND
    r.most_received = 1
GROUP BY
    r.client_id,
    r.id_campaign,
    e.quantity_error
ORDER BY
    r.client_id;

SELECT * FROM `sapient-cycling-434419-u0.Campaigns.v_interacoes_campanhas` LIMIT 10