"""Step 1: Clean the raw Superstore CSV and print a cleaning log."""
import re
import sys
from pathlib import Path
import pandas as pd

RAW = Path("data/raw/Superstore.csv")
OUT = Path("data/clean/superstore_clean.csv")


def snake(col: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", col.strip().lower()).strip("_")


def main():
    if not RAW.exists():
        sys.exit(f"Put the Kaggle Superstore CSV at {RAW}")
    df = pd.read_csv(RAW, encoding="latin-1")
    log = {"rows_raw": len(df)}

    df.columns = [snake(c) for c in df.columns]

    log["duplicates_removed"] = int(df.duplicated().sum())
    df = df.drop_duplicates()

    for c in ("order_date", "ship_date"):
        df[c] = pd.to_datetime(df[c], errors="coerce")
    log["invalid_dates_dropped"] = int(df["order_date"].isna().sum())
    df = df.dropna(subset=["order_date"])

    log["missing_values_before"] = int(df.isna().sum().sum())
    for c in df.select_dtypes("object"):
        df[c] = df[c].str.strip()
    if "postal_code" in df:
        df["postal_code"] = df["postal_code"].fillna(0).astype(int).astype(str)
    num = ["sales", "quantity", "discount", "profit"]
    df[num] = df[num].apply(pd.to_numeric, errors="coerce")
    df = df.dropna(subset=num)

    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
    df["ship_date"] = pd.to_datetime(df["ship_date"]).dt.strftime("%Y-%m-%d")
    df["profit_margin"] = (df["profit"] / df["sales"]).round(4)

    log["rows_clean"] = len(df)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    print("Cleaning log")
    for k, v in log.items():
        print(f"  {k}: {v}")
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    main()
