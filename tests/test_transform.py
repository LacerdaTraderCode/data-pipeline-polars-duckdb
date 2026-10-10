import polars as pl

from pipeline.transform import add_date_features, aggregate_sales, clean_data, filter_by_status


def test_clean_data_removes_duplicates_and_empty_rows():
    data = {"a": [1, 1, None], "b": ["x", "x", None]}
    df = pl.DataFrame(data)

    result = clean_data(df)

    assert result.to_dicts() == [{"a": 1, "b": "x"}]


def test_clean_data_keeps_partially_null_rows():
    df = pl.DataFrame({"a": [1, None], "b": [None, "y"]})

    assert len(clean_data(df)) == 2


def test_aggregate_sales_by_region(sales):
    result = aggregate_sales(sales)

    assert result["region"].to_list() == ["North", "South"]
    north = result.row(0, named=True)
    assert north["total_transactions"] == 3
    assert north["revenue"] == 2400.0
    assert north["avg_ticket"] == 800.0
    assert north["max_sale"] == 2000.0
    assert north["min_sale"] == 100.0


def test_aggregate_sales_supports_custom_dimension(sales):
    result = aggregate_sales(sales, group_by="product")

    assert result["product"].to_list() == ["Laptop", "Mouse"]


def test_add_date_features(sales):
    result = add_date_features(sales)

    first = result.row(0, named=True)
    assert (first["year"], first["month"], first["weekday"], first["quarter"]) == (2024, 1, 1, 1)


def test_filter_by_status_defaults_to_completed(sales):
    result = filter_by_status(sales)

    assert len(result) == 4
    assert set(result["status"]) == {"completed"}


def test_filter_by_status_accepts_custom_status(sales):
    assert len(filter_by_status(sales, "cancelled")) == 1
