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

    def __str__(self):
        return str(self.value)


try:
    print('Введите экземпляр а')
    a = Number(int(input()))
    print('Введите экземпляр b')
    b = Number(int(input()))
    print('Введите число')
    num = int(input())
except ValueError:
    print('Вы ввели строку вместо числа')

try:
    print('Введите экземпляр c, затем в какую систему счисления надо вывести, затем в которой находится ')

    numb, first, second  = map(int, input().split())
    c = Number(numb, first, second)
except ValueError:
    print('Вы ввели неправильно системы счисления')
try:
    print('a+b: ', a+b)
    print('numb/a: ', numb/a)
    print('c-a: ', c-a)
    arr = [a,b,c]
    arr.sort()
    print('Сортировка: ')
    for i in arr:
        print(i)
except NameError:
    print('Вы ввели строку вместо числа')
except ValueError:
    print('Вы ввели отрицательное значение')
except ZeroDivisionError:
    print('Нельзя делить на ноль!!!!!!!!!!!!!!!!!!!!!!!!!!!')
