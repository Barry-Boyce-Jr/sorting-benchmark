# Barry Boyce Jr
# 8/29/2026
# project0
# counter.py

#counter helper functions for all comparison operations
class Counter:
    def __init__(self):
        self.count = 0

    def less(self, a, b):
        self.count += 1
        return a < b

    def great(self, a, b):
        self.count += 1
        return a > b

    def less_eq(self, a, b):
        self.count += 1
        return a <= b

    def great_eq(self, a, b):
        self.count += 1
        return a >= b
    
    def eq(self, a, b):
        self.count += 1
        return a == b