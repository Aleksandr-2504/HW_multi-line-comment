"""
# ДЗ №1. Задача 1:

# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)
"""
  
# Решение задачи 1

# первый вариант:

n = 100
res = (n // 100 + (n // 10) % 10 + n % 10)
print(res)

# второй вариант:
n = 123
res = 0
while n > 0:
  res += n % 10
  n = n // 10
print(res) 

# эталонное решение:
n = 123
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3
print("n = {} -> {} + {} + {} = {}".format(n, n1, n2, n3, res)) # шаблон "".format
print(f"n = {n} -> {n1} + {n2} + {n3} = {res}") # шаблон f-строки
