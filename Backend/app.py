import requests
import json

URL = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(URL)

print("Status Code:", response.status_code)

# Get raw text
raw_text = response.text

# Remove problematic control characters
clean_text = raw_text.replace("\n", " ").replace("\r", " ")

# Convert safely
data = json.loads(clean_text)

# Save locally
with open("catalog.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("catalog.json saved successfully!")
print("Total records:", len(data))