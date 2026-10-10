import logging

import polars as pl

logger = logging.getLogger(__name__)


def clean_data(df: pl.DataFrame) -> pl.DataFrame:
    result = df.unique()
    result = result.filter(~pl.all_horizontal(pl.all().is_null()))
    logger.info("Cleaning: %d -> %d rows", len(df), len(result))
    return result


def aggregate_sales(df: pl.DataFrame, group_by: str = "region") -> pl.DataFrame:
    aggregated = df.group_by(group_by).agg(
        pl.len().alias("total_transactions"),
        pl.col("amount").sum().alias("revenue"),
        pl.col("amount").mean().round(2).alias("avg_ticket"),
        pl.col("amount").max().alias("max_sale"),
        pl.col("amount").min().alias("min_sale"),
    )
    return aggregated.sort("revenue", descending=True)


def add_date_features(df: pl.DataFrame, date_col: str = "date") -> pl.DataFrame:
    return df.with_columns(
        pl.col(date_col).dt.year().alias("year"),
        pl.col(date_col).dt.month().alias("month"),
        pl.col(date_col).dt.weekday().alias("weekday"),
        pl.col(date_col).dt.quarter().alias("quarter"),
    )


def filter_by_status(df: pl.DataFrame, status: str = "completed") -> pl.DataFrame:
    result = df.filter(pl.col("status") == status)
    logger.info("Status filter '%s': %d rows", status, len(result))
    return result
