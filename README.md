# Tabela Classificativa / Scorecard

O problema consiste em construir uma tabela em que dado uma lista de equipas com o seu nome, número de vitórias, empates, derrotas, golos marcados e golos sofridos, a tarefa passa por criar uma tabela classificativa, ordenada por ordem decrescente de pontos (3 pontos por vitória, 1 por empate e 0 por derrota). Caso mais de uma equipa tenham o mesmo número de pontos, as equipas devem ser classificadas por ordem decrescente do goal average (diferença entre número de golos marcados e sofridos). Caso o empate subsista, devem vir por ordem alfabética crescente do nome.

Como entrada temos um número N que pode tomar valor de 1 a 20, indicando a quantidade de equipas a considerar. Segue-se a descrição das equipas uma por linha, no formato NOME VITORIAS EMPATES DERROTAS GOLOS_MARCADOS GOLOS_SOFRIDOS. Os nomes das equipas não contêm espaços e têm um tamanho máximo de 20 letras. E como saída temos N linhas, listando as equipas pela ordem pedida, no formato NOME PONTOS GOAL_AVERAGE.

---

The problem consists in building a table where given a list of teams with their name, number of wins, draws, losses, goals scored and goals conceded, the task is to create a league table, sorted by descending order of points (3 points for a win, 1 for a draw and 0 for a loss). If more than one team has the same number of points, the teams should be ranked in descending order of goal average (difference between the number of goals scored and conceded). If the tie subsists, they should come in ascending alphabetical order of name.

As input we have a number N that can take value from 1 to 20, indicating the number of teams to consider. Then follows the description of the teams one per line, in the format NAME WIN WIN WIN DEFEATS GOALS_MARKED GOALS_SOFFERED. The team names contain no spaces and have a maximum length of 20 letters. And as output we have N lines, listing the teams in the order requested, in the format NAME POINTS GOAL_AVERAGE.


## Screenshot

![image](https://user-images.githubusercontent.com/49438293/132480826-795301d5-1bbb-4ea4-9322-0b680f9592be.png)
