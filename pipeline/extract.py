import logging

import polars as pl

logger = logging.getLogger(__name__)


def read_csv(filepath: str, **kwargs) -> pl.DataFrame:
    df = pl.read_csv(filepath, **kwargs)
    logger.info("CSV read: %s (%d rows, %d columns)", filepath, len(df), len(df.columns))
    return df


def read_json(filepath: str) -> pl.DataFrame:
    df = pl.read_json(filepath)
    logger.info("JSON read: %s (%d rows)", filepath, len(df))
    return df


def read_excel(filepath: str, sheet: str | None = None) -> pl.DataFrame:
    kwargs = {"sheet_name": sheet} if sheet else {}
    df = pl.read_excel(filepath, engine="openpyxl", **kwargs)
    logger.info("Excel read: %s (%d rows)", filepath, len(df))
    return df


def read_parquet(filepath: str) -> pl.DataFrame:
    df = pl.read_parquet(filepath)
    logger.info("Parquet read: %s (%d rows)", filepath, len(df))
    return df


def scan_parquet(filepath: str) -> pl.LazyFrame:
    return pl.scan_parquet(filepath)
