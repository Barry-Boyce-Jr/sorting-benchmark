# Barry Boyce Jr
# 8/30/2026
# project0
# benchmark.py

import time
import csv
import tracemalloc
from counter import Counter
from selection_sort import selection_sort
from merge_sort import merge_sort, merge

# finds the file paths for the test files
def read_inputs(test_case):
    with open(test_case, "r") as file:
        input = [line.strip() for line in file]
    return input

# runs input files, takes time, count, and tracks memory
def run_test(algorithm, input):
    counter = Counter()
    tracemalloc.start()            # for memory 
    start = time.perf_counter()

    if algorithm == "selection":
        sorted = selection_sort(input, counter)

    if algorithm == "merge":
        sorted = merge_sort(input, counter)

    end = time.perf_counter()
    elapsed = end - start

    # returns peak memory used
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return counter.count, elapsed, peak

# all combinations of test files
types = ['sorted', 'reverse', 'random', 'duplicates']
sizes = [100, 1000, 2500, 5000, 10000]
algorithms = ['selection', 'merge']

# loops through all test files & outputs results
with open("bench_results.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["algorithm", "type", "size", "comparisons", "time(secs)", "memory(peak)"])

    for size in sizes:
        for type in types:
            path = f"test_files/{type}_{size}.txt"
            input = read_inputs(path)
            for algorithm in algorithms:
                count, elapsed, peak = run_test(algorithm, input.copy())
                writer.writerow([algorithm, type, size, count, elapsed, peak])
                print(f"{algorithm} sort for {type}_{size}.txt complete")     # progress