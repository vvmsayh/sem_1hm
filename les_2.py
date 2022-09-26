#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) =
#  ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x=int(input("введите значение x: "))
y=int(input("введите значение y: "))
z=int(input("введите значение z: "))
left = not (x or y or z)
right = not x and not y and not z
print(left == right)