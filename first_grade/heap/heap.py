class Heapster:
    def __init__(self):
        self.storage = []

    def insert(self, el):
        self.storage.append(el)

    def heapSort(self):
        length = len(self.storage)

        for start in range(length, -1, -1):
            self.heapPick(start, length - 1)

        for end in range(length - 1, 0, -1):
            self.storage[end], self.storage[0] = self.storage[0], self.storage[end]
            self.heapPick(0, end - 1)

        return self.storage

    def heapPick(self, start, end):

        index = start

        while True:
            child = index * 2 + 1
            if child > end:
                break

            if child + 1 <= end and self.storage[child] < self.storage[child + 1]:
                child += 1

            if self.storage[index] < self.storage[child]:
                self.storage[index], self.storage[child] = self.storage[child], self.storage[index]
                index = child
            else:
                break

    def Full(self):
        for i in range(len(self.storage)):
            lChild = 2 * i + 1
            rChild = 2 * i + 2

            if (rChild < len(self.storage) and lChild >= len(self.storage)) or (rChild >= len(self.storage) and lChild < len(self.storage)):
                return False

        return True


def print_heapify(ar):
    ml = max(len(str(x)) for x in ar)
    ars = [('{:0'+str(ml)+'}').format(x) for x in ar]
    dp = len(bin(len(ar))) - 1
    print('*' * 2**(dp-2) * (ml + 1))
    for i in range(1, dp + 1):
        str_space = ' ' * max(0, 2**(dp-i-2) * (ml + 1) - 1 - ml // 2)
        sep_space = ' ' * max(0, 2**(dp-i-1) * (ml + 1) - ml)
        print(str_space + sep_space.join(ars[2**(i-1) - 1: 2**i - 1]))
    print('*' * 2**(dp-2) * (ml + 1))


hr = Heapster()

hr.insert(12)
hr.insert(11)
hr.insert(10)
hr.insert(-2)
hr.insert(5)
hr.insert(3)
hr.insert(1)
hr.insert(8)
hr.insert(8)


print(hr.storage)
hr.heapSort()
print(hr.storage)
print_heapify(hr.storage)

print("Дерево полное - ", hr.Full())





