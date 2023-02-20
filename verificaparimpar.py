## Escreva um código que verifique se um número é par ou divisível por 3.

num = int(input("Insira o número: "))

if num%2 > 0:
  print("O número é impar")
  if num%3 == 0:
    print("O número é divisível por 3")
else:
  print("O número é par")