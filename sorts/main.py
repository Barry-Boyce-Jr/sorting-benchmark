# Barry Boyce Jr
# CPSC 447
# Fall 2026
# 8/30/2026
# project0
# main.py

import sys
import time
import csv
from counter import Counter
from selection_sort import selection_sort
from merge_sort import merge_sort, merge
from pathlib import Path

#error if usage incorrect
if len(sys.argv) != 5:
    print("Usage: python main.py <selection|merge> <input_file> <output_file> <result_file>")
    sys.exit(1)

#saves cla
algorithm = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]
result_file = sys.argv[4]

#error for algorithm cla 
if algorithm != "selection" and algorithm != "merge":
    print("algorithm must be 'merge' or 'selection'")
    sys.exit(1)

#read input file
with open(input_file, "r") as file:
    input = [line.strip() for line in file]

#counter and timer
counter = Counter()
start = time.perf_counter()

#sorts
if algorithm == "selection":
    sorted = selection_sort(input, counter)

if algorithm == "merge":
    sorted = merge_sort(input, counter)

end = time.perf_counter()
elapsed = end - start

# writes to output file
with open(output_file, "w") as output:
    for word in sorted:
        output.write(word + "\n")

file_exists = Path(result_file).exists()

# write to results file
with open(result_file, "a", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    if not file_exists:
        writer.writerow(["algorithm", "size", "comparisons", "time(secs)"])
    writer.writerow([algorithm, len(input), counter.count, elapsed])
         






