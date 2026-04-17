# 📊 Data Pipeline — Polars & DuckDB

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Polars](https://img.shields.io/badge/Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white)](https://pola.rs/)
[![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black)](https://duckdb.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Pipeline ETL moderno usando as ferramentas mais performáticas do ecossistema de dados Python em 2026: **Polars** para processamento (10-100x mais rápido que Pandas), **DuckDB** para queries analíticas e **Parquet** para armazenamento colunar eficiente.

---

## 📋 Funcionalidades

- ✅ **Extract**: leitura de múltiplos formatos (CSV, JSON, Excel, Parquet)
- ✅ **Transform**: limpeza, agregações e joins com Polars
- ✅ **Load**: armazenamento em Parquet comprimido
- ✅ **Query**: análises SQL com DuckDB direto em arquivos Parquet
- ✅ **Benchmarks**: comparação Polars vs Pandas
- ✅ **Geração de dados sintéticos** para testes

---

## 🛠️ Por que Polars + DuckDB?

| Cenário | Pandas | Polars | DuckDB |
|---------|--------|--------|--------|
| Leitura 1M linhas CSV | ~5s | ~0.5s | ~0.8s |
| GroupBy + aggregation | ~3s | ~0.2s | ~0.3s |
| Consumo de memória | Alto | Baixo | Muito baixo |
| Queries SQL | ❌ | ⚠️ Limitado | ✅ Completo |

**Conclusão**: Polars para transformações, DuckDB para análises.

---

## 📁 Estrutura

```
data-pipeline-polars-duckdb/
├── pipeline/
│   ├── __init__.py
│   ├── extract.py          # Leitura de múltiplos formatos
│   ├── transform.py        # Transformações com Polars
│   ├── load.py             # Gravação em Parquet
│   └── analyze.py          # Queries DuckDB
├── examples/
│   ├── sales_pipeline.py   # Pipeline completo de vendas
│   └── benchmark.py        # Polars vs Pandas
├── data/                   # Dados de exemplo (gerados)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/LacerdaTraderCode/data-pipeline-polars-duckdb.git
cd data-pipeline-polars-duckdb

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 Uso

### Pipeline completo de vendas

```bash
python examples/sales_pipeline.py
```

Gera 100.000 linhas de dados sintéticos, processa com Polars, salva em Parquet e executa análises com DuckDB.

### Benchmark Polars vs Pandas

```bash
python examples/benchmark.py
```

---

## 💡 Exemplo de Análise com DuckDB

```python
import duckdb

# Query SQL direto em arquivo Parquet (sem carregar na memória!)
result = duckdb.sql("""
    SELECT 
        region,
        COUNT(*) as total_sales,
        SUM(amount) as revenue,
        AVG(amount) as avg_ticket
    FROM 'data/sales.parquet'
    WHERE status = 'completed'
    GROUP BY region
    ORDER BY revenue DESC
""").pl()  # Converte para DataFrame Polars

print(result)
```

---

## 👨‍💻 Autor

**Wagner Lacerda**  
🔗 [LinkedIn](https://www.linkedin.com/in/wagner-lacerda-da-silva-958b9481)  
🐙 [GitHub](https://github.com/LacerdaTraderCode)  

---

## 📄 Licença

MIT License
