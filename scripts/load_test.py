"""Simple async load test for /api/call/start endpoint."""
import asyncio
import time
import httpx

API = "http://127.0.0.1:8000/api/call/start"

async def send_task(client, i):
    payload = {"task_id": f"task-{i}", "script": "Halo", "concurrency": 1}
    start = time.perf_counter()
    r = await client.post(API, json=payload, timeout=10.0)
    elapsed = time.perf_counter() - start
    return r.status_code, elapsed

async def run(n: int = 10):
    async with httpx.AsyncClient() as client:
        tasks = [send_task(client, i) for i in range(n)]
        results = await asyncio.gather(*tasks)
    codes = [r for r, _ in results]
    times = [t for _, t in results]
    print(f"Requests: {len(times)}; success: {sum(1 for c in codes if c==200)}")
    print(f"Median: {sorted(times)[len(times)//2]:.3f}s; p95: {sorted(times)[int(len(times)*0.95)-1]:.3f}s")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=10)
    args = p.parse_args()
    asyncio.run(run(args.n))
