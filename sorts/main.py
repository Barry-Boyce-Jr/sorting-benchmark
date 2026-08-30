# Barry Boyce Jr
# 8/30/2026
# project0
# counter.py

import sys

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