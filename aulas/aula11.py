print("-"* 20)
print("calculo do IRRF")
print("-" * 20)

resposta = True

while resposta == True:
    try:
        sal_bruto = float(input("digite seu salario bruto"))

        if 2428.81 < sal_bruto <= 2826.65:
            irrf = 0.075
        elif 2826.66 < sal_bruto <= 3751.05:
            irrf = 0.015
        elif 3751 < sal_bruto <= 4664.68:
            irrf = 0.225
        else:
            irrf = 0.275

        print(f"{sal_bruto} com {irrf}% = R$ {sal_bruto - (sal_bruto * irrf):.2f}")

    except ValueError:
        print("valor do salario invalido!")

        resposta =  input("deseja realizar outro calculo (S/N)")
        if resposta == 'S' or resposta == 's':
            resposta = True
        else:
            resposta = False


