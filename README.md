<div align="center">

# 📊 Data Pipeline — Polars & DuckDB

**A modern ETL pipeline using the most performant tools in the Python ecosystem**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Polars](https://img.shields.io/badge/Polars-CD792C?logo=polars&logoColor=white)](https://pola.rs/)
[![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black)](https://duckdb.org/)
[![License](https://img.shields.io/badge/License-MIT-orange)](https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb)

</div>

---

## 📌 About the Project

A modern ETL pipeline using the most performant tools in the Python data ecosystem: **Polars** for processing (10-100x faster than Pandas), **DuckDB** for analytical SQL queries, and **Parquet** for efficient columnar storage.

Ideal for anyone who wants to study and understand how to build robust, scalable data pipelines without depending on heavy infrastructure.

### Features

- ✅ **Extract** — reading multiple formats: CSV, JSON, Excel, Parquet
- ✅ **Transform** — cleaning, aggregations, and joins with Polars
- ✅ **Load** — storage in compressed Parquet
- ✅ **Query** — SQL analytics with DuckDB directly on Parquet files
- ✅ **Benchmark** — Polars vs Pandas performance comparison
- ✅ **Synthetic data** — automatic generation for testing

---

## 🛠️ Why Polars + DuckDB?

| Scenario | Pandas | Polars | DuckDB |
|---------|--------|--------|--------|
| Reading 1M CSV rows | ~5s | ~0.5s | ~0.8s |
| GroupBy + aggregation | ~3s | ~0.2s | ~0.3s |
| Memory usage | High | Low | Very low |
| SQL queries | ❌ | ⚠️ Limited | ✅ Full |

**Conclusion:** Polars for transformations, DuckDB for SQL analytics.

---

## 📁 Structure

```
data-pipeline-polars-duckdb/
├── pipeline/
│   ├── extract.py          # Reading multiple formats
│   ├── transform.py        # Transformations with Polars
│   ├── load.py             # Writing to Parquet
│   └── analyze.py          # DuckDB queries
├── examples/
│   ├── sales_pipeline.py   # Complete sales pipeline
│   └── benchmark.py        # Polars vs Pandas
├── requirements.txt
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb.git
cd data-pipeline-polars-duckdb

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## ⚡ Quick Usage

### Complete sales pipeline

```bash
python examples/sales_pipeline.py
```

Generates 100,000 rows of synthetic data, processes it with Polars, saves it to Parquet, and runs analyses with DuckDB.

### Polars vs Pandas benchmark

```bash
python examples/benchmark.py
```

### SQL analysis directly on Parquet

```python
import duckdb

result = duckdb.sql("""
    SELECT
        region,
        COUNT(*)       AS total_sales,
        SUM(amount)    AS revenue,
        AVG(amount)    AS avg_ticket
    FROM 'data/sales.parquet'
    WHERE status = 'completed'
    GROUP BY region
    ORDER BY revenue DESC
""").pl()  # Converts to a Polars DataFrame

print(result)
```

---

## ✅ Requirements

- Python **3.11** or higher

---

## 👤 Author

<div align="center">

**Wagner Lacerda** — Senior Software Engineer | Python, Backend, AI Apps, Automation & Systems

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brazil

</div>

---

## 📄 License

Distributed under the MIT license. See [LICENSE](LICENSE) for more details.
