import time

def computational_task(n):
    """Calculates the sum of squares up to n."""
    result = 0
    for i in range(n):
        result += i * i
    return result

def measure_performance(n, iterations):
    """Runs the task multiple times and returns execution times."""
    times = []
    for _ in range(iterations):
        start_time = time.perf_counter()
        computational_task(n)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times

# Configuration
small_load = 100_000
large_load = 1_000_000
runs = 5

print(f"--- Performance Test: {runs} Runs ---")

# 1. Measure Small Workload
small_times = measure_performance(small_load, runs)
avg_small = sum(small_times) / runs

print(f"\nWorkload: {small_load} elements")
for i, t in enumerate(small_times, 1):
    print(f"  Run {i}: {t:.6f} seconds")
print(f"  Average: {avg_small:.6f} seconds")

# 2. Measure Large Workload
large_times = measure_performance(large_load, runs)
avg_large = sum(large_times) / runs

print(f"\nWorkload (Increased): {large_load} elements")
for i, t in enumerate(large_times, 1):
    print(f"  Run {i}: {t:.6f} seconds")
print(f"  Average: {avg_large:.6f} seconds")

# 3. Calculate Differences
diff = avg_large - avg_small
print("\n" + "="*30)
print(f"Execution Time Difference: {diff:.6f} seconds")
print(f"The large workload was approximately {avg_large/avg_small:.1f}x slower.")