# Barry Boyce Jr
# 8/29/2026
# project0
# merge_sort.py

from counter import Counter

# merges sorted lists
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

    return result

# splits and sorts
def merge_sort(input, counter):
    left = []
    right = []
    
    if len(input) <= 1:
        return input

    mid = len(input) // 2

    for i in range(0, mid):
        left.append(input[i])

    for i in range(mid, len(input)):
        right.append(input[i])

    # recursion on sorted lists
    l_sorted = merge_sort(left, counter)
    r_sorted = merge_sort(right, counter)

    # once sorted merge lists
    return merge(l_sorted, r_sorted, counter)
        


