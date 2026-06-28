# -*- coding: utf-8 -*-
"""
stock_analysis.py — quantitative analysis of B3 (Brazilian) stocks.

Improvement over the original notebook: a clean, reusable module that fetches
prices (yfinance), computes **returns, annualized volatility, Sharpe-like ratio,
moving averages and RSI**, and a **return-correlation matrix** across a basket —
then writes a short markdown report. Run `python stock_analysis.py`.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
import yfinance as yf

TRADING_DAYS = 252


def fetch_close(tickers: list[str], period: str = "1y") -> pd.DataFrame:
    """Adjusted close prices for `tickers` over `period` (e.g. '6mo','1y','2y')."""
    data = yf.download(tickers, period=period, interval="1d",
                       auto_adjust=True, progress=False)
    close = data["Close"] if "Close" in data else data
    return close.dropna(how="all")


def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    """Relative Strength Index."""
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(window).mean()
    loss = (-delta.clip(upper=0)).rolling(window).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def metrics(close: pd.DataFrame, rf: float = 0.0) -> pd.DataFrame:
    """Per-ticker: total return, annualized return/volatility, Sharpe-like, last RSI."""
    rets = close.pct_change().dropna()
    rows = {}
    for t in close.columns:
        r = rets[t].dropna()
        ann_ret = (1 + r.mean()) ** TRADING_DAYS - 1
        ann_vol = r.std() * np.sqrt(TRADING_DAYS)
        rows[t] = {
            "total_return": close[t].dropna().iloc[-1] / close[t].dropna().iloc[0] - 1,
            "ann_return": ann_ret,
            "ann_volatility": ann_vol,
            "sharpe_like": (ann_ret - rf) / ann_vol if ann_vol else np.nan,
            "last_RSI14": rsi(close[t]).iloc[-1],
        }
    return pd.DataFrame(rows).T.sort_values("sharpe_like", ascending=False)


def report(tickers: list[str], period: str = "1y", out_md: str | None = "RESULTS.md") -> str:
    close = fetch_close(tickers, period)
    m = metrics(close)
    corr = close.pct_change().corr()
    lines = [f"# Stock analysis — {len(close.columns)} tickers · period={period}\n",
             "## Risk/return metrics\n", m.round(3).to_markdown(),
             "\n\n## Daily-return correlation\n", corr.round(2).to_markdown(), ""]
    txt = "\n".join(lines)
    if out_md:
        open(out_md, "w", encoding="utf-8").write(txt)
    return txt


if __name__ == "__main__":
    basket = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "GGBR4.SA", "AURE3.SA"]
    print(report(basket, period="1y"))
