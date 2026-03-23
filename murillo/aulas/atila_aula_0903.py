import math
base = float(input("digite o valor da base:"))
potencia = float(input("digite o valor da potencia"))
resultado = pow (base, potencia)
print(resultado)
# print(pow(2,4))

# raiz = math.sqrt(16)
# print(raiz)
raiz = float(input("digite o valor para a raiz"))
resultado = math.sqrt(raiz)
print(resultado)



raio=float(input("Digite o valor do raio"))
altura=float(input("Digite o valor da altura"))

volume = 3.14159 * pow(raio, 2) * altura

print(f"volume ={volume:.4f}")

tempo = float(input("digite o valor do tempo"""))
velocidade = float(input('digite o valor da velocidade'))
preco = float(input("digite o consumo por litro"))
km = float(input("Digite o preco do litro"))


distancia = tempo * velocidade
litros= distancia / km
valor = litros* preco


print(f"tempo gasto:{tempo:.1f}")
print(f"velocidade ; {velocidade:.1f}")
print(f"distancia percorrida{distancia:.1f}")
print(f"litros usados{litros:.1f}")
print(f"valor gasto na viagem R$: {valor:.1f}")