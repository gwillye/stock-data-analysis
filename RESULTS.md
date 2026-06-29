# Stock analysis: 6 tickers, period = 1y

This is the report produced by `stock_analysis.py` over a basket of six B3 (Brazilian) tickers, using one year of daily adjusted-close prices pulled from yfinance. The script computes a handful of risk and return metrics per ticker and a correlation matrix of daily returns across the whole basket. Everything below is generated automatically, so the numbers are exactly what came out of the run.

A quick note on how things are calculated, in case you want to read the table without digging into the code:

- `total_return` is just the price change from the first day to the last day of the window (last price divided by first price, minus one).
- `ann_return` annualizes the average daily return assuming 252 trading days per year.
- `ann_volatility` is the daily standard deviation of returns scaled by the square root of 252.
- `sharpe_like` is the annualized return divided by the annualized volatility (risk-free rate set to zero here, hence "Sharpe-like" rather than a textbook Sharpe ratio).
- `last_RSI14` is the most recent value of the 14-day Relative Strength Index, a momentum gauge that runs from 0 to 100. Readings near 70 and above are often read as overbought, and readings near 30 and below as oversold.

The metrics table is sorted by `sharpe_like` (best risk-adjusted return at the top).

## Risk/return metrics

|          |   total_return |   ann_return |   ann_volatility |   sharpe_like |   last_RSI14 |
|:---------|---------------:|-------------:|-----------------:|--------------:|-------------:|
| VALE3.SA |          0.637 |        0.695 |            0.25  |         2.781 |       50.323 |
| GGBR4.SA |          0.381 |        0.433 |            0.263 |         1.649 |       20.106 |
| ITUB4.SA |          0.308 |        0.347 |            0.233 |         1.49  |       85.333 |
| PETR4.SA |          0.316 |        0.36  |            0.248 |         1.451 |       25.079 |
| BBDC4.SA |          0.177 |        0.216 |            0.251 |         0.862 |       66.514 |
| AURE3.SA |          0.164 |        0.226 |            0.319 |         0.709 |       47.692 |

Reading the table, VALE3.SA clearly stands out over the window: a total return of 0.637 (about 63.7 percent) with an annualized volatility of 0.25, which gives it the strongest Sharpe-like figure of the group at 2.781. GGBR4.SA, ITUB4.SA and PETR4.SA form a middle tier, all with Sharpe-like values between roughly 1.45 and 1.65. BBDC4.SA and AURE3.SA bring up the rear, with AURE3.SA showing both the lowest total return (0.164) and the highest volatility (0.319), which is exactly the combination that drags its risk-adjusted score down to 0.709.

The RSI column tells a different, shorter-term story. At the end of the window GGBR4.SA (20.106) and PETR4.SA (25.079) sit in oversold territory, while ITUB4.SA (85.333) looks heavily overbought and BBDC4.SA (66.514) is leaning that way. VALE3.SA (50.323) and AURE3.SA (47.692) are sitting close to the neutral middle. Keep in mind RSI is a momentum snapshot of the latest days, so it does not have to line up with the longer-horizon return numbers, and here it does not.

## Daily-return correlation

This matrix is the pairwise correlation of daily returns across the basket. Values close to 1 move together, values near 0 move independently, and negative values tend to move in opposite directions.

| Ticker   |   AURE3.SA |   BBDC4.SA |   GGBR4.SA |   ITUB4.SA |   PETR4.SA |   VALE3.SA |
|:---------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| AURE3.SA |       1    |       0.45 |       0.28 |       0.44 |      -0    |       0.2  |
| BBDC4.SA |       0.45 |       1    |       0.5  |       0.79 |       0.03 |       0.4  |
| GGBR4.SA |       0.28 |       0.5  |       1    |       0.42 |       0.01 |       0.5  |
| ITUB4.SA |       0.44 |       0.79 |       0.42 |       1    |       0.08 |       0.33 |
| PETR4.SA |      -0    |       0.03 |       0.01 |       0.08 |       1    |      -0.05 |
| VALE3.SA |       0.2  |       0.4  |       0.5  |       0.33 |      -0.05 |       1    |

The most obvious pair here is the two big banks, BBDC4.SA and ITUB4.SA, correlated at 0.79, which makes sense since they are exposed to very similar drivers. After that you see moderate links between the financials and the rest of the basket, mostly in the 0.4 to 0.5 range (for example GGBR4.SA with BBDC4.SA at 0.5 and with VALE3.SA at 0.5).

The interesting outlier is PETR4.SA. It is essentially uncorrelated with everything else in the basket: 0.08 against ITUB4.SA, 0.03 against BBDC4.SA, 0.01 against GGBR4.SA, and slightly negative against both AURE3.SA (-0, i.e. rounding to zero) and VALE3.SA (-0.05). In practice that means PETR4.SA was marching to its own beat over this window, which is the kind of low-correlation behavior that helps diversify a portfolio.
