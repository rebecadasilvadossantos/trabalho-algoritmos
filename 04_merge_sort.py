# Merge Sort
# Vantagem: O(n log n) garantido.
# Desvantagem: utiliza memória extra proporcional ao tamanho da lista.
import random

def merge_sort(lista):
    if len(lista) <= 1:
        return lista.copy()
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i]); i += 1
        else:
            resultado.append(direita[j]); j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(merge_sort(dados))
