"""Use the scraper straight from Python — no server needed.

    python main.py

Every function returns the same JSON the API does; results are written to
output/*.json. Params go through the same schemas the API uses, so defaults
are filled in and a listing id or link both work.
"""
import json
import os

from bizbuysell import api, schemas

os.makedirs("output", exist_ok=True)


def save(name, data):
    path = os.path.join("output", name)
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"saved {path}")


def run(schema_cls, fn, **params):
    return fn(**schema_cls().load(params))


if __name__ == "__main__":
    # a listing id or any bizbuysell.com listing link — asking price, cash flow, revenue, seller phone
    save("listing_houston_car_wash.json",
         run(schemas.CompanySchema, api.company_details, company="2564237"))

    # 50 businesses for sale per page, filter by keyword, state, price, cash flow and more
    save("search_car_wash_texas.json",
         run(schemas.CompaniesSearchSchema, api.companies_search, query="car wash", state="TX"))

    # a franchise slug or link — investment range, fees, units and unit revenue
    save("franchise_the_ups_store.json",
         run(schemas.FranchiseSchema, api.franchise_details, franchise="the-ups-store"))
