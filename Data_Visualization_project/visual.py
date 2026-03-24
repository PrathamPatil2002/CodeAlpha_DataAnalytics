import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# 3. Line Chart → Price Trend
df["Price"].plot(kind="line")
plt.title("Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()