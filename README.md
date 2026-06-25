# Retail Sales & Customer Analytics

End-to-end data analytics project analyzing retail sales and customer behavior using **SQL**, **Python (Pandas)**, and **interactive dashboards** to turn raw transactional data into actionable business insights.


End-to-end data analytics project analyzing retail sales and customer behavior using **SQL**, **Python (Pandas)**, and **interactive dashboards** to turn raw transactional data into actionable business insights.

---

## Project Overview

Retail businesses generate huge volumes of transactional data, but value comes from translating that data into decisions. This project simulates the workflow of a data analyst at a retail company: cleaning raw sales data, exploring trends, segmenting customers, and surfacing insights that support revenue growth and retention.

**Business questions addressed:**
- Which products, categories, and regions drive the most revenue?
- How do sales trend over time (seasonality, growth, month-over-month)?
- Who are the most valuable customers, and how can they be segmented?
- Where are the opportunities to increase average order value and retention?

---

## Tech Stack

| Area | Tools |
|------|-------|
| Data extraction & querying | SQL (PostgreSQL / SQLite) |
| Data cleaning & analysis | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboards | Power BI / Tableau |
| Environment | Jupyter Notebook |
| Version control | Git & GitHub |

---

## Repository Structure

```
retail-sales-customer-analytics/
|-- data/
|   |-- README.md            # Dataset source & setup instructions
|   |-- raw/                 # Original source data (not committed)
|   |-- processed/           # Cleaned, analysis-ready data
|-- notebooks/
|   |-- 01_data_cleaning_eda.py        # Cleaning + exploratory analysis
|   |-- 02_customer_segmentation.py    # RFM customer segmentation
|-- sql/
|   |-- schema.sql           # Table definitions
|   |-- analysis_queries.sql # Business analysis queries
|-- reports/                 # Generated charts & summary findings
|-- requirements.txt         # Python dependencies
|-- README.md
```

---

## Methodology

**1. Data Cleaning & Preparation** ( `notebooks/01_data_cleaning_eda.py` )
Handled missing values, removed cancelled orders and duplicates, standardized column names and date formats, and engineered features such as revenue, order month, and day-of-week.

**2. Exploratory Data Analysis (EDA)**
Analyzed sales trends across time, products, categories, and regions. Identified seasonality patterns and top/bottom performers, with charts saved to `reports/`.

**3. Customer Segmentation** ( `notebooks/02_customer_segmentation.py` )
Applied RFM analysis (Recency, Frequency, Monetary) using quartile scoring to group customers into actionable segments such as Champions, Loyal, At-Risk, and Lost.

**4. SQL Analysis** ( `sql/analysis_queries.sql` )
Wrote analytical SQL (joins, aggregations, CTEs, and window functions) for KPIs, monthly growth, top products, and RFM segmentation directly in the database.

---

## Key Insights (Sample)

- A small share of customers (~20%) accounts for the majority of revenue, highlighting the value of targeted retention.
- Sales show clear seasonal peaks in Q4, suggesting opportunities for inventory and marketing planning.
- Certain product categories have high volume but low margin, flagging pricing and bundling opportunities.

*(Insights are illustrative of the analysis framework; see the scripts and reports for detailed, data-driven findings.)*

---

## Skills Demonstrated

- Data cleaning and wrangling with Pandas
- Writing analytical SQL queries (joins, aggregations, CTEs, window functions)
- Exploratory data analysis and statistical thinking
- Customer segmentation (RFM analysis)
- Data visualization and dashboard design
- Translating analysis into business recommendations

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/FurYangi/retail-sales-customer-analytics.git
   cd retail-sales-customer-analytics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download a dataset into `data/raw/` (see `data/README.md` for a recommended public dataset).
4. Run the analysis scripts:
   ```bash
   python notebooks/01_data_cleaning_eda.py
   python notebooks/02_customer_segmentation.py
   ```
5. Explore the SQL queries in `sql/` and the generated charts in `reports/`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
