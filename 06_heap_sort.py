# Heap Sort
# Vantagem: O(n log n) mesmo no pior caso.
# Desvantagem: não é estável e pode ser menos rápido na prática que Quick Sort.
import random

def heap_sort(lista):
    a = lista.copy()
    n = len(a)
    def descer(tamanho, raiz):
        maior = raiz
        esq, dir_ = 2 * raiz + 1, 2 * raiz + 2
        if esq < tamanho and a[esq] > a[maior]:
            maior = esq
        if dir_ < tamanho and a[dir_] > a[maior]:
            maior = dir_
        if maior != raiz:
            a[raiz], a[maior] = a[maior], a[raiz]
            descer(tamanho, maior)
    for i in range(n // 2 - 1, -1, -1):
        descer(n, i)
    for fim in range(n - 1, 0, -1):
        a[0], a[fim] = a[fim], a[0]
        descer(fim, 0)
    return a

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(heap_sort(dados))
