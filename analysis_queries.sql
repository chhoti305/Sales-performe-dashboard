-- SQLite syntax. Each block starts with "-- name: <output_file_name>".

-- name: 01_kpis
SELECT COUNT(DISTINCT order_id)            AS total_orders,
       COUNT(DISTINCT customer_id)         AS total_customers,
       ROUND(SUM(sales), 2)                AS total_revenue,
       ROUND(SUM(profit), 2)               AS total_profit,
       ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM orders;

-- name: 02_monthly_revenue_trend
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(sales), 2)  AS revenue,
       ROUND(SUM(profit), 2) AS profit
FROM orders
GROUP BY month
ORDER BY month;

-- name: 03_top_10_products_by_profit
SELECT product_name, category,
       ROUND(SUM(sales), 2)  AS revenue,
       ROUND(SUM(profit), 2) AS profit
FROM orders
GROUP BY product_name, category
ORDER BY profit DESC
LIMIT 10;

-- name: 04_bottom_10_loss_making_products
SELECT product_name, category,
       ROUND(SUM(sales), 2)  AS revenue,
       ROUND(SUM(profit), 2) AS profit
FROM orders
GROUP BY product_name, category
ORDER BY profit ASC
LIMIT 10;

-- name: 05_region_performance
SELECT region,
       ROUND(SUM(sales), 2)  AS revenue,
       ROUND(SUM(profit), 2) AS profit,
       ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS margin_pct
FROM orders
GROUP BY region
ORDER BY profit DESC;

-- name: 06_category_subcategory_margin
SELECT category, sub_category,
       ROUND(SUM(sales), 2)  AS revenue,
       ROUND(SUM(profit), 2) AS profit,
       ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS margin_pct
FROM orders
GROUP BY category, sub_category
ORDER BY margin_pct ASC;

-- name: 07_discount_vs_profit
SELECT CASE
         WHEN discount = 0    THEN '0%'
         WHEN discount <= 0.2 THEN '1-20%'
         WHEN discount <= 0.3 THEN '21-30%'
         ELSE '30%+'
       END AS discount_band,
       COUNT(*)              AS order_lines,
       ROUND(SUM(sales), 2)  AS revenue,
       ROUND(SUM(profit), 2) AS profit,
       ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS margin_pct
FROM orders
GROUP BY discount_band
ORDER BY MIN(discount);

-- name: 08_new_vs_repeat_customers
WITH per_customer AS (
  SELECT customer_id, COUNT(DISTINCT order_id) AS orders, SUM(sales) AS revenue
  FROM orders
  GROUP BY customer_id
)
SELECT CASE WHEN orders = 1 THEN 'One-time' ELSE 'Repeat' END AS customer_type,
       COUNT(*)                AS customers,
       ROUND(SUM(revenue), 2)  AS revenue,
       ROUND(AVG(revenue), 2)  AS avg_revenue_per_customer
FROM per_customer
GROUP BY customer_type;
