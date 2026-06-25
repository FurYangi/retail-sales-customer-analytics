"""
01_data_cleaning_eda.py
------------------------------------------------------------
Retail Sales & Customer Analytics
Step 1: Load raw data, clean it, engineer features, and run
exploratory data analysis (EDA).

Run as a script or convert to a Jupyter notebook with:
    jupyter nbconvert --to notebook --execute 01_data_cleaning_eda.py
------------------------------------------------------------
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

RAW_PATH = "../data/raw/online_retail.csv"
PROCESSED_PATH = "../data/processed/retail_clean.csv"


def load_data(path: str) -> pd.DataFrame:
    """Load raw transactional data from CSV."""
    df = pd.read_csv(path, encoding="ISO-8859-1")
    print(f"Loaded {len(df):,} rows and {df.shape[1]} columns.")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize the raw retail dataset."""
    df = df.copy()

    # Standardize column names to snake_case
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_")
    )

    # Drop rows missing critical identifiers
    df = df.dropna(subset=["customer_id", "invoice_no", "stock_code"])

    # Remove cancelled orders (invoice numbers starting with 'C')
    df = df[~df["invoice_no"].astype(str).str.startswith("C")]

    # Keep only positive quantities and prices
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]

    # Parse dates and cast customer_id to int
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    df["customer_id"] = df["customer_id"].astype(int)

    # Remove duplicate transaction lines
    df = df.drop_duplicates()

    print(f"After cleaning: {len(df):,} rows remain.")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create analysis-ready features."""
    df = df.copy()
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["order_month"] = df["invoice_date"].dt.to_period("M").astype(str)
    df["order_dow"] = df["invoice_date"].dt.day_name()
    df["order_hour"] = df["invoice_date"].dt.hour
    return df


def run_eda(df: pd.DataFrame) -> None:
    """Produce key exploratory visualizations and summaries."""
    # Headline KPIs
    print("\n=== Key Metrics ===")
    print(f"Total revenue:   {df['revenue'].sum():,.2f}")
    print(f"Unique customers: {df['customer_id'].nunique():,}")
    print(f"Unique orders:    {df['invoice_no'].nunique():,}")
    print(f"Avg order value:  "
          f"{df.groupby('invoice_no')['revenue'].sum().mean():,.2f}")

    # Monthly revenue trend
    monthly = df.groupby("order_month")["revenue"].sum()
    plt.figure(figsize=(11, 5))
    monthly.plot(marker="o")
    plt.title("Monthly Revenue Trend")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../reports/monthly_revenue.png", dpi=120)

    # Top 10 countries by revenue
    if "country" in df.columns:
        top_countries = (
            df.groupby("country")["revenue"].sum()
            .sort_values(ascending=False).head(10)
        )
        plt.figure(figsize=(9, 5))
        sns.barplot(x=top_countries.values, y=top_countries.index)
        plt.title("Top 10 Markets by Revenue")
        plt.xlabel("Revenue")
        plt.tight_layout()
        plt.savefig("../reports/top_countries.png", dpi=120)


def main():
    df = load_data(RAW_PATH)
    df = clean_data(df)
    df = engineer_features(df)
    run_eda(df)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"\nSaved cleaned dataset to {PROCESSED_PATH}")


if __name__ == "__main__":
    main()
