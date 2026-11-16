# Insertion Sort
# Vantagem: eficiente para listas pequenas ou quase ordenadas.
# Desvantagem: O(n²) no caso médio e no pior caso.
import random

def insertion_sort(lista):
    a = lista.copy()
    for i in range(1, len(a)):
        chave = a[i]
        j = i - 1
        while j >= 0 and a[j] > chave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = chave
    return a

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(insertion_sort(dados))  # Pode demorar bastante com 100.000 elementos.
