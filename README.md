Barry Boyce Jr
CPSC 447
Fall 2026
Project0 / Warmup

REQUIREMENTS
    Python 3

 HOW TO RUN 
    1. navigate to sorts directory `project0\sorts`
    2. enter CLA `python main.py <selection|merge> test_files/random_1000.txt output.txt results.csv`  
        (this can be recreated with any file from test_files dir)
        (results.csv will be appended each run, located in sorts dir) 
    3. enter CLA `python benchmark.py`
        (bench_results.csv will be recreated each run, located in sorts dir)

COMPARISON COUNT ANALYSIS (Tables)
    Table 1. Selection Sort
    | n      | Sorted     | Reverse    | Random     | Duplicates |
    |--------|------------|------------|------------|------------|
    | 100    | 4,950      | 4,950      | 4,950      | 4,950      |
    | 1,000  | 499,500    | 499,500    | 499,500    | 499,500    |
    | 2,500  | 3,123,750  | 3,123,750  | 3,123,750  | 3,123,750  |
    | 5,000  | 12,497,500 | 12,497,500 | 12,497,500 | 12,497,500 |
    | 10,000 | 49,995,000 | 49,995,000 | 49,995,000 | 49,995,000 |

    Table 2. Selection Sort Theoretical vs. Actual (all data)
    | n      | Theoretical: n(n−1)/2  |    Actual    |
    |--------|------------------------|--------------|
    | 100    | 4,950                  | 4,950        |
    | 1,000  | 499,500                | 499,500      |
    | 2,500  | 3,123,750              | 3,123,750    |
    | 5,000  | 12,497,500             | 12,497,500   |
    | 10,000 | 49,995,000             | 49,995,000   |

    Table 3. Merge Sort
    | n      | Sorted | Reverse | Random  | Duplicates |
    |--------|--------|---------|---------|------------|
    | 100    | 316    | 356     | 542     | 481        |
    | 1,000  | 4,932  | 5,044   | 8,703   | 8,501      |
    | 2,500  | 13,652 | 14,752  | 25,143  | 24,935     |
    | 5,000  | 29,804 | 32,004  | 55,197  | 54,971     |
    | 10,000 | 64,608 | 69,008  | 120,358 | 120,257    |

    Table 4. Merge Sort Theoretical vs. Actual (random data)
    | n      | Theoretical (worst case): n·log₂(n) − n + 1 |    Actual    |
    |--------|---------------------------------------------|---------------
    | 100    | 565.4                                       | 542          | 
    | 1,000  | 9,866                                       | 8,703        |
    | 2,500  | 27,371                                      | 25,143       |
    | 5,000  | 60,141                                      | 55,197       |
    | 10,000 | 129,878                                     | 120,358      |

    From Table 1 and Table 3 we can see that as n increases in size, the number of computations done by the selection sort
    increases significantly more than the number of computations done by the merge sort. This matches the theoretical formulas of both.
    The best,worst and average case for the selection sort algorithm is n(n-1)/2. When looking at Table 2 it is shown that the theoretical results perfectly match the achieved results in bench_results.csv. Table 4's results show the worst case scenario vs. the actual scenario, so the results
    do not perfectly match. However, the relationship between the two still shows that there is a strong relationship between the theoretical worst case scenario and the actual results.


WALL-CLOCK TIME vs. OPERATION COUNT
    Table 5. Comparisons vs. Actual Time (random data)
    | n      | Selection Comparisons    | Selection Time (s)     | Merge Comparisons   | Merge Time (s) |
    |--------|------------------------ --|-------------------------|---------------------|----------------------|
    | 100    | 4,950                     | 0.00051                 | 542                 | 0.00034               |
    | 1,000  | 499,500                   | 0.05835                 | 8,703               | 0.00399               |
    | 2,500  | 3,123,750                 | 0.37584                 | 25,143              | 0.01129               |
    | 5,000  | 12,497,500                | 1.48276                 | 55,197              | 0.02340               |
    | 10,000 | 49,995,000                | 5.94921                 | 120,358             | 0.04911               |

    Table 6. Comparisons vs. Actual Time (sorted data)
    | n      | Selection Comparisons    | Selection Time (s)     | Merge Comparisons   | Merge Time (s) |
    |--------|---------------------------|--------------------------|---------------------|-------------------|
    | 100    | 4,950                     | 0.00056                 | 316                 | 0.00042           |
    | 1,000  | 499,500                   | 0.07443                 | 4,932               | 0.00392           |
    | 2,500  | 3,123,750                 | 0.37438                 | 13,652              | 0.00971           |
    | 5,000  | 12,497,500                | 1.47262                 | 29,804              | 0.01992           |
    | 10,000 | 49,995,000                | 6.20405                 | 64,608              | 0.04209           |

    Table 7. Comparisons vs. Actual Time (reverse data)
    | n      | Selection Comparisons    | Selection Time (s)     | Merge Comparisons   | Merge Time (s) |
    |--------|---------------------------|--------------------------|---------------------|-------------------|
    | 100    | 4,950                     | 0.00058                 | 356                 | 0.00030           |
    | 1,000  | 499,500                   | 0.06859                 | 5,044               | 0.00332           |
    | 2,500  | 3,123,750                 | 0.37238                 | 14,752              | 0.00992           |
    | 5,000  | 12,497,500                | 1.50721                 | 32,004              | 0.02030           |
    | 10,000 | 49,995,000                | 6.11337                 | 69,008              | 0.04255           |

    Table 8. Comparisons vs. Actual Time (duplicate data)
    | n      | Selection Comparisons    | Selection Time (s)     | Merge Comparisons   | Merge Time (s) |
    |--------|---------------------------|--------------------------|-------------------|-------------------|
    | 100    | 4,950                     | 0.00062                 | 481                 | 0.00030           |
    | 1,000  | 499,500                   | 0.06119                 | 8,501               | 0.00375           |
    | 2,500  | 3,123,750                 | 0.36722                 | 24,935              | 0.01076           |
    | 5,000  | 12,497,500                | 1.48660                 | 54,971              | 0.02298           |
    | 10,000 | 49,995,000                | 6.00576                 | 120,257             | 0.04944           |

    It is clear from the results.csv file that is generated from the CLA `python main.py <selection|merge> test_files/random_1000.txt output.txt results.csv`and from the bench_results.csv file that the algorithm that had fewer comparisons (merge sort) did always have a faster wall-clock time than the other algorithm. This became even more noticeable as n grew, with the selection sort's wall clock time taking up to 6.2 seconds in Table 6 with already sorted data.



PEAK MEMORY FOOTPRINT ANALYSIS
    
    Table 9. Peak Resident Memory (B) — Selection Sort 
    | n      | Sorted | Reverse | Random | Duplicates |
    |--------|--------|---------|--------|------------|
    | 100    | 32     | 0       | 0      | 0          |
    | 1,000  | 0      | 0       | 0      | 0          |
    | 2,500  | 0      | 0       | 0      | 0          |
    | 5,000  | 0      | 0       | 0      | 0          |
    | 10,000 | 0      | 0       | 0      | 0          |

    Table 10. Peak Resident Memory (B) — Merge Sort
    | n      | Sorted  | Reverse | Random  | Duplicates |
    |--------|---------|---------|---------|------------|
    | 100    | 2,880   | 2,880   | 2,880   | 2,880      |
    | 1,000  | 25,888  | 25,440  | 25,440  | 25,440     |
    | 2,500  | 67,256  | 66,976  | 66,976  | 66,976     |
    | 5,000  | 128,584 | 128,416 | 128,416 | 128,416    |
    | 10,000 | 254,056 | 253,888 | 253,888 | 253,888    |

    Table 9 and Table 10 both clearly show that both algorithms handle memory allocation differently as n grows in size.
    As shown in Table 9, the selection sort remains 0B no matter then size or the type of array (with the exception being the sorted array with n = 100 which has a peak of 32B. This however, is an outlier and is most possibly from some weird behavior with being the first ran test after tracemalloc is started). This shows that the Selection Sort maintain a flat O(1) auxiliary memory footprint as the selection sort does all the work inside the one array. However, the merge sort shows that the Peak Resident Memory increases as the n increases. Table 10 shows that when n is 100 the peak resident memory across all input types is 2,880B in merge sort. However, this grows to be 25,888B at n=1000, 128,584B at n = 5000, and between 253,888B-254,056B when n = 10000. This shows that Merge Sort exhibits an O(n) linear memory growth due to its auxiliary allocation buffers. This is because unlike the selection sort, merge sort does not do all the work inside the one array. Merge sort has to make multiple temporary arrays in order to split and then re-merge all the arrays it does while sorting. 