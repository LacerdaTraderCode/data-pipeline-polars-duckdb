from datetime import date

import polars as pl
import pytest


@pytest.fixture
def sales():
    data = {
        "region": ["South", "South", "North", "North", "North"],
        "product": ["Laptop", "Mouse", "Laptop", "Mouse", "Mouse"],
        "amount": [1000.0, 50.0, 2000.0, 100.0, 300.0],
        "status": ["completed", "completed", "completed", "cancelled", "completed"],
        "date": [
            date(2024, 1, 15),
            date(2024, 1, 20),
            date(2024, 2, 10),
            date(2024, 2, 11),
            date(2024, 2, 12),
        ],
    }
    return pl.DataFrame(data)


@pytest.fixture
def sales_parquet(tmp_path, sales):
    path = tmp_path / "sales.parquet"
    sales.write_parquet(path)
    return str(path)
