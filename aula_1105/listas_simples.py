#lista = strings
# lista numerica = int/float
# inserção = append
# remoçao = remove
# mediçao = len

#lista simples
compras = ["leite", "manteiga", "farinha"]
print(compras)


#numeros inteiros/lista numerica
numeros = int(print("1", "2"))


#numeros quabrados/lista numerica
numeros_quebrados = float(print("2.4", "3.3"))


#inserção/adicionar
nomes = ["murillo", "henry", "luiz"]
nomes.append("felipe")
print(nomes)


#Remoção
nomes_remover = ["lilok", "henryford", "white777"]
nomes_remover.remove("henryford")
print(nomes_remover)


# contagem
mediçao = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]
print(len(mediçao))


# media/ sum= somar os itens de um iterável (como listas, tuplas ou sets).
notas =[8.0, 7.5, 6.0, 4.5]

media = sum(notas) / len(notas)
print(media)


#if
estoque = ["mouse", "teclado", "monitor"]

produto =  input("digite o produto")

if produto in estoque:
    print("temos")
else:
    print("fora de estoque")


#cadastro de frutas/ codificação conjunta
frutas = []

for i in range(5):
    fruta = input("digite uma fruta:")
    frutas.append(fruta)

print("\nlista de frutas")

for fruta in frutas:
    print(fruta)


#codificação conjunta/média da turma

notas_turma = []
for i in range(4):
    nota = float(input("digite uma nota"))
    notas_turma.append(nota)

medias = sum(notas_turma) / len(notas_turma)
print(f"Média da turma: {medias:.2f}")