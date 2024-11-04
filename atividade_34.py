# Ler uma lista de 5 números inteiros e 
# mostre cada número juntamente com a 
# sua posição na lista

numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
    
for i, numero in enumerate(numeros):
    print(f"Número na posição {i}: {numero}")
