CREATE OR REPLACE VIEW `sapient-cycling-434419-u0.Purchases.v_historico_clientes` AS
SELECT 
  ec.client_id,
  cc.first_purchase,
  cc.last_purchase,
  ic.most_campaign,
  ec.total_price,
  ec.conversion_rate,
  FORMAT_DATE('%Y-%m-%d', CURRENT_DATE()) AS date_today,
  CAST(FORMAT_DATE('%m%Y', CURRENT_DATE()) AS INT64) AS anomes_today

FROM
  `sapient-cycling-434419-u0.Purchases.v_engajamento_conversao` ec
JOIN
  `sapient-cycling-434419-u0.Campaigns.v_interacoes_campanhas` ic
  ON ec.client_id=ic.client_id
JOIN
  `sapient-cycling-434419-u0.Purchases.v_compras_clientes` cc
  ON ec.client_id=cc.client_id;

