## Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.

idade = int(input("Qual a sua idade?: "))
if idade < 18:
  autorizacao = input("Tem autorização dos pais?(S/N): ")
  if autorizacao == 'N':
    print("Permissão negada")
    exit(0)
print("Permissão concedida")