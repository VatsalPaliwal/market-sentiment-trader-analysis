# Market Sentiment & Trader Behavior Analysis

## Live Dashboard

Access the interactive Streamlit dashboard here:

👉 [https://your-app-name.streamlit.app](https://market-sentiment-trader-analysis-agvx9iowefj8weinr5qw5y.streamlit.app/)

## Overview

This project analyzes how market sentiment regimes (Fear, Greed, Extreme Greed, Neutral) influence trader performance and behavior.

The study evaluates:

- Profitability differences across regimes  
- Behavioral changes in trading activity and position sizing  
- Heterogeneous effects across trader segments  

The project includes both analytical outputs and an interactive Streamlit dashboard.

---

## Key Research Questions

1. Does trading performance differ across market sentiment regimes?
2. Do traders change behavior (frequency, size) based on sentiment?
3. Do different trader segments react differently to sentiment shifts?

---

## Methodology

### Data Processing
- Converted timestamps and aligned datasets at daily frequency.
- Aggregated trade-level data to daily account-level metrics.
- Merged with sentiment classifications.

### Performance Metrics
- Median Daily PnL  
- Win Rate  
- PnL Volatility (Standard Deviation)  
- Worst Daily Outcome  

### Behavioral Metrics
- Average Trades per Day  
- Median Trades per Day  
- Average Trade Size  

### Segmentation
Traders were segmented based on:

- **Activity Level** (High vs Low average trade frequency)
- **Volatility Profile** (High vs Low PnL dispersion)

Segment performance was evaluated across sentiment regimes.

---

## Key Findings

- **Fear regimes generate the highest profitability and volatility.**
- Trading activity increases significantly during Fear.
- High-activity and high-volatility traders disproportionately benefit during Fear.
- Elevated activity during Neutral regimes reduces performance.

Performance is both regime-dependent and heterogeneous across trader profiles.

---

## Strategy Implications

1. **Regime-Adjusted Trading Intensity**  
   Increase activity during Fear regimes; reduce activity during Neutral regimes.

2. **Risk-Aligned Capital Allocation**  
   High-volatility traders can capture greater upside in Fear environments, while low-volatility traders exhibit muted regime sensitivity.

---
