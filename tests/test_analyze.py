import shutil
from datetime import date

import polars as pl

from pipeline.analyze import monthly_trend, query_parquet, revenue_by_region, top_products
from pipeline.transform import add_date_features


def test_revenue_by_region_counts_only_completed_sales(sales_parquet):
    result = revenue_by_region(sales_parquet)

    assert result["region"].to_list() == ["North", "South"]
    assert result["total_sales"].to_list() == [2, 2]
    assert result["revenue"].to_list() == [2300.0, 1050.0]
    assert result["avg_ticket"].to_list() == [1150.0, 525.0]


def test_top_products_ranks_by_revenue(sales_parquet):
    result = top_products(sales_parquet)

    assert result["product"].to_list() == ["Laptop", "Mouse"]
    assert result["total_revenue"].to_list() == [3000.0, 350.0]


def test_top_products_respects_limit(sales_parquet):
    result = top_products(sales_parquet, limit=1)

    assert result["product"].to_list() == ["Laptop"]


def test_monthly_trend_groups_by_month(sales_parquet):
    result = monthly_trend(sales_parquet)

    assert result["month"].cast(pl.Date).to_list() == [date(2024, 1, 1), date(2024, 2, 1)]
    assert result["transactions"].to_list() == [2, 2]
    assert result["revenue"].to_list() == [1050.0, 2300.0]


def test_monthly_trend_works_when_data_already_has_month_column(tmp_path, sales):
    path = tmp_path / "featured.parquet"
    add_date_features(sales).write_parquet(path)

    result = monthly_trend(str(path))

    assert result["revenue"].to_list() == [1050.0, 2300.0]


def test_query_parquet_substitutes_path_placeholder(sales_parquet):
    result = query_parquet("SELECT COUNT(*) AS n FROM {path}", sales_parquet)

    assert result["n"].to_list() == [5]


def test_query_parquet_escapes_quotes_in_path(tmp_path, sales_parquet):
    quoted_path = tmp_path / "it's.parquet"
    shutil.copy(sales_parquet, quoted_path)

    result = query_parquet("SELECT COUNT(*) AS n FROM {path}", str(quoted_path))

    assert result["n"].to_list() == [5]
