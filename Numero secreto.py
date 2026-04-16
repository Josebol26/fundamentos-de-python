secret_number = 0
while secret_number != 777:
    secret_number = int(input("""
    +===================================+
    | Bem vindo ao meu jogo, trouxa!    |
    | Insira um número inteiro          |
    | e adivinhar o número que tenho    |
    | escolhidos para você.             |
    | Então, qual é o número secreto?   |
    +===================================+
    """))
    if secret_number != 777:
        print("Ha ha! Você está preso no meu loop!")

print('Muito bem, trouxa! Você está livre agora.')
