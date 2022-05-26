li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x:x+10, li))
print(li)

data = list(map(int,input().split()))
print(data)

# можно не выводить в list а сразу считывать:
for e in data:
    print(e)

# тот же вариант, но без ввода с клавиатуры:
data = list(map(int,'12 56 89'.split()))
print(data)
for e in data:
    print(e)

print('------------')

for e in data:
    print(e)