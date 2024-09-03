CREATE OR REPLACE VIEW `sapient-cycling-434419-u0.Campaigns.v_interacoes_campanhas` AS
WITH location_ranking AS (
  SELECT 
    client_id,
    MAX(type_campaign) AS most_campaigns,
    COUNTIF(return_status = 'error') AS quantity_error,
    FORMAT_DATE('%Y-%m-%d', CURRENT_DATE()) AS date_today,
    CAST(FORMAT_DATE('%m%Y', CURRENT_DATE()) AS INT64) AS anomes_today
  FROM 
    `sapient-cycling-434419-u0.Campaigns.Campaigns`
  GROUP BY 
    client_id
)
SELECT * FROM location_ranking;
