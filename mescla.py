import math
import random
import time
import heapq as fila_prioridade

def ordenacao_raiz_quadrada_heap(vetor):
    """
    Ordena o vetor usando a técnica de ordenação por raiz quadrada com heap.
    """
    tamanho_vetor = len(vetor)
    tamanho_parte = int(math.sqrt(tamanho_vetor))

    # Dividir o vetor em partes
    partes = [vetor[i:i+tamanho_parte] for i in range(0, tamanho_vetor, tamanho_parte)]

    # Transformar cada parte em um Max Heap
    for i in range(len(partes)):
        fila_prioridade._heapify_max(partes[i])

    vetor_ordenado = []
    while any(partes):
        # Encontrar o maior elemento de cada parte
        maiores_elementos = [parte[0] for parte in partes if parte]

        # Pegar o maior elemento entre e1 . . . ek e inseri-lo no vetor solução
        maior = max(maiores_elementos)
        vetor_ordenado.append(maior)
        # Descartar o maior elemento da parte correspondente
        for parte in partes:
            if parte and parte[0] == maior:
                fila_prioridade._heappop_max(parte)
                break

    return vetor_ordenado[::-1]


def ordenacao_raiz_quadrada(vetor):
    """
    Ordena o vetor usando a técnica de ordenação por raiz quadrada.
    """
    tamanho_vetor = len(vetor)
    tamanho_parte = int(math.sqrt(tamanho_vetor))

    # Dividir o vetor em partes
    partes = [vetor[i:i+tamanho_parte] for i in range(0, tamanho_vetor, tamanho_parte)]

    # Ordenar cada parte
    for i in range(len(partes)):
        partes[i] = sorted(partes[i])

    vetor_ordenado = []
    while any(partes):
        # Encontrar o maior elemento de cada parte
        maiores_elementos = [parte[-1] for parte in partes if parte]

        # Pegar o maior elemento entre e1 . . . ek e inseri-lo no vetor solução
        maior = max(maiores_elementos)
        vetor_ordenado.append(maior)
        # Descartar o maior elemento da parte correspondente
        for parte in partes:
            if parte and parte[-1] == maior:
                parte.pop()
                break
        
    return vetor_ordenado[::-1]


# Tamanhos de entrada para teste
tamanhos_entrada = [10**8]  # Aumente o ta   manho da entrada gradualmente
num_repeticoes = 1  # Número de repetições para calcular a média

for n in tamanhos_entrada:
    tempos = []
    tempos2 = []
    for i in range(num_repeticoes):
        # Gera lista aleatória de tamanho n
        V = [random.randint(1, 1000000) for _ in range(n)]

        # Mede o tempo de execução da função com Bubble Sort
        inicio = time.time()
        ordenacao_raiz_quadrada(V.copy())  # Use uma cópia para não modificar a lista original
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        print(f"\n  Execução quadrática com Quadrática {n}: {tempo_execucao:.11f} segundos")

        # Mede o tempo de execução da função com Heap
        inicio2 = time.time()
        ordenacao_raiz_quadrada_heap(V.copy())  # Use uma cópia para não modificar a lista original
        fim2 = time.time()
        tempo_execucao2 = fim2 - inicio2
        tempos2.append(tempo_execucao2)
        print(f"\n  Execução com Heap {n}: {tempo_execucao2:.11f} segundos")
