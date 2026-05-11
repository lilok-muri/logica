senha = input("digite uma senha")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

caracteres_especiais = "!@#$%*(+=-_[]{}~^/?"



for caracter in senha:
    if caracter.isupper():
        tem_maiuscula = True

erros = []
if not tem_maiuscula:
    erros.append("falta caracter maiusculo!")

if len(erros) == 0:
    print("senha forte!")
else:
    print("senha invalida!")
    print("Requisitos ausentes")

    for erro in erros:
        print("- " + erro)