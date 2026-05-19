# ml.pandas

import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Example non-stationary data
data = [10, 21, 31, 40, 52, 61, 71]

# Convert into pandas Series
series = pd.Series(data)

# Function to check stationarity
def check_stationarity(series):

    result = adfuller(series)

    print("ADF Statistic:", format(result[0], ".6f"))
    print("p-value:", format(result[1], ".10f"))

    if result[1] <= 0.05:
        print("Data is Stationary")
    else:
        print("Data is Non-Stationary")


# Original Data
print("Original Data")
print(series)

check_stationarity(series)

# First Differencing
first_diff = series.diff().dropna()

print("\nAfter First Differencing")
print(first_diff)

check_stationarity(first_diff)