import asyncio
import time
from memory_profiler import memory_usage
import tracemalloc


# Importações
from modules.usando_request import main as lib_request
from modules.usando_request_session import main as lib_request_session
from modules.usando_httpx import main as lib_httpx
from modules.usando_httpx_session import main as lib_httpx_session
from modules.usando_httpx_session_async import main as lib_httpx_session_async
from modules.usando_aiohttp_session_async import main as lib_aiohttp_session_async

def profile_memory_and_time(func, *args, **kwargs):
    start_time = time.perf_counter()

    if asyncio.iscoroutinefunction(func):
        # Execute a coroutine em um novo evento loop
        mem_usage = memory_usage((asyncio.run, (func(*args, **kwargs),)))
    else:
        # Execute a função normalmente
        mem_usage = memory_usage((func, args, kwargs))

    end_time = time.perf_counter()

    time_elapsed = end_time - start_time
    max_mem_usage = max(mem_usage) - min(mem_usage)
    return time_elapsed, max_mem_usage

async def run_async_scripts():
    times = []
    mem_usages = []

    # Executar e medir scripts assíncronos
    for async_script, name in [
        (lib_httpx_session_async, "lib_httpx_session_async"),
        (lib_aiohttp_session_async, "lib_aiohttp_session_async"),
    ]:
        time_elapsed, mem_usage = await asyncio.to_thread(profile_memory_and_time, async_script)
        times.append((name, time_elapsed))
        mem_usages.append((name, mem_usage))

    return times, mem_usages

def main():
    tracemalloc.start()
    times = []
    mem_usages = []

    # Executar e medir scripts síncronos
    for sync_script, name in [
        (lib_request, "lib_request"),
        (lib_request_session, "lib_request_session"),
        (lib_httpx, "lib_httpx"),
        (lib_httpx_session, "lib_httpx_session"),
    ]:
        time_elapsed, mem_usage = profile_memory_and_time(sync_script)
        times.append((name, time_elapsed))
        mem_usages.append((name, mem_usage))

    # Executar scripts assíncronos
    async_times, async_mem_usages = asyncio.run(run_async_scripts())
    times.extend(async_times)
    mem_usages.extend(async_mem_usages)

    # Imprimir os tempos e usos de memória
    print("\nTempos de Execução e Uso de Memória:")
    for (script_name, execution_time), (_, memory_usage) in zip(times, mem_usages):
        print(f"{script_name}: Tempo de execução: {execution_time:.2f} segundos, Uso de memória: {memory_usage:.2f} MiB.")
    tracemalloc.stop()

if __name__ == "__main__":
    main()