Number = int(input("Input a 3-digit number: "))
Sum = int(Number//100 + Number//10%10 + Number%10)

print(Sum, "(", Number//100, "+", Number//10%10, "+", Number%10, ")")
