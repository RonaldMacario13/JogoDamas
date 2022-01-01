while True:
    print("Jogo de Damas v1.0 \n")
    print("Menu \n 1.Jogar \n 2.Instruções \n 3.Sair")
    opcao=(input("Digite o número da opção desejada: "))
    if opcao == 3:
        break
    elif opcao == 1:
        continue
    elif opcao == 2:
        print("Após iniciar a partida, você deve indicar a coluna e a linha da peça que você deseja mover, depois informar a coluna e linha de onde você quer que a peça vá. Para sair do Jogo digite '3' a qualquer momento")
    else:
        print("Comando não reconhecido, reveja as opções e tente novamente!")