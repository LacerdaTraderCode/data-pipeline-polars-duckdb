import random
import time
from pathlib import Path

import pandas as pd
import polars as pl

CSV_PATH = "data/benchmark.csv"


def timed(name: str, fn):
    start = time.perf_counter()
    result = fn()
    elapsed = time.perf_counter() - start
    print(f"  {name:20s} {elapsed:6.3f}s")
    return elapsed, result


def speedup(baseline: float, candidate: float) -> float:
    return baseline / max(candidate, 1e-9)


def main(rows: int = 1_000_000):
    data = {
        "id": list(range(rows)),
        "category": [random.choice(["A", "B", "C", "D"]) for _ in range(rows)],
        "value": [random.uniform(0, 1000) for _ in range(rows)],
    }

    Path(CSV_PATH).parent.mkdir(exist_ok=True)
    pl.DataFrame(data).write_csv(CSV_PATH)

    print(f"Benchmark ({rows:,} rows): CSV read + group by + sort\n")

    print("Polars:")
    pl_read, pl_df = timed("Read CSV", lambda: pl.read_csv(CSV_PATH))
    pl_agg, _ = timed(
        "Group by + sort",
        lambda: pl_df.group_by("category").agg(pl.col("value").mean()).sort("category"),
    )

    print("\nPandas:")
    pd_read, pd_df = timed("Read CSV", lambda: pd.read_csv(CSV_PATH))
    pd_agg, _ = timed(
        "Group by + sort",
        lambda: pd_df.groupby("category")["value"].mean().reset_index().sort_values("category"),
    )

    print("\nSummary:")
    print(f"  CSV read:        Polars {speedup(pd_read, pl_read):.1f}x faster")
    print(f"  Group by + sort: Polars {speedup(pd_agg, pl_agg):.1f}x faster")


if __name__ == "__main__":
    main()
