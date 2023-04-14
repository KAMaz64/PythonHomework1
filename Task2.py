# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

Number = int(input("Input a 3-digit number: "))
Sum = int(Number//100 + Number//10%10 + Number%10)

print(Sum, "(", Number//100, "+", Number//10%10, "+", Number%10, ")")
