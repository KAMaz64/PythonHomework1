# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 	Примеры/Тесты:
# 	3 2 4 -> yes
# 	3 2 1 -> no

print("Choco Bar of size MxN")
width_input = input("Input M: ")
length_input = input("Input N: ")
wanted_input = input("Input number of parts: ")

if width_input.isdigit() and length_input.isdigit() and wanted_input.isdigit():
    width = int(width_input)
    length = int(length_input)
    wanted = int(wanted_input)
else:
    print("Input data error")
    exit(1)

if wanted < width * length and (wanted % length == 0 or wanted % width == 0):
    print('yes')
else:
    print('no')