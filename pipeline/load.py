"""
Módulo Load - Gravação em Parquet e outros formatos.
"""
from pathlib import Path
import polars as pl


def save_parquet(df: pl.DataFrame, filepath: str, compression: str = "snappy") -> None:
    """
    Salva DataFrame em Parquet.
    
    Compressões disponíveis:
    - 'snappy': rápida, boa compressão (padrão)
    - 'zstd': melhor compressão, mais lenta
    - 'lz4': muito rápida, compressão menor
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(filepath, compression=compression)

    size_mb = Path(filepath).stat().st_size / 1024 / 1024
    print(f"💾 Parquet salvo: {filepath} ({size_mb:.2f} MB, compressão {compression})")


def save_csv(df: pl.DataFrame, filepath: str) -> None:
    """Salva em CSV (para compatibilidade)."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(filepath)
    print(f"💾 CSV salvo: {filepath}")


def save_partitioned_parquet(
    df: pl.DataFrame, base_path: str, partition_by: str
) -> None:
    """
    Salva particionado por uma coluna (cada valor vira uma pasta).
    Útil para datasets grandes e queries seletivas.
    """
    Path(base_path).mkdir(parents=True, exist_ok=True)

    for value in df[partition_by].unique():
        partition_df = df.filter(pl.col(partition_by) == value)
        partition_path = f"{base_path}/{partition_by}={value}/data.parquet"
        Path(partition_path).parent.mkdir(parents=True, exist_ok=True)
        partition_df.write_parquet(partition_path)

    print(f"💾 Dataset particionado em: {base_path}/ (coluna: {partition_by})")
