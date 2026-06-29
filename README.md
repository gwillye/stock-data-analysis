# Stock Data Analysis (B3 / yfinance)

This project collects and analyzes Brazilian stock-market data from B3: prices, technical indicators, risk/return metrics and a return-correlation matrix across a basket of stocks.

It started as a notebook that pulled data with yfinance, stored it in SQLite, computed moving averages (SMA 20/50), drew Plotly charts and experimented with Prophet forecasting. On top of that, I added a clean, reusable analysis module that turns the raw prices into actual metrics and a written report.

## What the analysis does

The core of the project is `stock_analysis.py`, a small module that goes beyond the original price + SMA notebook. For each ticker it computes total and annualized return, annualized volatility, a Sharpe-like ratio and RSI(14), plus a daily-return correlation matrix across the whole basket. It then writes a markdown report.

It was run on live 1-year data for a 6-stock basket (PETR4, VALE3, ITUB4, BBDC4, GGBR4, AURE3). The full output lives in `RESULTS.md`. A few of the numbers from that run:

| ticker | total return | ann. vol | Sharpe-like | RSI(14) |
|---|---:|---:|---:|---:|
| VALE3.SA | 0.64 | 0.25 | 2.78 | 50 |
| GGBR4.SA | 0.38 | 0.26 | 1.65 | 20 (oversold) |
| ITUB4.SA | 0.31 | 0.23 | 1.49 | 85 (overbought) |

The correlation matrix recovers structure that makes intuitive sense: the two banks ITUB4/BBDC4 sit around 0.79, PETR4 is roughly 0 with the rest, and the metals VALE3/GGBR4 land near 0.50.

## Files

- `stock_analysis.py`: the analysis module, with `fetch_close`, `metrics` (return/vol/Sharpe/RSI) and `report` (writes `RESULTS.md`).
- `RESULTS.md`: sample output from a live run. It is regenerable and depends on current market data.
- `stock_data_analysis.ipynb`: the original notebook (yfinance to SQLite to SMA to Plotly to Prophet), with outputs cleared.

## How to run

```bash
pip install -r requirements.txt
python stock_analysis.py          # prints results and writes RESULTS.md
```

## Possible extensions

- Add Prophet/ARIMA forecasting with a validation window (MAPE/RMSE). The notebook already scaffolds Prophet.
- More indicators (MACD, Bollinger) plus a simple backtest of an SMA-crossover strategy.
- An interactive Plotly Dash or Streamlit dashboard as a hosted demo.

This is a portfolio project around data science and quantitative finance. Data is fetched at runtime via yfinance, so the database and outputs are not versioned.
