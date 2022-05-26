# Для быстрого создания списков
list = []

for i in range(1, 101):
    #if(i%2 == 0):
        list.append(i);

print(list)

list = [i for i in range(1, 101)]  # Строки 4-6 можно записать так

list = [i for i in range(1, 101) if i % 2 ==0]  # то же самое (строка 10) с учётом условия чётности
print (list)

list = [(i, i) for i in range(1, 101) if i % 2 ==0]  # подключаем кортежи - на выходе список кортежей
print (list)

def f(x):
    return x**3
list = [(i, f(i)) for i in range(1, 101) if i % 2 ==0] # добавляем в ту же запись функцию
print(list)