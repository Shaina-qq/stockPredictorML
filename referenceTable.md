# 📘 Reference Table for Stock Prediction

This table summarizes the main **classes, functions, and variables** we are using from the libraries (`yfinance`, `pandas`, `numpy`, `sklearn`).  

| **Library** | **Class / Function** | **Meaning** | **Typical Use in Our Code** |
|-------------|-----------------------|-------------|------------------------------|
| `yfinance`  | `yf.download()` | Downloads historical stock price data (Open, High, Low, Close, Volume). | `yf.download("TSLA", start="2022-01-01", end="2023-01-01")` |
| `pandas`    | `DataFrame` | A 2D table (rows = dates, columns = stock data or factors). | Store stock prices and computed factors. |
| `pandas`    | `.rolling(window)` | Creates a moving/rolling window of size `window`. | Used to calculate moving averages or rolling volatility. |
| `pandas`    | `.mean()` | Calculates the mean (average). | Used after `.rolling()` to get moving averages. |
| `pandas`    | `.std()` | Calculates the standard deviation. | Used to measure volatility of stock returns. |
| `pandas`    | `.pct_change()` | Calculates percentage change between consecutive values. | Used to compute daily returns. |

| `numpy`     | `np.log()` | Natural log function. | Used to calculate log returns. |
| `numpy`     | `np.sqrt()` | Square root. | Used in volatility calculations. |
| `sklearn.ensemble` | `RandomForestClassifier` | Machine learning model: builds many decision trees and combines them. | Used to predict stock movement (Up/Down). |
| `sklearn.model_selection` | `train_test_split()` | Splits data into training and testing sets. | Ensures we test model on unseen data. |



---

## 📊 Key Variables We Use

| **Variable** | **Meaning** | **Example** |
|--------------|-------------|-------------|
| `data` | The raw stock price data (from yfinance). | Contains `Open`, `High`, `Low`, `Close`, `Volume`. |
| `returns` | Daily stock returns (percentage change). | `data['Close'].pct_change()` |
| `momentum` | Measures recent price trend. | Rolling average of returns. |
| `volatility` | Measures how “jumpy” the stock is. | Rolling standard deviation of returns. |
| `RSI` | Relative Strength Index (indicator of overbought/oversold). | Computed with rolling averages of gains/losses. |
| `volume` | Trading activity (how many shares traded). | Comes directly from yfinance. |
| `X` | Feature matrix (factors like momentum, volatility, RSI, volume). | Input to Random Forest. |
| `y` | Target variable (1 = stock goes up, 0 = stock goes down). | Output we want to predict. |

---
