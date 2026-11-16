# Selection Sort
# Vantagem: simples e usa pouca memória extra.
# Desvantagem: O(n²), mesmo quando a lista já está ordenada.
import random

def selection_sort(lista):
    a = lista.copy()
    for i in range(len(a) - 1):
        menor = i
        for j in range(i + 1, len(a)):
            if a[j] < a[menor]:
                menor = j
        a[i], a[menor] = a[menor], a[i]
    return a

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(selection_sort(dados))  # Pode demorar bastante com 100.000 elementos.
