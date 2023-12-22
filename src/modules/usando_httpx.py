import httpx
import time

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_get(post_id: int) -> dict:
    response = httpx.get(f"{BASE_URL}/{post_id}")
    return response.json()

def main() -> None:
    # Recordar o tempo de início
    start = time.perf_counter()

    for post_id in range(1, 51):
        print(f"Fetching post {post_id}")
        print(fetch_get(post_id))

    # Recordar o tempo de término
    end = time.perf_counter()
    print(f"Tempo total: {end - start:.2f} segundos.")

if __name__ == "__main__":
    main()
