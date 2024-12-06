def checarVitoria(tabuleiro, jogador, simbolo):
    # Verificando as condições de vitória
    if tabuleiro[0][0] == simbolo and tabuleiro[1][0] == simbolo and tabuleiro[2][0] == simbolo:  # Coluna 1
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[0][1] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][1] == simbolo:  # Coluna 2
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[0][2] == simbolo and tabuleiro[1][2] == simbolo and tabuleiro[2][2] == simbolo:  # Coluna 3
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[0][0] == simbolo and tabuleiro[0][1] == simbolo and tabuleiro[0][2] == simbolo:  # Linha 1
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[1][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[1][2] == simbolo:  # Linha 2
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[2][0] == simbolo and tabuleiro[2][1] == simbolo and tabuleiro[2][2] == simbolo:  # Linha 3
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:  # Diagonal principal
        print(f"{jogador} ganhou")
        return True
    elif tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:  # Diagonal secundária
        print(f"{jogador} ganhou")
        return True
    return False  # Se não houve vitória


def jogoDaVelha():
    #Imprime o estado inicial do tabuleiro
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Este é um jogo da velha!")
    print("Este é o estado inicial do tabuleiro:")

    for linha in tabuleiro:
        print(linha)

    #Recebe e guarda os nomes do Jogador1 e Jogador2
    jogador1 = input("Digite o nome do primeiro jogador: ")
    jogador2 = input("Digite o nome do segundo jogador: ")

    #Inicia o loop que roda até o jogo ser finalizado de alguma forma
    while True:
        # Loop criado pra controlar a jogada do Jogador 1
        while True:
            print(f"Vez de {jogador1} (X)")
            selecionarLinha = int(input("Escolha uma linha do tabuleiro para jogar (0-2): "))
            selecionarColuna = int(input("Escolha uma coluna do tabuleiro para jogar (0-2): "))

            #Condições criadas para checar se a jogada do Jogador1 é uma jogada válida

            if selecionarLinha > len(tabuleiro) - 1 or selecionarColuna > len(tabuleiro[0]) - 1:
                print("Jogada inválida, por favor jogue novamente.")
            elif tabuleiro[selecionarLinha][selecionarColuna] == 'X' or tabuleiro[selecionarLinha][selecionarColuna] == 'O':
                print("Posição já ocupada, escolha outra.")
            else:
                tabuleiro[selecionarLinha][selecionarColuna] = 'X'
                break  # Jogada válida, sai do loop do jogador 1

        #Imprime o tabuleiro novamente para, ou o resultado final, ou dar continuidade ao jogo
        for linha in tabuleiro:
            print(linha)

        #Condição que valida se o Jogador1 venceu a partida chamando a funcao checarVitoria

        if checarVitoria(tabuleiro, jogador1, 'X'):
            break  # Jogador1 venceu, o jogo termina

        # Loop criado pra controlar a jogada do Jogador 2
        while True:
            print(f"Vez de {jogador2} (O)")
            selecionarLinha = int(input("Escolha uma linha do tabuleiro para jogar (0-2): "))
            selecionarColuna = int(input("Escolha uma coluna do tabuleiro para jogar (0-2): "))

            # Condições criadas para checar se a jogada do Jogador2 é uma jogada válida

            if selecionarLinha > len(tabuleiro) - 1 or selecionarColuna > len(tabuleiro[0]) - 1:
                print("Jogada inválida, por favor jogue novamente.")
            elif tabuleiro[selecionarLinha][selecionarColuna] == 'X' or tabuleiro[selecionarLinha][selecionarColuna] == 'O':
                print("Posição já ocupada, escolha outra.")
            else:
                tabuleiro[selecionarLinha][selecionarColuna] = 'O'
                break  # Jogada válida, sai do loop do jogador 2

        # Imprime o tabuleiro novamente para, ou o resultado final, ou dar continuidade ao jogo
        for linha in tabuleiro:
            print(linha)

        # Condição que valida se o Jogador2 venceu a partida chamando a funcao checarVitoria
        if checarVitoria(tabuleiro, jogador2, 'O'):
            break  # Jogador 2 venceu, termina o jogo


jogoDaVelha()
