import polars as pl
import pytest

from pipeline.load import save_csv, save_parquet, save_partitioned_parquet


def test_save_parquet_roundtrip_creates_directories(tmp_path, sales):
    path = tmp_path / "nested" / "sales.parquet"

    save_parquet(sales, str(path))

    assert pl.read_parquet(path).equals(sales)


@pytest.mark.parametrize("compression", ["snappy", "zstd", "lz4"])
def test_save_parquet_supports_compression_codecs(tmp_path, sales, compression):
    path = tmp_path / f"{compression}.parquet"

    save_parquet(sales, str(path), compression=compression)

    assert len(pl.read_parquet(path)) == len(sales)


def test_save_csv_roundtrip_creates_directories(tmp_path, sales):
    path = tmp_path / "nested" / "sales.csv"

    save_csv(sales.drop("date"), str(path))

    assert pl.read_csv(path).columns == ["region", "product", "amount", "status"]


def test_save_partitioned_parquet_writes_one_folder_per_value(tmp_path, sales):
    base = tmp_path / "partitioned"

    save_partitioned_parquet(sales, str(base), "region")

    folders = sorted(folder.name for folder in base.iterdir())
    assert folders == ["region=North", "region=South"]
    north = pl.read_parquet(base / "region=North" / "data.parquet")
    assert len(north) == 3
