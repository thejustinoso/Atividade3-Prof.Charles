import random

num_sublistas = int(input('Digite a quantidade de sub-listas: '))
num_elementos = int(input('Digite a quantidade de elementos em cada sub-lista: '))

# Gera a lista principal com sub-listas contendo elementos aleatórios e logo após exibe a lista gerada
lista_principal = [[random.randint(1, 100) for _ in range(num_elementos)] for _ in range(num_sublistas)]

print('\nLista gerada:')
for sublista in lista_principal:
    print(sublista)

# Calcula e logo após exibe a lista transposta
transposta = [[lista_principal[j][i] for j in range(num_sublistas)] for i in range(num_elementos)]

print('\nLista transposta:')
for linha in transposta:
    print(linha)
    
