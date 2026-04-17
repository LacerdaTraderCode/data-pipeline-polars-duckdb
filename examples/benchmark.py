"""
Benchmark: Polars vs Pandas em operações comuns.
Executar: python examples/benchmark.py
"""
import time
import random
from pathlib import Path

import polars as pl
import pandas as pd


def benchmark(name: str, fn):
    """Decorator simples para medir tempo."""
    start = time.time()
    result = fn()
    elapsed = time.time() - start
    print(f"  {name:20s} {elapsed:6.3f}s")
    return elapsed, result


def main():
    print("🏁 Gerando dataset de teste (1.000.000 linhas)...")
    n = 1_000_000
    data = {
        "id": list(range(n)),
        "category": [random.choice(["A", "B", "C", "D"]) for _ in range(n)],
        "value": [random.uniform(0, 1000) for _ in range(n)],
    }

    # Salvar CSV para teste
    Path("data").mkdir(exist_ok=True)
    pl.DataFrame(data).write_csv("data/benchmark.csv")

    print("\n📊 BENCHMARK: Leitura CSV + GroupBy + Sort\n")
    print(f"{'Operação':<22}{'Tempo':>8}")
    print("-" * 32)

    # Polars
    print("\n🔷 Polars:")
    t_polars_read, df_pl = benchmark("  Read CSV", lambda: pl.read_csv("data/benchmark.csv"))
    t_polars_agg, _ = benchmark("  GroupBy + Sort",
        lambda: df_pl.group_by("category").agg(pl.col("value").mean()).sort("category"))

    # Pandas
    print("\n🐼 Pandas:")
    t_pd_read, df_pd = benchmark("  Read CSV", lambda: pd.read_csv("data/benchmark.csv"))
    t_pd_agg, _ = benchmark("  GroupBy + Sort",
        lambda: df_pd.groupby("category")["value"].mean().reset_index().sort_values("category"))

    # Resumo
    print("\n📈 RESUMO:")
    print(f"  Leitura CSV:    Polars {t_pd_read / t_polars_read:.1f}x mais rápido")
    print(f"  GroupBy + Sort: Polars {t_pd_agg / t_polars_agg:.1f}x mais rápido")


if __name__ == "__main__":
    main()
