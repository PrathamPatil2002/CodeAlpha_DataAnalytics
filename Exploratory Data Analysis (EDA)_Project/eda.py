import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

# Show first 5 rows
print("First 5 Rows:\n", df.head())

# Data info
print("\nData Info:")
print(df.info())

# Summary statistics
print("\nSummary:\n", df.describe())

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Group by product
print("\nTotal Quantity by Product:")
print(df.groupby("Product")["Quantity"].sum())

# Group by city
print("\nAverage Price by City:")
print(df.groupby("City")["Price"].mean())

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# EDA
print(df.head())
print(df.info())
print(df.describe())

# Graph
df.groupby("Product")["Quantity"].sum().plot(kind="bar")
plt.title("Total Quantity by Product")
plt.show()