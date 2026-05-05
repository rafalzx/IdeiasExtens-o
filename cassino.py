import time
import random
import sys

fichas = 10
simbolos = [
    "👨",
    "🍔",
    "🧂",
    "🍿",
    "🌭",
    "🍟",
]
def digitar(texto, velocidade=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()


jogando = True
while jogando:
    input("Pressione enter para sortear os simbolos...")

    resultado = [random.choice(simbolos) for _ in range(3)] #Parte onde ele deve gerar os 3 símbolos

    digitar("Os símbolos sorteados foram...", velocidade = 0.09)
    print()

    sys.stdout.write(resultado[0])
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(resultado[1])
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(resultado[2])
    sys.stdout.flush()
    time.sleep(1)

    print()
    print()
    if resultado[0] == resultado[1] == resultado[2]:
        print("ganhou")
        fichas += 1
    else:
        print("perdeu")
        fichas -= 1

    respostaVal = False

    if fichas > 0:
        while not respostaVal:
            time.sleep(0.07)
            resposta = input(f"Você ainda tem {fichas} fichas restantes. Quer jogar novamente? (S/N)")
            if resposta == "S" or resposta == "N":
                time.sleep(0.07)
                respostaVal = True
                if resposta == "N":
                    jogando = False
            else:
                time.sleep(1)
                print("Digite apenas S ou N!!!")
    else:
        print("Suas fichas acabaram!!")
        jogando = False
