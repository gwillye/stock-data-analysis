# Stock Data Analysis (B3 / yfinance)

Collects and analyzes **Brazilian stock-market data (B3)**: prices, technical
indicators, **risk/return metrics** and a **return-correlation matrix** across a basket.

## ✨ Improvement (real, runnable analysis)
Beyond the original notebook (price + SMA), this adds **`stock_analysis.py`** — a clean,
reusable module that computes **total/annualized return, annualized volatility, a
Sharpe-like ratio, RSI(14)** per ticker and a **daily-return correlation matrix**, then
writes a markdown report. It was **run on live 1-year data** for a 6-stock basket
(PETR4, VALE3, ITUB4, BBDC4, GGBR4, AURE3) — see **`RESULTS.md`** for the actual output, e.g.:

| ticker | total return | ann. vol | Sharpe-like | RSI(14) |
|---|---:|---:|---:|---:|
| VALE3.SA | 0.64 | 0.25 | **2.78** | 50 |
| GGBR4.SA | 0.38 | 0.26 | 1.65 | 20 *(oversold)* |
| ITUB4.SA | 0.31 | 0.23 | 1.49 | 85 *(overbought)* |

The correlation matrix recovers intuitive structure (the two banks ITUB4/BBDC4 ≈ **0.79**;
PETR4 ≈ **0** with the rest; metals VALE3/GGBR4 ≈ **0.50**).

## Files
- **`stock_analysis.py`** — `fetch_close`, `metrics` (return/vol/Sharpe/RSI), `report` (→ `RESULTS.md`).
- **`RESULTS.md`** — sample output from a live run (regenerable; market-data dependent).
- **`stock_data_analysis.ipynb`** — original notebook: yfinance → SQLite → SMA → Plotly → Prophet (outputs cleared).

## Run
```bash
pip install -r requirements.txt
python stock_analysis.py          # prints + writes RESULTS.md
```

## Possible extensions
- Add **Prophet/ARIMA forecasting with a validation window** (MAPE/RMSE) — the notebook scaffolds Prophet.
- More indicators (MACD, Bollinger) + a simple **backtest** of an SMA-crossover strategy.
- Interactive **Plotly Dash / Streamlit** dashboard as a hosted demo.

> Portfolio project (Data Science / quantitative finance). Data fetched at runtime via `yfinance`; DB/outputs not versioned.
