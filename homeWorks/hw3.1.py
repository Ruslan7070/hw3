class calculator():
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, other):
        return other + self.argument

    def __sub__(self, other):
        return other - self.argument

    def __mul__(self, other):
        return other * self.argument

    def __truediv__(self, other):
        return other / self.argument

a = calculator(5)
b = calculator(10)
c = calculator.__add__(a,b)
e = calculator.__sub__(b,a)
d = calculator.__mul__(a,b)
f = calculator.__truediv__(b,a)
print(f'a + b = {c}')
print(f'b - a = {e}')
print(f'a * b = {d}')
print(f'b / a = {f}')