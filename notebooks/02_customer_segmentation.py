"""
02_customer_segmentation.py
------------------------------------------------------------
Retail Sales & Customer Analytics
Step 2: Segment customers using RFM analysis
(Recency, Frequency, Monetary).

RFM is a proven marketing technique for identifying high-value
customers and tailoring retention strategies.
------------------------------------------------------------
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

PROCESSED_PATH = "../data/processed/retail_clean.csv"


def load_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["invoice_date"])
    return df


def build_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """Compute Recency, Frequency, and Monetary metrics per customer."""
    snapshot_date = df["invoice_date"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("customer_id").agg(
        recency=("invoice_date", lambda x: (snapshot_date - x.max()).days),
        frequency=("invoice_no", "nunique"),
        monetary=("revenue", "sum"),
    ).reset_index()

    return rfm


def score_rfm(rfm: pd.DataFrame) -> pd.DataFrame:
    """Assign 1-4 quartile scores for each RFM dimension."""
    rfm = rfm.copy()

    # Recency: lower is better, so reverse the labels
    rfm["r_score"] = pd.qcut(rfm["recency"], 4, labels=[4, 3, 2, 1]).astype(int)
    rfm["f_score"] = pd.qcut(
        rfm["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]
    ).astype(int)
    rfm["m_score"] = pd.qcut(rfm["monetary"], 4, labels=[1, 2, 3, 4]).astype(int)

    rfm["rfm_score"] = rfm["r_score"] + rfm["f_score"] + rfm["m_score"]
    return rfm


def assign_segment(row) -> str:
    """Map RFM scores to a human-readable customer segment."""
    r, f, m = row["r_score"], row["f_score"], row["m_score"]
    if r >= 3 and f >= 3 and m >= 3:
        return "Champions"
    if f >= 3 and m >= 3:
        return "Loyal Customers"
    if r >= 3:
        return "Recent / Promising"
    if r == 1 and f >= 3:
        return "At Risk"
    if r == 1:
        return "Lost"
    return "Needs Attention"


def summarize_segments(rfm: pd.DataFrame) -> pd.DataFrame:
    """Aggregate segment-level statistics for reporting."""
    summary = rfm.groupby("segment").agg(
        customers=("customer_id", "count"),
        avg_recency=("recency", "mean"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
        total_revenue=("monetary", "sum"),
    ).sort_values("total_revenue", ascending=False)

    summary["revenue_share_pct"] = (
        100 * summary["total_revenue"] / summary["total_revenue"].sum()
    ).round(1)
    return summary


def plot_segments(summary: pd.DataFrame) -> None:
    plt.figure(figsize=(9, 5))
    sns.barplot(x=summary.index, y=summary["customers"])
    plt.title("Customer Count by Segment")
    plt.ylabel("Customers")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("../reports/segment_counts.png", dpi=120)


def main():
    df = load_clean_data(PROCESSED_PATH)
    rfm = build_rfm(df)
    rfm = score_rfm(rfm)
    rfm["segment"] = rfm.apply(assign_segment, axis=1)

    summary = summarize_segments(rfm)
    print("\n=== RFM Segment Summary ===")
    print(summary)

    plot_segments(summary)
    rfm.to_csv("../data/processed/customer_segments.csv", index=False)
    print("\nSaved customer segments to data/processed/customer_segments.csv")


if __name__ == "__main__":
    main()
