# Barry Boyce Jr
# 8/29/2026
# project0
# selection_sort.py

from counter import Counter

#selection sort algorithm 
def selection_sort(input, counter):
    for i in range(len(input)):
        index = i
        for j in range(i+1, len(input)):
            if counter.less(input[j], input[index]):
                index = j
        input[i], input[index] = input[index], input[i]
    return input
