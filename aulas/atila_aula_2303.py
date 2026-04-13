consumo = float(input("Digite o consumo em m3: "))

if consumo <= 10:
    valor = 7.59
elif consumo <= 20:
    valor = consumo * 1.31
elif consumo <= 30:
    valor = consumo * 4.64
elif consumo <= 50:
    valor = consumo * 6.62
else:
    valor = consumo * 7.31

print(f"Valor da conta: R$ {valor:.2f}")

#-----------------------------------------------------------------------------------------------------------------------------------------


peso = float(input("Peso em KiloGramas: "))
altura = float(input("Altura em Metros: "))
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau")
elif imc < 40:
    print("Obesidade Grau severa")
else:
    print("Obesidade Grau mórbida")

    #------------------------------------------------------------------------------------------------------------------------------------

a = float(input("Valor A: "))
b = float(input("Valor B: "))
c = float(input("Valor C: "))

# Verifica se forma um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores não formam um triângulo.")

    #-------------------------------------------------------------------------------------------------------------------------------------

