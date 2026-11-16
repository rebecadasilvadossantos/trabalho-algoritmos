# Bucket Sort
# Vantagem: pode ser muito rápido quando os valores estão bem distribuídos.
# Desvantagem: depende da distribuição; baldes desequilibrados pioram o tempo.
import random

def bucket_sort(lista, quantidade_buckets=None):
    if len(lista) <= 1:
        return lista.copy()
    minimo, maximo = min(lista), max(lista)
    if minimo == maximo:
        return lista.copy()
    if quantidade_buckets is None:
        quantidade_buckets = len(lista)
    baldes = [[] for _ in range(quantidade_buckets)]
    intervalo = maximo - minimo + 1
    for valor in lista:
        indice = (valor - minimo) * quantidade_buckets // intervalo
        indice = min(indice, quantidade_buckets - 1)
        baldes[indice].append(valor)
    resultado = []
    for balde in baldes:
        balde.sort()  # Ordena os elementos de cada balde.
        resultado.extend(balde)
    return resultado

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(bucket_sort(dados))
