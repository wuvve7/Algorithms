import time
import os
import psutil


def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 ** 2

start_time = time.time()
start_memory = memory_usage()

#the code

end_time = time.time()
end_memory = memory_usage()
memory_usage_in_mb = end_memory - start_memory
time_elapsed = end_time - start_time

print(f"Time elapsed: {time_elapsed:.2f} seconds")
print(f"Memory usage: {memory_usage_in_mb:.2f} MB")


