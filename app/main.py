import asyncio
from fastapi import FastAPI

from .services import calculate_congestion, fetch_paths, fetch_vehicle_states

app = FastAPI(title="RGV Congestion Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.get("/congestion")
async def congestion() -> dict:
    states, paths = await asyncio.gather(fetch_vehicle_states(), fetch_paths())
    data = calculate_congestion(states, paths)
    return {"congestion": data}
