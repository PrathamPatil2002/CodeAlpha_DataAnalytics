import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL (quotes.toscrape.com is safe for practice)
url = "http://quotes.toscrape.com/"

# Get webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("span", class_="text")

# Extract data
data = []
for q in quotes:
    data.append(q.text)

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Quotes"])

# Show output
print(df)

# Save file
df.to_csv("quotes.csv", index=False)