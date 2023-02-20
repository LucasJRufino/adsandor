##Escreva um programa que peça ao usuário inserir três números e, em seguida, determine se um dos três números é maior que a soma dos outros dois.
x = int(input("Insira o primeiro número"))
y = int(input("Insira o segundo número"))
z = int(input("Insira o terceiro número"))

if x > y + z or y > x + z or z > x + y:
  print("Um dos números é maior que a soma dos outros")
else:
  print("Nenhum dos números é maior que a soma dos outros")