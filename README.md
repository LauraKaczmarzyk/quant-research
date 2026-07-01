# quant-research

## Hypothesis

### Economic rationale
This repository evaluates pairs trading and cointegration strategies, focusing on commodity-linked equities. Pairs trading helps identify relative mispricing by comparing similar securities and exploiting mean-reversion in their spread.

The strategy is inspired by seminal research such as “Pairs Trading: Performance of a Relative Value Arbitrage Rule.” The codebase tests whether common commodity-sector pairs exhibit stable relationships and practical trading opportunity.

### Selected pair examples
- **XOM vs CVX** — two large integrated oil majors with similar business models and exposure to crude oil and refining margins.
- **XLE vs XOP** — XLE is a market-cap-weighted energy sector ETF, while XOP is equal-weighted and concentrated in exploration and production names.
- **NEM vs GOLD** — Newmont and Barrick are both large gold miners driven by the same underlying gold price.
- **ADM vs BG** — Archer-Daniels-Midland and Bunge are global agricultural processors/traders exposed to grain and oilseed prices.

### Statistical hypothesis
We test whether the log-price series are cointegrated, meaning a linear combination of the two series is stationary.

Let:
- $p_{A,t} = \ln(P_{A,t})$
- $p_{B,t} = \ln(P_{B,t})$

Then estimate:

$p_{A,t} = \alpha + \beta p_{B,t} + \epsilon_t$

Where $\epsilon_t$ is the spread.

Hypotheses:
- $H_0$: $\epsilon_t$ is non-stationary (no cointegration)
- $H_1$: $\epsilon_t$ is stationary (cointegration exists)

Test using the Augmented Dickey-Fuller (ADF) regression on $\epsilon_t$:

$\Delta \epsilon_t = \gamma \epsilon_{t-1} + \sum_{i=1}^{k} \theta_i \Delta \epsilon_{t-i} + u_t$

If $\gamma = 0$, the spread behaves like a random walk and $H_0$ holds. If $\gamma < 0$ and statistically significant, reject $H_0$ and conclude the pair is cointegrated.

### Trading hypothesis
Assuming the spread is stationary, the mean reversion should be exploitable after transaction costs.

A sample entry rule is:
- enter on $|z_t| > 2$, where $z_t = \frac{\epsilon_t - \hat{\mu}_{\text{roll}}}{\hat{\sigma}_{\text{roll}}}$
- exit when $z_t$ reverts toward zero

The goal is a strategy with a positive Sharpe ratio that remains statistically significant net of transaction costs over an out-of-sample period.

### Falsification conditions
- Out-of-sample Sharpe ratio not statistically distinguishable from zero
- Hedge ratio $\beta$ unstable across rolling estimation windows
- Mean-reversion half-life too long relative to trading costs
- ADF test fails to reject $H_0$ at 5% significance
