from shodan import Shodan
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/ip/{ip}")
async def get_ip(ip: str, key: Optional[str] = None):
    if key is None:
        return {"Error": "Please provide a valid API key"}
    else:
        try:
            api = Shodan(key)
            res = api.host(ip)
            return "https://www.openstreetmap.org/?mlat={}&mlon={}#map=12".format(res["latitude"],res["longitude"])
        except Exception as e:
            return {"Error": str(e)}


