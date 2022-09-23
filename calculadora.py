altura = float(input('Sua altura em cm: '))
peso = float(input('Seu peso em kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print(f'Seu IMC é de {round(IMC, 1)} e é classificado como Magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de {round(IMC, 1)}, e é classificado com Normal')

elif IMC >= 25 and IMC < 29.9:
    print(f'Seu IMC é de {round(IMC, 1)}, e é classificado com Sobrepeso')

elif IMC >= 30 and IMC < 34.9:
    print(f'Seu IMC é de {round(IMC, 1)}, e é classificado com Obesidade grau I')

elif IMC >= 35 and IMC < 39.9:
    print(f'Seu IMC é de {round(IMC, 1)}, e é classificado com Obesidade grau II')

elif IMC < 40:
    print(f'Seu IMC é de {round(IMC, 1)}, e é classificado com Obesidade grau III')

# Menor que 18,5 Magreza
# 18,5 a 24,9    Normal
# 25 a 29,9	     Sobrepeso
# 30 a 34,9	     Obesidade grau I
# 35 a 39,9	     Obesidade grau II
# Maior que 40	 Obesidade grau III
