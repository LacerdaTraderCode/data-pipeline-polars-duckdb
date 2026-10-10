import logging
from pathlib import Path

import polars as pl

logger = logging.getLogger(__name__)


def save_parquet(df: pl.DataFrame, filepath: str, compression: str = "snappy") -> None:
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(filepath, compression=compression)

    size_mb = Path(filepath).stat().st_size / 1024 / 1024
    logger.info("Parquet saved: %s (%.2f MB, %s compression)", filepath, size_mb, compression)


def save_csv(df: pl.DataFrame, filepath: str) -> None:
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(filepath)
    logger.info("CSV saved: %s", filepath)


def save_partitioned_parquet(df: pl.DataFrame, base_path: str, partition_by: str) -> None:
    for value in df[partition_by].unique():
        partition_df = df.filter(pl.col(partition_by) == value)
        partition_path = Path(base_path) / f"{partition_by}={value}" / "data.parquet"
        partition_path.parent.mkdir(parents=True, exist_ok=True)
        partition_df.write_parquet(partition_path)

    logger.info("Partitioned dataset saved: %s/ (column: %s)", base_path, partition_by)
