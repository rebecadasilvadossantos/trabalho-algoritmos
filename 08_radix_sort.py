# Radix Sort
# Vantagem: ordena dígito por dígito, sem comparar pares de elementos.
# Desvantagem: depende da quantidade de dígitos e usa memória auxiliar.
import random

def radix_sort(lista):
    if not lista:
        return []
    def positivos(valores):
        valores = valores.copy()
        maior = max(valores)
        exp = 1
        while maior // exp > 0:
            saida = [0] * len(valores)
            contagem = [0] * 10
            for v in valores:
                contagem[(v // exp) % 10] += 1
            for i in range(1, 10):
                contagem[i] += contagem[i - 1]
            for v in reversed(valores):
                digito = (v // exp) % 10
                contagem[digito] -= 1
                saida[contagem[digito]] = v
            valores = saida
            exp *= 10
        return valores
    negativos = [-v for v in lista if v < 0]
    nao_negativos = [v for v in lista if v >= 0]
    negativos = [-v for v in reversed(positivos(negativos))]
    return negativos + positivos(nao_negativos)

if __name__ == "__main__":
    dados = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    print(radix_sort(dados))
