# Sales Performance Analysis & Dashboard

End-to-end analysis of retail sales data: **clean (Python) → analyze (SQL) → visualize (dashboard) → recommend (business decisions).**

**Tools:** Python (pandas), SQL (SQLite), Power BI / Tableau / Excel
**Dataset:** [Superstore Sales (Kaggle)](https://www.kaggle.com/) – search "Superstore Sales" and download the CSV
**Live dashboard:** [add your link here]

## Business questions
1. How are revenue and profit trending month by month?
2. Which products, categories and regions drive or hurt profit?
3. How do discounts affect profit?
4. How much revenue comes from repeat customers?

## Project structure
```
├── data/raw/            # put Superstore.csv here (not committed)
├── data/clean/          # cleaned output
├── src/
│   ├── clean_data.py       # cleaning + cleaning log
│   ├── load_to_sqlite.py   # loads data into SQLite
│   └── run_queries.py      # runs SQL, exports CSVs
├── sql/analysis_queries.sql  # 8 analysis queries
├── outputs/             # query results used in the dashboard
└── dashboard/           # dashboard guide + screenshots
```

## How to run
```bash
pip install -r requirements.txt
# 1. place the dataset at data/raw/Superstore.csv
python src/clean_data.py
python src/load_to_sqlite.py
python src/run_queries.py
```

## Data cleaning summary
| Step | Result |
|---|---|
| Raw rows | [X] |
| Duplicates removed | [X] |
| Invalid dates dropped | [X] |
| Clean rows | [X] |

## SQL analysis
Queries cover KPIs, monthly trend, top/bottom products, regional performance, category margins, discount vs profit, and new vs repeat customers. See `sql/analysis_queries.sql`.

## Key insights and recommendations
> Replace with your own findings after running the queries.
1. **[Insight]**, e.g. "Orders with discounts above [X]% had a margin of [X]%." → **Recommendation:** [action].
2. **[Insight]** → **Recommendation:** [action].
3. **[Insight]** → **Recommendation:** [action].

## Dashboard
![Dashboard](dashboard/screenshots/dashboard.png)

## Author
Chhoti Kumari – [GitHub](https://github.com/chhoti305)
