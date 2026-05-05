import random
import time
import sys

respostas = [
    "Pode ser que sim",
    "Com certeza",
    "Definitivamente não",
    "Está no caminho certo",
    "O importante é tentar",
    "Quem sabe um dia",
    "Não conte com isso...",
]

def digitar(texto, velocidade=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

input("Qual a sua pergunta? ")

import sys

print("🎱 A bola está pensando", end="", flush=True) #end=""faz o código não pular a linha e substitui por um vazio 
time.sleep(1)
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(1) #O código espera um segundo antes do próximo
sys.stdout.write(".") # joga o ponto no caminho assim que ele é recebido
sys.stdout.flush() #Printa sem esperar o código finalizar
time.sleep(1) #O código espera um segundo antes do próximo
sys.stdout.write(".")
sys.stdout.flush()
time.sleep(0.5)
print()

print()

resposta = random.choice(respostas)

print("Sua resposta é: ")
digitar(resposta, velocidade = 0.06)