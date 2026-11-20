"""Step 2: Load the cleaned CSV into a SQLite database."""
import sqlite3
from pathlib import Path
import pandas as pd

CSV = Path("data/clean/superstore_clean.csv")
DB = Path("superstore.db")

df = pd.read_csv(CSV)
with sqlite3.connect(DB) as con:
    df.to_sql("orders", con, if_exists="replace", index=False)
    con.execute("CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id)")
print(f"Loaded {len(df)} rows into {DB} (table: orders)")
