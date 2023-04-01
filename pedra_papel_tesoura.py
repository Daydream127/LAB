import random

opcoes = ["pedra", "papel", "tesoura"]

jogada_user = input("escolhe entre pedra, papel ou tesoura: ").lower()
jogada_computador = random.choice(opcoes)

print("escolheste: ", jogada_user)
print("o computador escolheu: ", jogada_computador)

if jogada_user == jogada_computador:
    print("empate!")
elif jogada_user == "pedra":
    if jogada_computador == "papel":
        print("o computador ganhou!")
    else:
        print("tu ganhaste!")
elif jogada_user == "papel":
    if jogada_computador == "tesoura":
        print("o computador ganhou!")
    else:
        print("tu ganhaste!")
elif jogada_user == "tesoura":
    if jogada_computador == "pedra":
        print("o computador ganhou!")
    else:
        print("tu ganhaste!")