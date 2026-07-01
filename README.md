# quant-research

## Hypothesis

### Economic rationale
This codebase deals with pairs trading/cointegration and the possible profit based on it. The "pairs trading" strategy has been popular. The most relevant paper, "Pairs Trading: Performance of a Relative Value Arbitrage Rule", has over 1442 citations. In this codebase, this method will be further evaluated on the following common selection of commodity-linked equities.

Pairs trading aids in the determination of whether a security is overvalued or undervalued, using relative pricing.

### Statistical hypothesis
Is there a stable long-term linear relationship between the two price series such that their combination is stationary?

Formally:
Take log prices $p_{A,t} = \ln(P_{A,t})$ and $p_{B,t} = \ln(P_{B,t})$:

$p_{A,t} = \alpha + \beta p_{B,t} + \epsilon_t$

Where $\epsilon_t$ is the spread.

- $H_0$: $\epsilon_t$ is non-stationary (no cointegration present)
- $H_1$: $\epsilon_t$ is stationary (A and B are cointegrated)

This is going to be tested with the use of the Augmented Dickey-Fuller (ADF) test applied to $\epsilon_t$.

$\Delta \epsilon_t = \gamma \epsilon_{t-1} + \sum_{i=1}^{k} \theta_i \Delta \epsilon_{t-i} + u_t$

Then, if $\gamma = 0$, $\epsilon_t$ is a random walk and $H_0$ holds. If $\gamma < 0$ and statistically significant, reject $H_0$ and conclude cointegration.

### Trading hypothesis
Is the reversion exploitable net of costs?

Given $\epsilon_t$ is stationary, its mean-reverting shall be modeled.

Given a trading rule that enters when $z_t = \frac{\epsilon_t - \hat{\mu}_{\text{roll}}}{\hat{\sigma}_{\text{roll}}}$ exceeds $\pm 2$ and exits at $z_t \to 0$, the resulting strategy generates a Sharpe ratio $> 0$ that is statistically distinguishable from zero after transaction costs of $c$ bps per round trip, over an out-of-sample period distinct from the estimation window.

### Falsification conditions
- Out-of-sample Sharpe ratio not statistically distinguishable from zero
- TBD