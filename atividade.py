notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
media = sum(notas) / 4

if media >= 9: conceito = 'A'
elif media >= 7.5: conceito = 'B'
elif media >= 6: conceito = 'C'
elif media >= 4: conceito = 'D'
else: conceito = 'E'

status = "APROVADO" if conceito in 'ABC' else "REPROVADO"

print(f"\nNotas: {notas}")
print(f"Média: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")