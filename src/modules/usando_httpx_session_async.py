import httpx
import asyncio
import time

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_get(client: httpx.AsyncClient, post_id: int) -> dict:
    response = await client.get(f"{BASE_URL}/{post_id}")
    return response.json()

async def main() -> None:
    # Recordar o tempo de início
    start = time.perf_counter()

    # Usar httpx.AsyncClient para requisições assíncronas
    async with httpx.AsyncClient() as client:
        tasks = [fetch_get(client, post_id) for post_id in range(1, 51)]
        responses = await asyncio.gather(*tasks)

        for post_id, response in enumerate(responses, 1):
            print(f"Post {post_id}: {response}")

    # Recordar o tempo de término
    end = time.perf_counter()
    print(f"Tempo total: {end - start:.2f} segundos.")

# Executar a função main do asyncio
if __name__ == "__main__":
    asyncio.run(main())
