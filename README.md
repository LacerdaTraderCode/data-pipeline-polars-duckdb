<div align="center">

# 📊 Data Pipeline — Polars & DuckDB

**Pipeline ETL moderno com as ferramentas mais performáticas do ecossistema Python**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Polars](https://img.shields.io/badge/Polars-CD792C?logo=polars&logoColor=white)](https://pola.rs/)
[![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black)](https://duckdb.org/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-orange)](https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb)

</div>

---

## 📌 Sobre o projeto

Pipeline ETL moderno usando as ferramentas mais performáticas do ecossistema de dados Python: **Polars** para processamento (10–100× mais rápido que Pandas), **DuckDB** para queries analíticas em SQL e **Parquet** para armazenamento colunar eficiente.

Ideal para quem quer estudar e entender como construir pipelines de dados robustos e escaláveis sem depender de infraestrutura pesada.

### Funcionalidades

- ✅ **Extract** — leitura de múltiplos formatos: CSV, JSON, Excel, Parquet
- ✅ **Transform** — limpeza, agregações e joins com Polars
- ✅ **Load** — armazenamento em Parquet comprimido
- ✅ **Query** — análises SQL com DuckDB direto em arquivos Parquet
- ✅ **Benchmark** — comparação de performance Polars vs Pandas
- ✅ **Dados sintéticos** — geração automática para testes

---

## 🛠️ Por que Polars + DuckDB?

| Cenário | Pandas | Polars | DuckDB |
|---------|--------|--------|--------|
| Leitura 1M linhas CSV | ~5s | ~0.5s | ~0.8s |
| GroupBy + aggregation | ~3s | ~0.2s | ~0.3s |
| Consumo de memória | Alto | Baixo | Muito baixo |
| Queries SQL | ❌ | ⚠️ Limitado | ✅ Completo |

**Conclusão:** Polars para transformações, DuckDB para análises SQL.

---

## 📁 Estrutura

```
data-pipeline-polars-duckdb/
├── pipeline/
│   ├── extract.py          # Leitura de múltiplos formatos
│   ├── transform.py        # Transformações com Polars
│   ├── load.py             # Gravação em Parquet
│   └── analyze.py          # Queries DuckDB
├── examples/
│   ├── sales_pipeline.py   # Pipeline completo de vendas
│   └── benchmark.py        # Polars vs Pandas
├── requirements.txt
└── README.md
```

---

## 📦 Instalação

```bash
git clone https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb.git
cd data-pipeline-polars-duckdb

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## ⚡ Uso rápido

### Pipeline completo de vendas

```bash
python examples/sales_pipeline.py
```

Gera 100.000 linhas de dados sintéticos, processa com Polars, salva em Parquet e executa análises com DuckDB.

### Benchmark Polars vs Pandas

```bash
python examples/benchmark.py
```

### Análise SQL direto em Parquet

```python
import duckdb

result = duckdb.sql("""
    SELECT
        region,
        COUNT(*)       AS total_sales,
        SUM(amount)    AS revenue,
        AVG(amount)    AS avg_ticket
    FROM 'data/sales.parquet'
    WHERE status = 'completed'
    GROUP BY region
    ORDER BY revenue DESC
""").pl()  # Converte para DataFrame Polars

print(result)
```

---

## ✅ Requisitos

- Python **3.11** ou superior

---

## 👤 Autor

<div align="center">

**Wagner Lacerda** — Python Backend Developer | APIs REST • Automação • Data Engineering

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brasil

</div>

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
