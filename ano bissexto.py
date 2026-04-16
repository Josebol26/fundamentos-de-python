year = int(input("Digite um ano: "))

if year < 1582:
  print("Não dentro do período do calendário gregoriano")
else:
    if year % 4 == 0:
        print("Ano bissexto")
    else: 
        print("Ano comum")