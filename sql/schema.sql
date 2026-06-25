-- ============================================================
-- Retail Sales & Customer Analytics - Database Schema
-- Dialect: PostgreSQL (compatible with most SQL engines)
-- ============================================================

-- Customers dimension table
CREATE TABLE customers (
    customer_id     INTEGER PRIMARY KEY,
    first_name      VARCHAR(50),
    last_name       VARCHAR(50),
    email           VARCHAR(120),
    country         VARCHAR(60),
    region          VARCHAR(60),
    signup_date     DATE
);

-- Products dimension table
CREATE TABLE products (
    product_id      INTEGER PRIMARY KEY,
    product_name    VARCHAR(120),
    category        VARCHAR(60),
    unit_price      NUMERIC(10, 2),
    unit_cost       NUMERIC(10, 2)
);

-- Orders fact table (one row per order)
CREATE TABLE orders (
    order_id        INTEGER PRIMARY KEY,
    customer_id     INTEGER REFERENCES customers(customer_id),
    order_date      DATE NOT NULL,
    order_status    VARCHAR(20),       -- e.g. completed, returned, cancelled
    channel         VARCHAR(20)        -- e.g. online, in-store
);

-- Order line items fact table (one row per product per order)
CREATE TABLE order_items (
    order_item_id   INTEGER PRIMARY KEY,
    order_id        INTEGER REFERENCES orders(order_id),
    product_id      INTEGER REFERENCES products(product_id),
    quantity        INTEGER NOT NULL,
    unit_price      NUMERIC(10, 2) NOT NULL,
    discount        NUMERIC(4, 2) DEFAULT 0   -- fractional discount, e.g. 0.10 = 10%
);

-- Helpful indexes for analytical queries
CREATE INDEX idx_orders_customer   ON orders(customer_id);
CREATE INDEX idx_orders_date       ON orders(order_date);
CREATE INDEX idx_items_order       ON order_items(order_id);
CREATE INDEX idx_items_product     ON order_items(product_id);
