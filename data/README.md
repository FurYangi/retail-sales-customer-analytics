# Data

This folder holds the datasets used in the project. Raw data files are **not committed** to keep the repository lightweight (and are typically git-ignored).

## Folder layout

```
data/
|-- raw/         # Original, unmodified source data
|-- processed/   # Cleaned, analysis-ready data produced by the scripts
```

## Getting the dataset

This project is designed to work with a transactional retail dataset. A great public option is the **Online Retail** dataset:

- UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/352/online+retail
- It contains real online transactions (invoices, products, quantities, prices, customer IDs, and countries).

## Setup steps

1. Download the dataset and place it in `data/raw/` as `online_retail.csv`.
2. Run `notebooks/01_data_cleaning_eda.py` to clean it and generate `data/processed/retail_clean.csv`.
3. Run `notebooks/02_customer_segmentation.py` to build customer segments.

> Note: Column names in the scripts use snake_case (e.g. `invoice_no`, `unit_price`, `customer_id`). The cleaning script standardizes raw column headers automatically.
