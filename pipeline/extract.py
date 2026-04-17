"""
Módulo Extract - Leitura de múltiplos formatos de origem.
"""
from pathlib import Path
import polars as pl


def read_csv(filepath: str, **kwargs) -> pl.DataFrame:
    """Lê CSV retornando DataFrame Polars."""
    df = pl.read_csv(filepath, **kwargs)
    print(f"📥 CSV lido: {filepath} ({len(df):,} linhas, {len(df.columns)} colunas)")
    return df


def read_json(filepath: str) -> pl.DataFrame:
    """Lê JSON (newline-delimited ou array)."""
    df = pl.read_json(filepath)
    print(f"📥 JSON lido: {filepath} ({len(df):,} linhas)")
    return df


def read_excel(filepath: str, sheet: str = None) -> pl.DataFrame:
    """Lê planilha Excel."""
    kwargs = {"sheet_name": sheet} if sheet else {}
    df = pl.read_excel(filepath, **kwargs)
    print(f"📥 Excel lido: {filepath} ({len(df):,} linhas)")
    return df


def read_parquet(filepath: str) -> pl.DataFrame:
    """Lê Parquet (formato colunar eficiente)."""
    df = pl.read_parquet(filepath)
    print(f"📥 Parquet lido: {filepath} ({len(df):,} linhas)")
    return df


def scan_parquet(filepath: str) -> pl.LazyFrame:
    """
    Scan lazy de Parquet - não carrega nada na memória até executar.
    Ideal para arquivos grandes.
    """
    return pl.scan_parquet(filepath)
