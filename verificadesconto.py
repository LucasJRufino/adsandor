## Criar um programa que verifica se uma pessoa tem desconto em um produto,
## baseado na idade e sua categoria (estudante, aposentado, etc.) e no dia da semana. (Use quantas categorias desejar)

idade = int(input("Qual a idade?"))
categoria = input("Qual a categoria?\nE - estudante\nS - Doador de Sangue\nG - Grávida\nN - Nenhum")
desconto = 0
if idade >= 60 or idade < 18:
  desconto += 10
15
match categoria:
  case "E":
    desconto += 10
    print("Estudante, desconto de '10%' aplicado")
  case "D":
    desconto += 15
    print("Doador de sangue, desconto de '15%' aplicado")
  case "G":
    desconto += 10
    print("Grávida, desconto de '10%' aplicado")
  case "N":
    print("Nenhum desconto adicional aplicado")
  case _:
    print("Categoria não válida inserida!")

print("Desconto total: ", desconto, "%")

