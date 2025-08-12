import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/cities")
def get_cities():
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    headers = {
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
        "x-rapidapi-host": "wft-geo-db.p.rapidapi.com"
    }
    params = {
        "limit": 10,  # limit number of results
        "offset": 0   # start at the first city
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()
