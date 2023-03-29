from typing import Dict, List

numero_equipas = int(input("Digite a quantidade de equipas >> "))

if 1 <= numero_equipas <= 20:

    lista_equipas: List[Dict[str, str]] = []  # lista de dicionarios

    for i in range(numero_equipas):

        nome = input("\nNome da equipa >> ")

        while len(nome) > 20 or " " in nome:  # se tamanho do nome da equipa for maior que 20 ou conter espacos
            nome = input("\nNome inválido, máximo 20 letras!\nNome da equipa >> ")

        equipa = {
            'nome': nome,
            'vitorias': input("Numero de vitorias >> "),
            'empates': input("Numero de empates >> "),
            'derrotas': input("Numero de derrotas >> "),
            'golosmarcados': input("Golos Marcados >> "),
            'golossofridos': input("Golos Sofridos >> ")}

        equipa['pontos'] = (int((equipa['vitorias'])) * 3 + int((equipa['empates'])))
        equipa['diferencagoal'] = (int((equipa['golosmarcados'])) - int((equipa['golossofridos'])))

        lista_equipas.append(equipa)  # adicionar equipa a lista
        print("===================================================================")

    lista_equipas = sorted(lista_equipas, key=lambda item: (item['nome']))  # ordenar a lista por ordem alfabetica

    lista_equipas = sorted(lista_equipas, key=lambda item: (item['pontos'], item['diferencagoal']),
                           reverse=True)  # ordenar a lista por pontos ou diferanca de golos

    for equipa in lista_equipas:
        print(equipa['nome'], equipa['pontos'], equipa['diferencagoal'], end=' ')
        print()
