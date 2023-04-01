import random

opcoes = ["pedra", "papel", "tesoura"]
resultados = []

def pedraPapelTesoura():
    jogada_user = input("escolhe entre pedra, papel ou tesoura: ").lower()
    jogada_computador = random.choice(opcoes)

    while jogada_user not in opcoes:
        jogada_user = input("escolha inválida, escolhe entre pedra, papel ou tesoura: ").lower()

    print("escolheste: ", jogada_user)
    print("o computador escolheu: ", jogada_computador)

    if jogada_user == jogada_computador:
        print("empate!")
        return("e")
    elif jogada_user == "pedra":
        if jogada_computador == "papel":
            print("o computador ganhou!")
            return("c")
        else:
            print("tu ganhaste!")
            return("u")
    elif jogada_user == "papel":
        if jogada_computador == "tesoura":
            print("o computador ganhou!")
            return("c")
        else:
            print("tu ganhaste!")
            return("u")
    elif jogada_user == "tesoura":
        if jogada_computador == "pedra":
            print("o computador ganhou!")
            return("c")
        else:
            print("tu ganhaste!")
            return("u")
while True:
    winner = pedraPapelTesoura()
    resultados.append(winner)

    c = str(input("queres continuar [y/n]?: ")).lower()
    while c not in ["y", "n"]:
        c = str(input("resposta inválida, queres continuar [y/n]?: ")).lower()

    if c == "n":
        break

    print("-------")

computer_wins = resultados.count("c")
user_wins = resultados.count("u")
ties = resultados.count("e")

print(f"foram feitos {len(resultados)} jogos, dos quais o user ganhou {user_wins} vezes, o computador ganhou {computer_wins} vezes, e o jogo ficou empatado {ties} vezes.")
