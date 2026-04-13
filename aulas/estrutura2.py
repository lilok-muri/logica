velocidade = float(input("Digite a velocidade em Km/h: "))
limite = 80

if velocidade > limite:
    excedeu = velocidade - limite
    multa = excedeu * 50
    print(f"Limite = {limite}Km/h")
    print(f"Excedeu {excedeu}Km/h")
    print(f"multa = {excedeu}Km/h * R$ 50,00")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite.")

    #------------------------------------------------------
    num1 = float(input("num1 = "))
num2 = float(input("num2 = "))
num3 = float(input("num3 = "))

numeros = [num1, num2, num3]
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / 3

print("**********")
print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"soma = {soma}")
print(f"media = {media}")
#-----------------------------------------------------------
distancia = float(input("Qual a distância da viagem em km? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da passagem será R$ {preco:.2f}")
#-----------------------------------------------------------
print("*" * 30)
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("*" * 30)
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")
print("*" * 30)

opcao = input("Qual grandeza deseja calcular? ")

if opcao == '1':
    r = float(input("Informe a Resistência (R): "))
    i = float(input("Informe a Corrente (I): "))
    u = r * i
    print(f"Tensão (U) = {u} V")
elif opcao == '2':
    u = float(input("Informe a Tensão (U): "))
    i = float(input("Informe a Corrente (I): "))
    r = u / i
    print(f"Resistência (R) = {r} Ω")
elif opcao == '3':
    u = float(input("Informe a Tensão (U): "))
    r = float(input("Informe a Resistência (R): "))
    i = u / r
    print(f"Corrente (I) = {i} A")
elif opcao == '4':
    print("Saindo...")
else:
    print("Opção inválida!")
 #------------------------------------------------------------
usuario = input("Usuário: ")
senha = input("Senha: ")

if (usuario == "atila" and senha == "12345") or (usuario == "olivi" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")
#------------------------------------------------------------
preco = float(input("Preço total da venda: R$ "))
print("1 - À vista (espécie) | 2 - Débito | 3 - Crédito | 4 - PIX")
forma = input("Forma de pagamento: ")

if forma == '1':
    final = preco * 0.90
elif forma == '2':
    final = preco * 0.95
elif forma == '3':
    final = preco * 0.97
elif forma == '4':
    final = preco * 0.925
else:
    final = preco
    print("Opção inválida! Sem desconto aplicado.")

print(f"Valor final a ser pago: R$ {final:.2f}")
#-----------------------------------------------------------
texto = input("Digite algo: ")

if texto.strip() == "":
    print("Dado inválido")
else:
    print(f"Você digitou: {texto}")
#-----------------------------------------------------------
entrada = input("Digite um número inteiro: ")

if entrada.strip() == "":
    print("Dado inválido")
else:
    try:
        numero = int(entrada)
        print(f"Número digitado: {numero}")
    except ValueError:
        print("Isso não é um número inteiro válido.")
#----------------------------------------------------------
litros = float(input("Litros vendidos: "))
tipo = input("Tipo (A-Álcool / G-Gasolina): ").upper()

preco_a = 2.89
preco_g = 4.95

if tipo == 'A':
    if litros <= 20:
        total = litros * (preco_a * 0.97)
    else:
        total = litros * (preco_a * 0.95)
    print(f"Valor a pagar: R$ {total:.2f}")
elif tipo == 'G':
    if litros <= 20:
        total = litros * (preco_g * 0.96)
    else:
        total = litros * (preco_g * 0.94)
    print(f"Valor a pagar: R$ {total:.2f}")
else:
    print("Tipo de combustível inválido.")
#------------------------------------------------------
lista_numeros = []

for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(n)

print("Os números digitados foram:", lista_numeros)
#-----------------------------------------------------
print("*" * 30)
num = int(input("Informe o número da tabuada: "))
print("*" * 30)

for i in range(1, 11):
    resultado = i * num
    print(f"{i} x {num} = {resultado}")
#------------------------------------------------------
for i in range(1, 101):
    print(i)
#------------------------------------------------------
import time

for contagem in range(10, -1, -1):
    print(contagem)

print("Ignição!")
#------------------------------------------------------
for i in range(1, 101):
    if i % 2 == 0:
        print(i)