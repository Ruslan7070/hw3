class Bank:

    def __init__(self,name,balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        add_balanse = float(input("Введите сумму которую хотите добавить на счет:"))
        self._balanse += add_balanse
        print(f'Ваш текущий баланс: {self._balanse}')
git
    def _kill(self):
        self._balanse = 0
        print(f"Ваш баланс обнулен: {self._balanse}")

    def __jackpot(self):
        self._balanse *=10
        print(f"Ваш баланс увеличен в 10 раз!\n"
              f"Текущий баланс:{self._balanse}")

    def copy_balanse(self,user):
        self._balanse += user._balanse
        print(f"Ваш новый баланс после добавления:{self._balanse}")


a1= Bank('Beka',100)
a2 = Bank('Rus',200)

a1.moneyX()
a1._kill()
a1.copy_balanse(a2)

print(f'Баланс Beka:{a1._balanse}')
print(f'Баланс Rus: {a2._balanse}')
