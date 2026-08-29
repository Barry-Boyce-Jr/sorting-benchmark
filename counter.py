# Barry Boyce Jr


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