from typing import Any
import time
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_get(session: requests.Session, post_id: int) -> Any:
    response = session.get(f"{BASE_URL}/{post_id}")
    return response.json()

def main() -> None:
    # Recordar o tempo de início
    start = time.perf_counter()

    # Criar uma sessão
    with requests.Session() as session:
        # Realizar 50 requisições GET usando a sessão
        for post_id in range(1, 51):
            print(f"Fetching post {post_id}")
            print(fetch_get(session, post_id))

    # Recordar o tempo de término
    end = time.perf_counter()
    print(f"Tempo total: {end - start:.2f} segundos.")

if __name__ == "__main__":
    main()
