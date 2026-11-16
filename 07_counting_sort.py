# Counting Sort
# Vantagem: O(n + k), rápido quando o intervalo de valores é pequeno.
# Desvantagem: memória depende do intervalo entre o menor e o maior valor.
import random

def counting_sort(lista):
    if not lista:
        return []
    minimo, maximo = min(lista), max(lista)
    contagens = [0] * (maximo - minimo + 1)
    for valor in lista:
        contagens[valor - minimo] += 1
    resultado = []
    for indice, quantidade in enumerate(contagens):
        resultado.extend([indice + minimo] * quantidade)
    return resultado

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(counting_sort(dados))
