import random

desculpas = [
    "Estava com dor de cabeça",
    "Meu cachorro comeu meu trabalho",
    "A internet caiu justamente na hora",
    "Tive um sonho muito intenso e não consegui dormir",
    "Meu celular morreu e perdi o alarme",
    "Estava ajudando uma velhinha atravessar a rua",
    "O trânsito estava um caos absurdo",
    "Minha avó ligou e não dava pra desligar",
    "O gato ficou em cima do teclado e deletou tudo",
    "Estava meditando e perdi a noção do tempo",
]

print("🎲 Gerador de Desculpas\n")
input("Pressione Enter para gerar sua desculpa...")

desculpa = random.choice(desculpas)

print(f"\n✅ Sua desculpa é:\n👉 {desculpa}\n")