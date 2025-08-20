# Import necessary libraries
import yfinance as yf          # to download stock data
import pandas as pd            # to handle tabular data
import numpy as np             # for numerical calculations
from sklearn.ensemble import RandomForestClassifier  # the Random Forest model
from sklearn.model_selection import train_test_split  # to split data into training/testing
from sklearn.metrics import accuracy_score           # to check model performance

#================= Download Tesla stock data for the past 6 months ===============#
data =yf.download("TSLA", period="6mo",interval="1d",auto_adjust=False)
data.columns=data.columns.get_level_values(0)  # keep only the first level of column names , not multi-index:tickers -> tsla 
print(data.head()) # show first 5 rows

#================= calculate the factors  =================#

#data is the entire table of stock data with columns like 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'
# so data['Adj Close'] focuses on THE COLOMN is the adjusted closing price of the stock
data['Returns'] = data['Adj Close'].pct_change()  # daily returns

# Momentum: 5-day average return
data['Momentum']=data['Returns'].rolling(window=5).mean()  

# volatility: 20-day rolling standard deviation of returns
data['Volatility'] = data['Returns'].rolling(window=20).std()  


# RSI 14-day 
delta = data ['Adj Close'].diff()  # daily price change
gain=delta.clip(lower=0)  # positive changes
loss= -delta.clip(upper=0)  # negative changes
avg_gain = gain.rolling(window=14).mean()  # average gain over 14
avg_loss = loss.rolling(window=14).mean()  # average loss over 14
rs = avg_gain / avg_loss  # relative strength
data['RSI'] = 100 - (100 / (1 + rs))  # Relative Strength Index (RSI)

# Normalized Volume 
data['Volume_Norm'] = data['Volume']/data['Volume'].rolling(20).mean()  # volume divided by 20-day average  

# drop rows with NaN values (first few rows will have NaN due to rolling calculations)
data= data.dropna()

print("factors calculated:")
print(data[['Returns', 'Momentum', 'Volatility', 'RSI', 'Volume_Norm']].head())  # show first 5 rows of factors 

#================= Prepare data for machine learning =================#
# create target variable 

data['Target']=np.where(data['Returns'].shift(-1)>0, 1, 0)  # 1 if next day return is positive, else 0
print("Target variable created:")
print(data[['Returns','Target']].head(10))

#================= preparing feature and target  =================#
X=data[['Momentum', 'Volatility', 'RSI', 'Volume_Norm']]  # features
y=data['Target']  # target variable
 
print("Features and target ready:")
print(X.head())
print(y.head())

#================= Split data into training and testing sets =================#

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=False
)

print("Training and testing sets created:")
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")
 
#================= Train the Random Forest model =================#
model = RandomForestClassifier(n_estimators=100, random_state=42)  # create model with 100 trees
model.fit(X_train, y_train)  # train the model
print("Model trained successfully.")

#================= Make predictions =================#
y_pred= model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred)  # calculate accuracy comparing the predictions with the actual values
print(f"Model accuracy: {accuracy:.2f}")  # print accuracy  