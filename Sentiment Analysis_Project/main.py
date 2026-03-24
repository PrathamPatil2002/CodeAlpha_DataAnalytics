import pandas as pd
from textblob import TextBlob

# Read data
data = pd.read_csv("data.csv")

# Function to check sentiment
def check_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply function
data["Sentiment"] = data["review"].apply(check_sentiment)

# Print result
print(data)

# Save result
data.to_csv("output.csv", index=False)