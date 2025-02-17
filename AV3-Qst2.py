import random
import itertools

n = int(input("Digite a quantidade de números (entre 7 e 60): "))
if 7 <= n <= 60:
  break
  print("Valor inválido! Digite um número entre 7 e 60.")
else:
    
# Gera lista de números escolhidos (números aleatórios entre 1 e 60, sem repetição)
numeros_escolhidos = random.sample(range(1, 61), n)
numeros_escolhidos.sort()

