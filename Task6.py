# coding=utf-8

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

Number = int(input("Input a 6-digit ticket number: "))
LeftPart = Number//1000
RightPart = Number%1000
LeftSum = LeftPart//100+(LeftPart//10)%10+LeftPart%10
RightSum = RightPart//100+(RightPart//10)%10+RightPart%10

if 100000<=Number<=999999:
    if LeftSum == RightSum:
        print("yes")
    else:
        print("no")
else:
    print("Input data error")