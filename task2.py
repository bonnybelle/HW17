# Реализовать класс итератора, который будет возвращать переданную ему коллекцию в обратном порядке.


class MyIterator:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return self

    def __next__(self):
        return self.collection[::-1]


collection = [i for i in range(10)]
for i in MyIterator(collection):
    print(i)
    break
