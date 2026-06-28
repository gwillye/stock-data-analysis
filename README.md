# Stock Data Analysis & Forecasting (B3 / yfinance)

Coleta, armazena e analisa **dados históricos de ações** (foco no mercado brasileiro/B3) e
projeta tendências.

## Pipeline
1. **Coleta** — baixa o histórico via **`yfinance`** e persiste num banco **SQLite** (`finance.bd`).
2. **Indicadores** — calcula **médias móveis simples (SMA-20 / SMA-50)** e detalhes do ativo (setor, indústria, moeda).
3. **Visualização** — gráficos de preço/SMA com **Plotly**.
4. **Previsão** — projeção de séries temporais com **Prophet** / `statsmodels`.

## Como rodar
```bash
pip install -r requirements.txt
jupyter notebook stock_data_analysis.ipynb
```
Defina sua lista de `tickers` (ex.: `["AURE3.SA","GGBR4.SA"]`) na célula de configuração.

## Possíveis extensões (próximos passos)
- Mais indicadores técnicos (RSI, MACD, Bollinger) e **backtest** de uma estratégia.
- **Avaliação** do forecast (MAPE/RMSE em janela de validação) comparando Prophet vs ARIMA.
- Dashboard interativo (Plotly Dash/Streamlit) como demo hospedado.

> Notebook acadêmico/portfólio (Data Science). Outputs limpos; o `.bd` não é versionado.
