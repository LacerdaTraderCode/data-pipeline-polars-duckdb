import pytest

from examples import benchmark, sales_pipeline


def test_generate_sales_data_shape_and_values():
    df = sales_pipeline.generate_sales_data(50)

    assert len(df) == 50
    assert df.columns == [
        "transaction_id",
        "date",
        "customer",
        "region",
        "product",
        "amount",
        "status",
    ]
    assert set(df["region"]) <= set(sales_pipeline.REGIONS)
    assert set(df["status"]) <= set(sales_pipeline.STATUSES)
    assert df["amount"].min() >= 50


def test_sales_pipeline_runs_end_to_end(tmp_path, capsys):
    output = tmp_path / "out" / "sales.parquet"

    sales_pipeline.main(n_rows=200, output_path=str(output))

    printed = capsys.readouterr().out
    assert output.exists()
    assert "Revenue by region" in printed
    assert "Top 5 products" in printed
    assert "Monthly trend" in printed


def test_timed_returns_elapsed_time_and_result():
    elapsed, result = benchmark.timed("noop", lambda: 42)

    assert elapsed >= 0
    assert result == 42


def test_speedup_ratio_and_zero_guard():
    assert benchmark.speedup(2.0, 1.0) == pytest.approx(2.0)
    assert benchmark.speedup(1.0, 0.0) > 1


def test_benchmark_runs_on_small_dataset(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    benchmark.main(rows=2_000)

    assert (tmp_path / "data" / "benchmark.csv").exists()
    printed = capsys.readouterr().out
    assert "Polars:" in printed
    assert "Summary:" in printed
