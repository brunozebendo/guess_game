"""Jogo da adivinhação"""
from random import randint

FACIL = 10
DIFICIL = 5
"""variável no escopo global, que não pode sofrer variação, por isso está em maiúsculo"""
def checker(numero_escolhido, escolha, turns):
  if escolha > numero_escolhido:
    print("errrrrou, seja menos")
    return turns -1
  elif escolha < numero_escolhido:
    print("tá frio, tá frio, suba aí")
    return turns -1
  else:
    print(f"{numero_escolhido} acerrrtou, não é de todo burro")

"""função para chegar o número escolhido, passou-se os parâmetros dentro da função"""
def level():
  level_choice = input("Digite F para fácil com 10 chances ou D para difícil com 5 chances\n")
  if level_choice == "f":
    return FACIL
  else:
    return DIFICIL
"""função para checar a escolha entre o número de jogadas possíveis"""

def jogo():
  numero_escolhido = randint(1,100)
  turns = level()
  guess = 0
  while guess != numero_escolhido:

    print(f"Vc tem {turns} mais chances, mas já adianto que vai perder")
    escolha = int(input("escolha um numero de 01 a 100\n"))
    turns = checker(numero_escolhido, escolha, turns)
    if turns  == 0:
      print("Perdeu, playboy!")
      return
    elif escolha != numero_escolhido:
      print("tente de novo...ou não, ninguém se importa")

jogo()
"""função para o jogo em si, aqui o que foi feito de diferente foi o modo como o turns foi usado para diminuir
o número de jogadas, primeiro passa-se a função level para determinar o número de jogadas a que o jogador
  tem direito, depois, passa-se dentro do escopo local a função Checker que vai diminuir o número de jogadas
   a cada erro e essa função turn já atualiza a outra. A função return também é uma boa escolha para parar o jogo."""

