# Tabela Classificativa

O problema consiste em construir uma tabela em que dado uma lista de equipas 
com o seu nome, número de vitórias, empates, derrotas, golos marcados e golos 
sofridos, a tua tarefa é criar uma tabela classificativa, ordenada por ordem 
decrescente de pontos (3 pontos por vitória, 1 por empate e 0 por derrota). Caso 
tenham o mesmo número de pontos, as equipas devem vir por ordem 
decrescente do goal average (diferença entre número de golos marcados e 
sofridos). Caso o empate subsista, devem vir por ordem alfabética crescente do 
nome.

Como entrada temos um número N que pode tomar valor de 1 a 20, indicando 
a quantidade de equipas a considerar. Segue-se a descrição das equipas uma por 
linha, no formato NOME VITORIAS EMPATES DERROTAS GOLOS_MARCADOS 
GOLOS_SOFRIDOS. Os nomes das equipas não contêm espaços e têm um tamanho 
máximo de 20 letras. E como saída temos N linhas, listando as equipas pela 
ordem pedida, no formato NOME PONTOS GOAL_AVERAGE.

![image](https://user-images.githubusercontent.com/49438293/132480826-795301d5-1bbb-4ea4-9322-0b680f9592be.png)
