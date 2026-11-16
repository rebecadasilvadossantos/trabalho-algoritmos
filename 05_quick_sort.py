# Quick Sort
# Vantagem: costuma ser rápido na prática.
# Desvantagem: pode chegar a O(n²) em partições muito desequilibradas.
import random

def quick_sort(lista):
    a = lista.copy()
    def ordenar(inicio, fim):
        if inicio >= fim:
            return
        p = random.randint(inicio, fim)
        a[p], a[fim] = a[fim], a[p]
        pivo = a[fim]
        menor = inicio
        for atual in range(inicio, fim):
            if a[atual] <= pivo:
                a[menor], a[atual] = a[atual], a[menor]
                menor += 1
        a[menor], a[fim] = a[fim], a[menor]
        ordenar(inicio, menor - 1)
        ordenar(menor + 1, fim)
    ordenar(0, len(a) - 1)
    return a

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(quick_sort(dados))
