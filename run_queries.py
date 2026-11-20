"""Step 3: Run every query in sql/analysis_queries.sql and export CSVs for the dashboard."""
import re
import sqlite3
from pathlib import Path
import pandas as pd

SQL = Path("sql/analysis_queries.sql").read_text()
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

blocks = re.split(r"^-- name:\s*(\w+)\s*$", SQL, flags=re.M)[1:]
with sqlite3.connect("superstore.db") as con:
    for name, query in zip(blocks[::2], blocks[1::2]):
        df = pd.read_sql_query(query.strip().rstrip(";"), con)
        df.to_csv(OUT / f"{name}.csv", index=False)
        print(f"\n== {name} ({len(df)} rows) ==")
        print(df.head(10).to_string(index=False))
