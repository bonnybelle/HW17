# Реализовать класс итератор и генератор типа range. (с 1, 2 и 3 аргументами)


class MyIterator:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.args) == 1:
            a = [i for i in range(self.args[0])]
            return a
        elif len(self.args) == 2:
            a = [i for i in range(self.args[0], self.args[1])]
            return a
        elif len(self.args) == 3:
            a = [i for i in range(self.args[0] + 1, self.args[1] + 1)][::self.args[2]]
            return a
        else:
            raise Exception('not enough/too much arguments')


m1 = MyIterator(10)
m2 = MyIterator(-10, 10)
m3 = MyIterator(-10, 10, -2)
m4 = MyIterator(-10, 4, 10, -2)
for i in m1:
    print(i)
    break

for i in m2:
    print(i)
    break

for i in m3:
    print(i)
    break

'''
for i in m4:
    print(i)
    break
'''
# ---------------------------------

print(list(range(10)))
print(list(range(-10, 10)))
print(list(range(10, -10, -2)))
