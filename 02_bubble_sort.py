# Bubble Sort
# Vantagem: fácil de entender e termina cedo se a lista já estiver ordenada.
# Desvantagem: O(n²) no caso médio e no pior caso.
import random

def bubble_sort(lista):
    a = lista.copy()
    for i in range(len(a)):
        trocou = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                trocou = True
        if not trocou:
            break
    return a

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(bubble_sort(dados))  # Pode demorar bastante com 100.000 elementos.
