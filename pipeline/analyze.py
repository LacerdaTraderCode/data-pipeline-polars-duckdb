"""
Módulo Analyze - Queries SQL em arquivos Parquet com DuckDB.
"""
import duckdb
import polars as pl


def query_parquet(sql: str, parquet_path: str) -> pl.DataFrame:
    """
    Executa query SQL direto em Parquet (sem carregar na memória).
    Use o placeholder '{path}' para referenciar o arquivo na query.
    """
    sql = sql.replace("{path}", f"'{parquet_path}'")
    result = duckdb.sql(sql).pl()
    return result


def revenue_by_region(parquet_path: str) -> pl.DataFrame:
    """Análise: receita por região."""
    return query_parquet("""
        SELECT 
            region,
            COUNT(*) as total_sales,
            ROUND(SUM(amount), 2) as revenue,
            ROUND(AVG(amount), 2) as avg_ticket
        FROM {path}
        WHERE status = 'completed'
        GROUP BY region
        ORDER BY revenue DESC
    """, parquet_path)


def top_products(parquet_path: str, limit: int = 10) -> pl.DataFrame:
    """Análise: top N produtos por receita."""
    return query_parquet(f"""
        SELECT 
            product,
            COUNT(*) as sales_count,
            ROUND(SUM(amount), 2) as total_revenue
        FROM {{path}}
        WHERE status = 'completed'
        GROUP BY product
        ORDER BY total_revenue DESC
        LIMIT {limit}
    """, parquet_path)


def monthly_trend(parquet_path: str) -> pl.DataFrame:
    """Análise: tendência mensal de vendas."""
    return query_parquet("""
        SELECT 
            DATE_TRUNC('month', date) as month,
            COUNT(*) as transactions,
            ROUND(SUM(amount), 2) as revenue
        FROM {path}
        WHERE status = 'completed'
        GROUP BY month
        ORDER BY month
    """, parquet_path)
