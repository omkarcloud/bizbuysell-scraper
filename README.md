# 🏪 BizBuySell Scraper

BizBuySell Scraper is a **free and open-source** scraper that gets you **unlimited** detailed BizBuySell data for free.

## ✨ What Can I Get?

- 🏪 **Full details on 14,500+ businesses for sale** — asking price, cash flow, revenue, EBITDA, photos & seller phone
- 🔍 **Search 19 industries & 176 sub-categories** — filter by state, county, price, cash flow, revenue & seller financing
- 🍔 **900+ franchise opportunities** — total investment, franchise fee, royalty, units & average unit revenue
- 🤝 **7,700+ business brokers** — phones, brokerages, licenses, areas served & sold-listing stats

## 🎥 Example: A Full BizBuySell Listing

```json
{
  "id": 2564237,
  "title": "Houston Two Location Hand Car Wash Opportunity",
  "link": "https://www.bizbuysell.com/business-opportunity/houston-two-location-hand-car-wash-opportunity/2564237/",
  "listing_type": "established",
  "description": "HS Listing ID-73378\nAsking Price: $749,000\nTwo Houston Locations\nAverage Monthly Revenue: Approximately $96,079\nAverage Monthly EBITDA: Approximately $32,864\nRecent Annualized Revenue Run Rate: Approximately $1.15 Million...",
  "category": "Car Washes > Other",
  "location": { "name": "Houston, TX", "city": "Houston", "state": "TX", "real_estate": "Leased" },
  "pricing": {
    "asking_price": 749000,
    "cash_flow": 394000,
    "gross_revenue": 1150000,
    "currency": "USD",
    "has_seller_financing": false,
    "is_real_estate_included": false
  },
  "support_and_training": "Yes.",
  "reason_for_selling": "Other business interests.",
  "contact": {
    "name": "Francesco Maola",
    "company": "Hedgestone Business Advisors",
    "profile_link": "https://www.bizbuysell.com/business-broker/francesco-maola/hedgestone-business-advisors/42225/",
    "phone": "516-386-6380",
    "is_broker": true
  },
  "photos": ["https://images.bizbuysell.com/shared/listings/256/2564237/60ad2e30-7593-406c-955e-6bc6fde87b7b-W768.webp"],
  "similar_listings": [
    { "id": 2570968, "title": "3-Store Automotive & Electronics Business | Seller Financing in Houston, Texas", "asking_price": 1700000, "currency": "USD", "location": "Houston, Texas" }
  ]
}
```

*Trimmed for readability.*

## 🚀 Unlimited Free BizBuySell Data — Get It in 60 Seconds

1️⃣ Clone and install:
```bash
git clone https://github.com/omkarcloud/bizbuysell-scraper
cd bizbuysell-scraper
python -m pip install -r requirements.txt
```

2️⃣ Start the API:
```bash
python run.py
```

3️⃣ Get your first data:
```bash
curl "http://localhost:8000/companies/details?company=2564237"
```

```json
{
  "id": 2564237,
  "title": "Houston Two Location Hand Car Wash Opportunity",
  "link": "https://www.bizbuysell.com/business-opportunity/houston-two-location-hand-car-wash-opportunity/2564237/",
  "listing_type": "established",
  "category": "Car Washes > Other",
  "location": { "name": "Houston, TX", "city": "Houston", "state": "TX", "real_estate": "Leased" },
  "pricing": {
    "asking_price": 749000,
    "cash_flow": 394000,
    "gross_revenue": 1150000,
    "currency": "USD",
    "has_seller_financing": false
  },
  "reason_for_selling": "Other business interests.",
  "contact": {
    "name": "Francesco Maola",
    "company": "Hedgestone Business Advisors",
    "phone": "516-386-6380",
    "is_broker": true
  }
}
```

All 8 endpoints are now live at `http://localhost:8000`.

## 📚 Endpoints

8 endpoints cover everything you need.

| Endpoint | Path | Returns |
|---|---|---|
| Business Listing Details | `/companies/details` | Asking price, cash flow, revenue, description, photos and seller phone |
| Search Businesses for Sale | `/companies/search` | 50 listings per page; filter by state, county, industry, price, cash flow |
| Count Businesses for Sale | `/companies/counts` | Matching totals split into established, asset sale, real estate, startup |
| Search Franchises | `/franchises/search` | 50 franchises per page with cash required and unit revenue |
| Franchise Details | `/franchises/details` | Investment range, fees, royalty, units, unit revenue, HQ and CEO |
| Search Business Brokers | `/brokers/search` | 30 brokers per page with phone, brokerage, photo and listing counts |
| Broker Details | `/brokers/details` | Full profile: services, areas served, licenses and sold listings |
| List Categories | `/categories/list` | Every industry, sub-category, franchise category and state to filter by |

## 🔍 Exploring Parameters

The same API is published on RapidAPI, and its playground is the easiest place to try parameters and see raw responses. Once a request looks right, run it locally for **unlimited free** data.

1. [Subscribe to the free plan](https://rapidapi.com/OmkarCloud/api/best-bizbuysell-scraper-free-1000-calls/pricing) — 1,000 calls/month, no credit card.
2. [Try the endpoints in the playground](https://rapidapi.com/OmkarCloud/api/best-bizbuysell-scraper-free-1000-calls/playground) — every param is pre-filled, so you see real data in one click.
3. Copy the generated code and replace `https://best-bizbuysell-scraper-free-1000-calls.p.rapidapi.com` with `http://localhost:8000`. It will now run against your local API.

```python
import requests

# generated by the playground, host swapped for the local API
response = requests.get(
    "http://localhost:8000/companies/search",
    params={"query": "car wash", "state": "TX", "sort": "cash_flow_desc"},
)
print(response.json())
```

## 💬 Have Questions? We Have Answers.

You're a developer — we know how hard completing a project can be. So we offer full support: just message us and we'll reply ✅ with a solution within 1 working day.

[![Message Us on WhatsApp about BizBuySell Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://www.omkar.cloud/l/bizbuysell-scraper-github-whatsapp)

[![Ask Us by Email about BizBuySell Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=Help%20with%20BizBuySell%20Scraper%20API&body=I%20need%20help%20using%20the%20BizBuySell%20Scraper%20API.)

## ⚡ Popular Scrapers by Omkar Cloud

- [**Google Maps Scraper (3,100+ GitHub Stars)**](https://github.com/omkarcloud/google-maps-scraper) — type "dentists in New York", get every business as a ready-to-call lead list: phones, emails, websites & reviews. Up to 100K free leads/month.
- [**G2 Scraper**](https://www.omkar.cloud/tools/g2-scraper) — G2 product details, ratings & AI-found contacts
- [**Website Email Contact Scraper**](https://www.omkar.cloud/tools/website-email-contact-scraper) — emails, phones & socials from any website
- [**AliExpress Scraper**](https://www.omkar.cloud/tools/aliexpress-scraper-api) — live product details, SKU variants, stock & shipping
- [**Booking Scraper**](https://www.omkar.cloud/tools/booking-scraper) — Booking.com hotels: prices, ratings, rooms & amenities
- [**Crexi Scraper**](https://github.com/omkarcloud/crexi-scraper) — commercial real estate for sale & lease, auctions & brokers: price, rent, spaces & photos

## ⭐ Love It? [Star It ⭐!](https://github.com/omkarcloud/bizbuysell-scraper)

Star the repo ⭐ and become my star hero!

It's just 1 click, but it means the world to me.

[![Star us on GitHub](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/star-us.png)](https://github.com/omkarcloud/bizbuysell-scraper)
