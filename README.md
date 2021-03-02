# Graph Model for Solving a Travelling Salesman Problem (TSP)

Final project for master's discipline Algorithm Analysis and Data Structures - Federal University of Lavras (UFLA)

## Problem Description (PT-BR)

Carlos é um estudante de Administração que ama viajar nas férias. Sempre quando viaja para uma cidade pela primeira vez, Carlos aluga um carro e começa a fazer pequenos passeios por locais próximos onde está. No entanto, seu deslocamento segue uma mania curiosa. Carlos posiciona todos os locais que quer visitar como se fossem pontos no plano cartesiano. Na sequência, ele começa a visitar o local que está mais à esquerda do plano, e segue caminhando da esquerda para a direita, até chegar no ponto que está mais no extremo direito. Daí, Carlos vai voltando da direita para a esquerda, até encontrar o ponto de origem (o que está no lado extremo esquerdo).

No entanto, Carlos não quer fazer esse tour deliberadamente: ele quer encontrar o tour que visite todos os pontos, com o menor custo de deslocamento possível. 

## Goal

- Discover the tour linking all points with the smallest movement cost possible.

## Time-Complexity Requirement

- Let `n` the number of points in the cartesian plan, the algorithm must run under `O(n²)` steps.

## I/O Specification

- **Input:** The fisrt line has the number of points. Each following line has the 2D coordinate of each point.

- **Output:** The movement cost, rounded by 2 decimal places.

-----

### Example 1

#### Input 

```
3
1 1
2 3
3 1
```

#### Output

```
6.47
```

-----

### Example 2

#### Input

```
4
1 1
2 3
3 1
4 2
```

#### Output

```
7.89
```

-----

### Example 3

#### Input

```
7
0 6
1 0
2 3
5 4
6 1
7 5
8 2
```

#### Output

```
25.58
```
