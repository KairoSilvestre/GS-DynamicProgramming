# Requalificação Profissional - Global Solution

### Integrantes:
* Guilherme Santos Nunes - RM558989
* Kaique Rodrigues Zaffarani - RM 556677 
* Kairo da Silva Silvestre de Carvalho - RM558288 

## Contextualização do problema
O cenário profissional atual, passa por uma tranformação sem precendentes, impulsionadas pela automação, inteligência artificial e novos modelos de negócios. Estimativas apontam que 65% dos trabalhadores precisarão se requalificar para manter a empregabilidade. 

Neste contexto, a tomada de decisão sobre quais competências desenvolver torna-se um problema de
otimização. Um profissional dispõe de recursos limitados (tempo e, por vezes, dinheiro) e precisa alocá-los da
forma mais eficiente para maximizar sua relevância no mercado

## Desafio - Dynamic Programming 
Esse projeto aplica Programação Dinâmica para resolver um problema real de requalificação profissional usando a versão 0/1 do problema de Mochila. 

O sistema implementa duas abordagens, como: 

* Memoização (Top-Down)
* Tabulação (Bottom-up)

Ao chegar no final do programa, ele compara os resultados para garantir que ambas cheguem ao mesmo resultado ótimo, além da lista de cursos. 

## Objetivo do Projeto
Simular, por meio de Programação Dinâmica, a escolha de cursos ideias para um profissional que precisa se requalificar para carreiras do futuro, mas possui tempo limitado. 

Cada curso possui:

* Hours (peso da mochila): quantas horas ele exige. 
* Impact (valor da mochila): o quanto ele agrega à carreira (1-100).

O problema é determinar: 
```
"Qual conjunto de cursos maximiza o impacto total sem ultrapassar o tempo disponível?"
```

Este é exatamente o Problema da Mochila 0/1, onde cada curso pode seer escolhido uma única vez. 
 
## Leitura do catálogo de cursos 

O programa lê o arquivo courses_reskilling.json, que funciona como um banco de dados contendo todos os cursos, suas horas, impacto e categorias. Esses JSON pode ser modificado sem alterar o código. 
## Entrada do usuário 

O usuário informa quantas horas tem disponíveis. Esse valor é a capacidade da mochila. 
## Execução de dois algoritmos de Programação Dinâmica.

### Memoização (Top-Down)

* Usa recursão e chace (@Iru_cache) para evitar cálculos repetidos.
* Resolve a recorrência da mochila partindo do problema maior e quebrando em subproblemas menores. 

### Tabulação (Bottom-Up)

* Constrói uma tabela 2D onde cada posição representa o melhor impacto possível para um número específico de cursos e horas disponíveis. 
* Resolve de forma totalmente iterativa.

Ambos retornam: 

* O impacto total máximo.
* A lista de cursos escolhidos.

## Reconstrução dos cursos selecionados 

Após encontrar o melhor valor, o algoritmo faz o caminho inverso na tabela/recursão para descobrir quais cursos compõem a solução ótima. 

## Verificação final 
O programa confirma: 

* Se ambos os algoritmos tiveram o mesmo impacto total. 
* Se escolherem a mesma combinação de cursoos. 

Se sim:
```bash 
verificação: Ambos os métodos retornam o mesmo resultado!
```
## Como executar o Projeto 

### 1. Rodar programa
No terminal: 
```bash
python main.py
```    
### 2. Interação
O programa exibirá os cursos do catálogo e pedirá seu tempo disponível: 
```bash
Informe seu tempo disponível em horas: 180
```
Em seguida, executará os dois algoritmos e retornará: 

* O impacto total máximo. 
* A lista de cursos recomendados 
* A verificação final da consistência

O projeto termina executando as duas versões do algoritmo, apresentando ao usuário o impacto máximo e os cursos ideais, e confirmando que ambas as abordagens chegam ao mesmo resultado. Isso encerra o ciclo garantindo precisão e consistência na solução.
