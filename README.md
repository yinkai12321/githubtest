# RGV Congestion Service

A FastAPI service that reads vehicle and path data from Redis and computes a simple congestion index for each grid cell.

## Endpoints

- `GET /health` – basic health check.
- `GET /congestion` – returns cells where more than one vehicle or path step are present.
- `GET /` – simple HTML page that lists congested cells.

## Running

```bash
pip install -r requirements.txt
python start.py
```

Configure the Redis connection with the `REDIS_URL` environment variable. The default is `redis://localhost:6379/0`.
