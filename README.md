# Retail Sales & Customer Analytics

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
|   |-- raw/                 # Original source data
|   |-- processed/          # Cleaned, analysis-ready data
|-- notebooks/
|   |-- 01_data_cleaning.ipynb
|   |-- 02_exploratory_analysis.ipynb
|   |-- 03_customer_segmentation.ipynb
|-- sql/
|   |-- schema.sql          # Table definitions
|   |-- analysis_queries.sql
|-- dashboards/             # Power BI / Tableau files & exports
|-- reports/                # Summary findings & visuals
|-- README.md
```

---

## Methodology

**1. Data Cleaning & Preparation**
Handled missing values, removed duplicates, standardized date and currency formats, and engineered features such as order month, revenue per order, and customer tenure.

**2. Exploratory Data Analysis (EDA)**
Analyzed sales trends across time, products, categories, and regions. Identified seasonality patterns and top/bottom performers.

**3. Customer Segmentation**
Applied RFM analysis (Recency, Frequency, Monetary) to group customers into actionable segments such as Champions, Loyal, At-Risk, and Lost.

**4. Insight & Reporting**
Built dashboards and a summary report translating findings into business recommendations.

---

## Key Insights (Sample)

- A small share of customers (~20%) accounts for the majority of revenue, highlighting the value of targeted retention.
- Sales show clear seasonal peaks in Q4, suggesting opportunities for inventory and marketing planning.
- Certain product categories have high volume but low margin, flagging pricing and bundling opportunities.

*(Insights are illustrative of the analysis framework; see notebooks and reports for detailed, data-driven findings.)*

---

## Skills Demonstrated

- Data cleaning and wrangling with Pandas
- Writing analytical SQL queries (joins, aggregations, window functions)
- Exploratory data analysis and statistical thinking
- Customer segmentation (RFM analysis)
- Data visualization and dashboard design
- Translating analysis into business recommendations

---

## How to Use

1. Clone the repository: `git clone https://github.com/FurYangi/retail-sales-customer-analytics.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Explore the notebooks in the `notebooks/` folder in order.
4. Review SQL queries in the `sql/` folder and dashboards in `dashboards/`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
