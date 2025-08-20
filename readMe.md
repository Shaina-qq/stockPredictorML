# Stock prediction using Random Forest Model #

* Goal: Predict if a stock will go up or down tomorrow.

* Features used to influence stock movement:
    * Momentum → Has the stock been going up recently?
   * Volatility → How jumpy is the stock?
    * RSI → Relative Strength Index (a common trading indicator)
    *Volume → How much trading activity is happening
* Tool: Random Forest → a machine learning model made of many decision trees.
* Outcome: Model predicts “up” or “down” and tells us which factors matter most.

## Project Flowchart

```mermaid
flowchart TD
    A[Download Stock Data] --> B[Clean & Preprocess Data]
    B --> C[Train ML Model]
    C --> D[Make Predictions]
    D --> E[Visualize Results]

