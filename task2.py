# Реализовать класс итератора, который будет возвращать переданную ему коллекцию в обратном порядке.

class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.start = collection[::-1][0] + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1
        if self.start:
            return self.start
        else:
            raise StopIteration()


collection = [1, 2, 3, 4]
for i in MyIterator(collection):
    print(i)
