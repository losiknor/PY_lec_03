# def sum(x, y):
#     return x+y

# строки 1-2 можно записать так --->
sum = lambda x, y: x+y

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    return op(a, b)

calc(mylt, 4, 5)

calc(sum, 4, 5)
calc(lambda x, y: x+y, 4, 5) # можно минуя переменную сразу аргументом функции ставить запись lammbda
