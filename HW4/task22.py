# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке 
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
l_1 = list()
l_2 = list()
el = 0
while el < n:
    number = int(input("Введите значение элемента для первого множества: "))
    l_1.append(number)
    el += 1
num = 0
print(l_1)
m = int(input("Введите количество элементов второго множества: "))
while num < m:
    number = int(input("Введите значение элемента для второго множества: "))
    l_2.append(number)
    num += 1
print(l_2)
t_1 = set(l_1)
t_2 = set(l_2)
i = t_1.intersection(t_2)
list_i = list(i)
list_i.sort()
print(list_i)