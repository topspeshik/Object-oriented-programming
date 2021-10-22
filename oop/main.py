class Number:
    def __init__(self, value , to_base = 10, from_base= 10):
        self.value = value
        self.to_base = to_base
        self.from_base = from_base

    def summ(self, value, to_base = 10,from_base = 10 ):
        if (from_base != 10):
            return int(value, from_base)

        else:
            return str(value)

    def convert_base(self, num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEF"
        if n < to_base:
            return alphabet[n]
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base]

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.value + other
        elif isinstance(other, Number):
            value = int(self.summ(self.value, self.from_base)) + int(other.summ(other.value, other.from_base))
            return int(self.convert_base(value, self.to_base, self.from_base))

    def __radd__(self, other):
        return self+other

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * other
        elif isinstance(other, Number):
            value = int(self.summ(self.value, self.from_base)) * int(other.summ(other.value, other.from_base))
            return int(self.convert_base(value, self.to_base, self.from_base))

    def __radd__(self, other):
        return self*other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.value - other
        elif isinstance(other, Number):
            value  = int(self.summ(self.value, self.from_base)) - int(other.summ(other.value, other.from_base))
            return int(self.convert_base(value, self.to_base, self.from_base))

    def __rsub__(self, other):
        return  other-self.value

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.value / other
        elif isinstance(other, Number):
            value  = int(self.summ(self.value, self.from_base)) / int(other.summ(other.value, other.from_base))
            return int(self.convert_base(value, self.to_base, self.from_base))

    def __rtruediv__(self, other):
        return other/self.value

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return self.value ** other
        elif isinstance(other, Number):
            value  = int(self.summ(self.value, self.from_base)) ** int(other.summ(other.value, other.from_base))
            return int(self.convert_base(value, self.to_base, self.from_base))

    def __rpow__(self, other):
        return other**self.value

    def __lt__(self, other):
        return self.value < other.value


i = 1
print('Введите экземпляр а')
a = Number(int(input()))
print('Введите экземпляр b')
b = Number(int(input()))
print('Введите экземпляр c и системы счисления, в какую систему счисления надо вывести, в которой находится ')
numb = int(input())
first = int(input())
second = int(input())
c = Number(numb, first, second)
print('Введите число')
num = int(input())


print('a+b: ', a+b)
print('numb/a', numb/a)
print('c-a', c-a)
arr = [(a, 'a'),(b,'b'),(c,'c')] #сортировка кривая, но я не знал как по другому сделать
print(sorted(arr))