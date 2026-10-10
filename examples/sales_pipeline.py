import random
from datetime import datetime, timedelta

import polars as pl
from faker import Faker

from pipeline.analyze import monthly_trend, revenue_by_region, top_products
from pipeline.load import save_parquet
from pipeline.transform import add_date_features, clean_data

REGIONS = ["South", "Southeast", "Northeast", "North", "Central-West"]
PRODUCTS = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headset",
    "Webcam",
    "Printer",
    "SSD",
    "RAM",
    "Graphics Card",
]
STATUSES = ["completed", "completed", "completed", "cancelled", "pending"]


def generate_sales_data(n_rows: int = 100_000) -> pl.DataFrame:
    fake = Faker("en_US")
    base_date = datetime(2024, 1, 1)

    data = {
        "transaction_id": [f"TX{i:08d}" for i in range(n_rows)],
        "date": [base_date + timedelta(days=random.randint(0, 730)) for _ in range(n_rows)],
        "customer": [fake.name() for _ in range(n_rows)],
        "region": [random.choice(REGIONS) for _ in range(n_rows)],
        "product": [random.choice(PRODUCTS) for _ in range(n_rows)],
        "amount": [round(random.uniform(50, 5000), 2) for _ in range(n_rows)],
        "status": [random.choice(STATUSES) for _ in range(n_rows)],
    }

    return pl.DataFrame(data)


def main(n_rows: int = 100_000, output_path: str = "data/sales.parquet"):
    df = generate_sales_data(n_rows)
    df = clean_data(df)
    df = add_date_features(df, "date")
    save_parquet(df, output_path)

    print("Revenue by region:")
    print(revenue_by_region(output_path))

    print("\nTop 5 products:")
    print(top_products(output_path, limit=5))

    print("\nMonthly trend (first 6 rows):")
    print(monthly_trend(output_path).head(6))


if __name__ == "__main__":
    main()
