import duckdb
import polars as pl

REVENUE_BY_REGION_SQL = """
    SELECT
        region,
        COUNT(*) AS total_sales,
        ROUND(SUM(amount), 2) AS revenue,
        ROUND(AVG(amount), 2) AS avg_ticket
    FROM {path}
    WHERE status = 'completed'
    GROUP BY region
    ORDER BY revenue DESC
"""

TOP_PRODUCTS_SQL = """
    SELECT
        product,
        COUNT(*) AS sales_count,
        ROUND(SUM(amount), 2) AS total_revenue
    FROM {path}
    WHERE status = 'completed'
    GROUP BY product
    ORDER BY total_revenue DESC
    LIMIT {limit}
"""

MONTHLY_TREND_SQL = """
    SELECT
        DATE_TRUNC('month', date) AS month,
        COUNT(*) AS transactions,
        ROUND(SUM(amount), 2) AS revenue
    FROM {path}
    WHERE status = 'completed'
    GROUP BY 1
    ORDER BY 1
"""


def query_parquet(sql: str, parquet_path: str) -> pl.DataFrame:
    escaped_path = parquet_path.replace("'", "''")
    return duckdb.sql(sql.replace("{path}", f"'{escaped_path}'")).pl()


def revenue_by_region(parquet_path: str) -> pl.DataFrame:
    return query_parquet(REVENUE_BY_REGION_SQL, parquet_path)


def top_products(parquet_path: str, limit: int = 10) -> pl.DataFrame:
    sql = TOP_PRODUCTS_SQL.replace("{limit}", str(int(limit)))
    return query_parquet(sql, parquet_path)


def monthly_trend(parquet_path: str) -> pl.DataFrame:
    return query_parquet(MONTHLY_TREND_SQL, parquet_path)
