# Barry Boyce Jr
# 8/29/2026
# project0
# merge_sort.py

from counter import Counter

def merge(left, right, counter):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if counter.less_eq (left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

# append remaining values
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1




