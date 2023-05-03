class Transactie():
    balance = 0
    def __init__(self, amount):
        self.amount = amount
        Transactie.balance += amount

test1 = Transactie(5)
print(Transactie.balance)
test1 = Transactie(8)
print(Transactie.balance)
test1 = Transactie(-6)
print(Transactie.balance)
test1 = Transactie(4)
print(Transactie.balance)
test1 = Transactie(10)
print(Transactie.balance)
test1 = Transactie(-12)
print(Transactie.balance)
test1 = Transactie(-9)
print(Transactie.balance)