import numpy as np
from cpmpy import *


def solve_8_queens():
    # 1. Definição do tamanho do tabuleiro
    N = 8
    
    # 2. Definição das Variáveis de Decisão
    # 'queens' é um array de N variáveis, onde queens[i] representa a coluna
    # da rainha na linha i. O domínio é de 0 a N-1.
    queens = intvar(0, N - 1, shape=N, name="Q")
    
    # 3. Definição das Restrições
    constraints = []
    
    # Restrição 1: Todas as rainhas em colunas diferentes (garantindo linha e coluna únicas)
    # Já que cada elemento de 'queens' é uma linha diferente,
    # esta restrição garante que todas as colunas sejam únicas.
    constraints += [AllDifferent(queens)]
    
    # Restrição 2: Nenhuma rainha na mesma diagonal principal (i - j)
    # A diagonal principal é constante quando (linha - coluna) é constante.
    # Como 'queens[i]' é a coluna, a expressão é (i - queens[i]).
    diag1 = [i - queens[i] for i in range(N)]
    constraints += [AllDifferent(diag1)]
    
    # Restrição 3: Nenhuma rainha na mesma diagonal secundária (i + j)
    # A diagonal secundária é constante quando (linha + coluna) é constante.
    # A expressão é (i + queens[i]).
    diag2 = [i + queens[i] for i in range(N)]
    constraints += [AllDifferent(diag2)]
    
    # 4. Criação do Modelo e Solução
    model = Model(constraints)
    
    if model.solve():
        print("✅ Solução encontrada para o Problema das 8 Rainhas:")
        
        # Obter a solução (colunas onde as rainhas estão)
        solucao_colunas = queens.value()
        
        # Exibir o tabuleiro
        tabuleiro = np.full((N, N), '□')
        for linha, coluna in enumerate(solucao_colunas):
            tabuleiro[linha, coluna] = '♕'
            
        # Imprimir de forma legível
        print("-" * (2 * N + 1))
        for linha in tabuleiro:
            print("|" + "|".join(linha) + "|")
        print("-" * (2 * N + 1))

    else:
        print("❌ Não foi encontrada solução.")

# Execução da função
solve_8_queens()