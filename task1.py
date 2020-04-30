# Реализовать класс итератор и генератор типа range. (с 1, 2 и 3 аргументами)


class MyIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        else:
            self.start += 1
            return self.start


for i in MyIterator(5, 10):
    print(i)

# ---------------------------------

print(list(range(10)))
print(list(range(-10, 10)))
print(list(range(10, -10, -2)))
