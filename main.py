import json
from functools import lru_cache
from typing import List, Dict, Tuple

#  Leitura do catálogo - Parte 1 

def carregar_cursos(caminho_json: str) -> List[Dict]:
    with open(caminho_json, "r", encoding="utf-8") as f:
        return json.load(f)

# Parte 2 - Exibir todos os cursos lidos do JSON, listando eles para o usuário.

def exibir_catalogo(cursos: List[Dict]):
    print("\n=== Catálogo dos Cursos Disponíveis ===")
    for c in cursos:
        print(
            f"{c['id']:>2}. {c['name']} ({c['hours']}h, impacto {c['impact']}) "
            f"- {c['category']}"
        )
    print("======================================")


#  Algoritmo Knapsack (Top-down Memo)

def knapsack_memo(cursos: List[Dict], capacidade: int) -> Tuple[int, List[Dict]]:
    n = len(cursos) 
    # Define o número de cursos (n)
    # A função receberá a lista de cursos e o tempo total disponível (a capacidade da mochila)

    @lru_cache(maxsize=None)
    def dp(i: int, w: int) -> int:

        # Iru_cache guarda os resultados de cada combinação

        if i == 0 or w == 0:
            return 0
        
        # Se não há cursos / ou não há tempo = o impacto é zero 

        curso = cursos[i - 1]
        wi = curso["hours"]
        vi = curso["impact"]

        # Será separado o curso atual e separado em seus dois atributos principais: peso e impacto 

        if wi > w:
            return dp(i - 1, w)
        
        # Se o tempo restante não cauber, não podemos escolher. 

        return max(dp(i - 1, w), vi + dp(i - 1, w - wi))

        # O problema da mochila é resolvido aqui, onde é comparado as duas situações. Isso permite a garantia do resultado "ótimo".
    
    valor_otimo = dp(n, capacidade)

    # reconstrução
    selecionados = []
    i, w = n, capacidade
    while i > 0 and w > 0:
        if dp(i, w) != dp(i - 1, w):
            curso = cursos[i - 1]
            selecionados.append(curso)
            w -= curso["hours"]
        i -= 1

        # Essa parte do algoritmo reconstrói a lista de cursos escolhidos, andando de trás pra frente. Se o valor mudou no dp(i, w) e no dp(i-1, w), significa que esse curso foi escolhido. 

    selecionados.reverse()
    return valor_otimo, selecionados

    # No fim, a lista é invertida para manter na ordem original. 

#  Algoritmo Knapsack (Bottom-up Tab)

def knapsack_tab(cursos: List[Dict], capacidade: int) -> Tuple[int, List[Dict]]:
    n = len(cursos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    # Aqui criamos uma tabela (matriz) com n + 1 linhas (cursos) e capacidade + 1 colunas (horas)

    for i in range(1, n + 1):
        wi = cursos[i - 1]["hours"]
        vi = cursos[i - 1]["impact"]
        for w in range(capacidade + 1): 

            # Percorre todos os cursos (i) e todas as capacidades (w), preenchendo a tabala passa a passo.

            if wi > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], vi + dp[i - 1][w - wi])

                # A lógica é a seguite: se o curso não cabe, ele copia o valor de cima

                # Se cabe, ele compara "pegar" ou "não pegar" e guardar o maior.

    valor_otimo = dp[n][capacidade]

    # Aqui é o impacto máximo possível. 

    # reconstrução
    selecionados = []
    i, w = n, capacidade
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            curso = cursos[i - 1]
            selecionados.append(curso)
            w -= curso["hours"]
        i -= 1

    selecionados.reverse()
    return valor_otimo, selecionados

# Na reconstrução, ocorre o mesmo processo do top-down, percorrendo de baixo para cima verificando quais cursos foram escolidos. 

#  Execução principal

def main():
    caminho_json = "courses_reskilling.json"  
    cursos = carregar_cursos(caminho_json)
    exibir_catalogo(cursos)

    try:
        capacidade = int(input("\nColoque seu tempo disponível em horas: "))
        if capacidade <= 0:
            raise ValueError
    except ValueError:
        print("Entrada inválida. Use um número inteiro positivo.")
        return
    
    # Até aqui, o algoritmo fará duas ações como: ler o arquivo JSON e converter o valor digitado do usuário para inteiro 

    print("\nExecutando algoritmo com Memoização...")
    valor_memo, escolhidos_memo = knapsack_memo(cursos, capacidade)

    print("Executando algoritmo com Tabulação...")
    valor_tab, escolhidos_tab = knapsack_tab(cursos, capacidade)

    # Aqui é onde os dois algoritmos são executados. A memoização resolve o problema de forma recursiva e a tabulação de forma iterativa. 

    print("\n=== Resultado Final ===")
    print(f"Tempo disponível: {capacidade}h")
    print(f"Valor máximo (Impacto total): {valor_tab}")

    print("\nCursos recomendados:")
    for c in escolhidos_tab:
        print(f"- {c['name']} ({c['hours']}h, impacto {c['impact']})")

        # Os cursos escolhidos representam a melhor combinação possível, ou seja, o conjunto que oferece o maior impacto dentro do tempo limitado do usuário. 

    # Comparação final
    conjuntos_iguais = {c["id"] for c in escolhidos_memo} == {c["id"] for c in escolhidos_tab}
    if valor_memo == valor_tab and conjuntos_iguais:
        print("\nVerificação: Ambos os métodos retornaram o mesmo resultado!")
    else:
        print("\nVerificação: Resultados diferentes!")

        # Essa parte comprova o uso de ambos os métodos. Se o resultado foi o mesmo, sabemos que a nossa implementação está correta.


if __name__ == "__main__":
    main()

# Observação final:
# Os dois métodos (memoização e tabulação) devem sempre gerar o mesmo valor ótimo e a mesma lista de cursos, já que ambos seguem a mesma lógica do Problema da Mochila 0/1. Diferenças só ocorreriam em casos de dados inválidos no JSON, alteração incorreta da ordem dos cursos ou erro na lógica de reconstrução. No fluxo normal, o programa finaliza exibindo o impacto máximo atingível dentro do tempo disponível e confirmando a equivalência entre as duas abordagens.
