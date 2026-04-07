import time
import tracemalloc
from functools import wraps

def performance(func):
    counter = 0
    total_time = 0
    total_mem = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter, total_time, total_mem

        counter += 1

        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time += elapsed_time
        total_mem += peak

        wrapper.counter = counter
        wrapper.total_time = total_time
        wrapper.total_mem = total_mem

        return result

    wrapper.counter = 0
    wrapper.total_time = 0
    wrapper.total_mem = 0

    return wrapper
