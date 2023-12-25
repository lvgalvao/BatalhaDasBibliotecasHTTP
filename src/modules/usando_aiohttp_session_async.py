from aiohttp import ClientSession
from asyncio import gather, run
import time

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_get(session: ClientSession, post_id: int) -> dict:
    async with session.get(f"{BASE_URL}/{post_id}") as response:
        return await response.json()

async def main() -> None:
    # Recordar o tempo de início
    start = time.perf_counter()

    # Criar uma sessão ClientSession
    async with ClientSession() as session:
        tasks = [fetch_get(session, post_id) for post_id in range(1, 51)]
        responses = await gather(*tasks)

        for post_id, response in enumerate(responses, 1):
            print(f"Post {post_id}: {response}")

    # Recordar o tempo de término
    end = time.perf_counter()
    print(f"Tempo total: {end - start:.2f} segundos.")

# Executar a função main do asyncio
if __name__ == "__main__":
    run(main())
