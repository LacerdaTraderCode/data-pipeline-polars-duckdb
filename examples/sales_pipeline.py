"""
Pipeline ETL completo: gera dados sintéticos de vendas, processa,
salva em Parquet e executa análises com DuckDB.

Executar: python examples/sales_pipeline.py
"""
import sys
import random
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent))

import polars as pl
from faker import Faker

from pipeline.transform import clean_data, add_date_features, filter_by_status
from pipeline.load import save_parquet
from pipeline.analyze import revenue_by_region, top_products, monthly_trend


def generate_sales_data(n_rows: int = 100_000) -> pl.DataFrame:
    """Gera dataset sintético de vendas."""
    print(f"🎲 Gerando {n_rows:,} linhas de dados sintéticos...")
    fake = Faker("pt_BR")

    regions = ["Sul", "Sudeste", "Nordeste", "Norte", "Centro-Oeste"]
    products = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset", "Webcam",
                "Impressora", "SSD", "Memória RAM", "Placa de Vídeo"]
    statuses = ["completed", "completed", "completed", "cancelled", "pending"]

    base_date = datetime(2024, 1, 1)
    data = {
        "transaction_id": [f"TX{i:08d}" for i in range(n_rows)],
        "date": [base_date + timedelta(days=random.randint(0, 730)) for _ in range(n_rows)],
        "customer": [fake.name() for _ in range(n_rows)],
        "region": [random.choice(regions) for _ in range(n_rows)],
        "product": [random.choice(products) for _ in range(n_rows)],
        "amount": [round(random.uniform(50, 5000), 2) for _ in range(n_rows)],
        "status": [random.choice(statuses) for _ in range(n_rows)],
    }

    return pl.DataFrame(data)


def main():
    output_path = "data/sales.parquet"

    # EXTRACT — gerando dados sintéticos
    df = generate_sales_data(100_000)

    # TRANSFORM
    print("\n🔄 Transformando dados...")
    df = clean_data(df)
    df = add_date_features(df, "date")

    # LOAD
    print("\n💾 Salvando em Parquet...")
    save_parquet(df, output_path)

    # ANALYZE com DuckDB
    print("\n📊 Análises com DuckDB (query SQL direto no Parquet):\n")

    print("📍 Receita por região:")
    print(revenue_by_region(output_path))

    print("\n🏆 Top 5 produtos:")
    print(top_products(output_path, limit=5))

    print("\n📅 Tendência mensal (primeiras 6 linhas):")
    print(monthly_trend(output_path).head(6))

    print("\n✅ Pipeline concluído!")


if __name__ == "__main__":
    main()
