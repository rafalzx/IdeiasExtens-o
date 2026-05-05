import random

numero_secreto = random.randint(1, 100) #Gera um número aleatório entre 1 e 100, contando com os extremos
tentativas = 0
max_tentativas = 7

print("🎯 Adivinhe o número!")
print(f"   Estou pensando em um número entre 1 e 100")
print(f"   Você tem {max_tentativas} tentativas\n") #/n separa para uma próxima linha

while tentativas < max_tentativas:
    tentativas_restantes = max_tentativas - tentativas
    chute = int(input(f"[{tentativas_restantes} tentativas restantes] Seu chute: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"\n🏆 Acertou em {tentativas} tentativa(s)! O número era {numero_secreto}")
        break
    elif chute < numero_secreto:
        print("📈 Muito baixo!\n")
    else:
        print("📉 Muito alto!\n")
else:
    print(f"\n💀 Game over! O número era {numero_secreto}")