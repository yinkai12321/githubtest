import asyncio
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .services import calculate_congestion, fetch_paths, fetch_vehicle_states

app = FastAPI(title="RGV Congestion Service")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.get("/congestion")
async def congestion() -> dict:
    states, paths = await asyncio.gather(fetch_vehicle_states(), fetch_paths())
    data = calculate_congestion(states, paths)
    return {"congestion": data}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Serve a simple UI to display congestion information."""
    return templates.TemplateResponse("index.html", {"request": request})
