## Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine se o aluno passou ou não.
## Um aluno passa se a soma das notas for maior ou igual a 60 e nenhuma nota é menor que 40.

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

if nota1 < 40 or nota2 < 40 or nota1 + nota2 <= 60:
  print("Não passou")
else:
  print("Passou")
