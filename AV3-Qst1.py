import random

num_sublistas = int(input('Digite a quantidade de sub-listas: '))
num_elementos = int(input('Digite a quantidade de elementos em cada sub-lista: '))

lista_principal = [[random.randint(1, 100) for _ in range(num_elementos)] for _ in range(num_sublistas)]
