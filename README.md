# Grafos2_Exercises_LeetCode

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2063462 |  Samuel Alves Silva |
| 20/0024949  |  Matheus Ferreira Diogo |

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 1 média) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Grafos 2) da disciplina. 

## Screenshots

### [2192 - Média](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)
Utilizamos ordenação topológica com BFS para processar os nós em ordem e propagar ancestrais de cada nó para seus vizinhos. Cada nó mantém um conjunto de ancestrais, que é atualizado a partir dos ancestrais de seus predecessores mais o próprio predecessor.

![785](/assets/2192.PNG)

### [1579 - Difícil](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/)
A ideia principal é usar Union-Find (Disjoint Set Union) para manter o controle dos componentes conectados tanto para Alice quanto para Bob, e priorizar as arestas do tipo 3, pois elas são úteis para ambos.

![785](/assets/1579.png)


### [847 - Difícil](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
Utilizamos BFS com estado (nó atual, máscara de visitados) para explorar todos os caminhos possíveis enquanto rastreamos quais nós já foram visitados. A busca termina ao encontrar o menor caminho em que todos os bits da máscara estejam ativados, ou seja, todos os nós foram visitados.

![785](/assets/847.png)



##Link para vídeo da apresentação:


## Instalação 
**Linguagem**: Python<br>

## Outros 
...
