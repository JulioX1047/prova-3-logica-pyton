
ns = 19
tentativas = 3
tentativa_atual = 0
print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 3 tentativas para adivinhar o número secreto.")
while tentativa_atual < tentativas:
    palpite = int(input(f"Tentativa {tentativa_atual + 1}: Digite o seu palpite: "))
    
    if palpite == ns:
        print(f"Parabéns! Você acertou o número {ns}.")
        break  
    
    tentativa_atual +=1
if tentativa_atual == tentativas:
    print(f"Que pena! Você usou todas as suas tentativas. O número era {ns}.")
