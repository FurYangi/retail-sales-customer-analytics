-- ============================================================
-- Retail Sales & Customer Analytics - Analytical Queries
-- Dialect: PostgreSQL
-- These queries answer the core business questions of the project.
-- ============================================================

-- ------------------------------------------------------------
-- 1. Total revenue, orders, and average order value (KPIs)
-- ------------------------------------------------------------
SELECT
    COUNT(DISTINCT o.order_id)                              AS total_orders,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount))
        / COUNT(DISTINCT o.order_id), 2)                    AS avg_order_value
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'completed';

-- ------------------------------------------------------------
-- 2. Monthly revenue trend with month-over-month growth
-- ------------------------------------------------------------
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS order_month,
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'completed'
    GROUP BY 1
)
SELECT
    order_month,
    ROUND(revenue, 2) AS revenue,
    ROUND(
        100.0 * (revenue - LAG(revenue) OVER (ORDER BY order_month))
        / NULLIF(LAG(revenue) OVER (ORDER BY order_month), 0), 1
    ) AS mom_growth_pct
FROM monthly
ORDER BY order_month;

-- ------------------------------------------------------------
-- 3. Top 10 products by revenue
-- ------------------------------------------------------------
SELECT
    p.product_name,
    p.category,
    SUM(oi.quantity)                                       AS units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o   ON oi.order_id = o.order_id
WHERE o.order_status = 'completed'
GROUP BY p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;

-- ------------------------------------------------------------
-- 4. Revenue by category and region (pivot-style breakdown)
-- ------------------------------------------------------------
SELECT
    p.category,
    c.region,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM order_items oi
JOIN products p  ON oi.product_id = p.product_id
JOIN orders o    ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'completed'
GROUP BY p.category, c.region
ORDER BY revenue DESC;

-- ------------------------------------------------------------
-- 5. Customer Lifetime Value: top 20 customers by total spend
-- ------------------------------------------------------------
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    COUNT(DISTINCT o.order_id)         AS orders,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS lifetime_value
FROM customers c
JOIN orders o      ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'completed'
GROUP BY c.customer_id, customer_name
ORDER BY lifetime_value DESC
LIMIT 20;

-- ------------------------------------------------------------
-- 6. RFM segmentation (Recency, Frequency, Monetary)
--    Scores customers 1-4 on each dimension using quartiles.
-- ------------------------------------------------------------
WITH customer_rfm AS (
    SELECT
        c.customer_id,
        CURRENT_DATE - MAX(o.order_date)                   AS recency_days,
        COUNT(DISTINCT o.order_id)                         AS frequency,
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS monetary
    FROM customers c
    JOIN orders o      ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'completed'
    GROUP BY c.customer_id
),
scored AS (
    SELECT
        customer_id,
        recency_days,
        frequency,
        ROUND(monetary, 2) AS monetary,
        NTILE(4) OVER (ORDER BY recency_days DESC) AS r_score,  -- lower recency = better
        NTILE(4) OVER (ORDER BY frequency)         AS f_score,
        NTILE(4) OVER (ORDER BY monetary)          AS m_score
    FROM customer_rfm
)
SELECT
    customer_id,
    recency_days,
    frequency,
    monetary,
    r_score, f_score, m_score,
    CASE
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champions'
        WHEN f_score >= 3 AND m_score >= 3                  THEN 'Loyal'
        WHEN r_score >= 3                                   THEN 'Recent / Promising'
        WHEN r_score = 1 AND f_score >= 3                   THEN 'At Risk'
        WHEN r_score = 1                                    THEN 'Lost'
        ELSE 'Needs Attention'
    END AS segment
FROM scored
ORDER BY monetary DESC;
