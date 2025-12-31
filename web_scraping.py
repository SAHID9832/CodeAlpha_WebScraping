import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print("🔍 Starting Web Scraping Task...")

# Public website for scraping (safe for learning)
url = "https://quotes.toscrape.com/"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Lists to store scraped data
quotes = []
authors = []
tags = []

# Extract relevant data
for quote in soup.find_all("div", class_="quote"):
    quotes.append(quote.find("span", class_="text").text)
    authors.append(quote.find("small", class_="author").text)
    tags.append(", ".join(tag.text for tag in quote.find_all("a", class_="tag")))

# Create custom dataset
df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags
})

# Save dataset to CSV
df.to_csv("quotes_dataset.csv", index=False)

print("\n✅ Web Scraping Completed Successfully!")
print("📁 Dataset saved as: quotes_dataset.csv\n")
print(df.head())

# Keep output open for 15 seconds
time.sleep(15)
print("⏳ Closing in 15 seconds...")