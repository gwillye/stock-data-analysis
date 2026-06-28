# Stock Data Analysis & Forecasting (B3 / yfinance)

> *Academic / portfolio project — Data Science.*

Collects, stores and analyzes **historical stock data** (focused on the Brazilian market / B3) and projects trends.

## Pipeline
1. **Collection** — downloads history via **`yfinance`** and persists it in a **SQLite** database (`finance.bd`).
2. **Indicators** — computes **simple moving averages (SMA-20 / SMA-50)** and asset details (sector, industry, currency).
3. **Visualization** — price / SMA charts with **Plotly**.
4. **Forecasting** — time-series projection with **Prophet** / `statsmodels`.

## How to run
```bash
pip install -r requirements.txt
jupyter notebook stock_data_analysis.ipynb
```
Set your list of `tickers` (e.g. `["AURE3.SA","GGBR4.SA"]`) in the configuration cell.

## Roadmap (possible extensions)
- More technical indicators (RSI, MACD, Bollinger) and a strategy **backtest**.
- **Forecast evaluation** (MAPE / RMSE on a validation window) comparing Prophet vs ARIMA.
- Interactive dashboard (Plotly Dash / Streamlit) as a hosted demo.

## Stack
Python · yfinance · SQLite · pandas · Plotly · Prophet / statsmodels
