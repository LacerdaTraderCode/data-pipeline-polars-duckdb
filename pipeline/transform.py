"""
Módulo Transform - Limpeza e transformação com Polars.
"""
import polars as pl


def clean_data(df: pl.DataFrame) -> pl.DataFrame:
    """Operações comuns de limpeza."""
    result = df.clone()

    # Remove duplicatas
    result = result.unique()

    # Remove linhas totalmente nulas
    result = result.filter(~pl.all_horizontal(pl.all().is_null()))

    print(f"🧹 Limpeza: {len(df):,} → {len(result):,} linhas")
    return result


def aggregate_sales(df: pl.DataFrame, group_by: str = "region") -> pl.DataFrame:
    """Agregação de vendas por dimensão."""
    return df.group_by(group_by).agg([
        pl.len().alias("total_transactions"),
        pl.col("amount").sum().alias("revenue"),
        pl.col("amount").mean().round(2).alias("avg_ticket"),
        pl.col("amount").max().alias("max_sale"),
        pl.col("amount").min().alias("min_sale"),
    ]).sort("revenue", descending=True)


def add_date_features(df: pl.DataFrame, date_col: str = "date") -> pl.DataFrame:
    """Adiciona colunas derivadas de data (ano, mês, dia-da-semana)."""
    return df.with_columns([
        pl.col(date_col).dt.year().alias("year"),
        pl.col(date_col).dt.month().alias("month"),
        pl.col(date_col).dt.weekday().alias("weekday"),
        pl.col(date_col).dt.quarter().alias("quarter"),
    ])


def filter_by_status(df: pl.DataFrame, status: str = "completed") -> pl.DataFrame:
    """Filtra linhas por status."""
    result = df.filter(pl.col("status") == status)
    print(f"🔍 Filtro status='{status}': {len(result):,} linhas")
    return result
