from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(
    title="API Gateway",
    description="Проксирует запросы к user-, book- и order-сервисам",
    version="1.0.0"
)

SERVICE_MAP = {
    "users": "http://user_service:8001",
    "books": "http://book_service:8002",
    "orders": "http://order_service:8003"
}

@app.get("/{service}/{path:path}")
async def proxy_get(service: str, path: str):
    if service not in SERVICE_MAP:
        raise HTTPException(404, "Unknown service")
    url = f"{SERVICE_MAP[service]}/{path}"
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url)
        return r.json()

@app.post("/{service}/{path:path}")
async def proxy_post(service: str, path: str, payload: dict = None):
    if service not in SERVICE_MAP:
        raise HTTPException(404, "Unknown service")
    url = f"{SERVICE_MAP[service]}/{path}"
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(url, json=payload)
        return r.json()