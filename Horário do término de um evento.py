hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
if hour <= 23 and mins <= 59:
    tempo_total_minutos = (hour * 60) + mins
    tempo_total_dia = tempo_total_minutos + dura
    hora_final = tempo_total_dia // 60 % 24
    minuto_final = tempo_total_dia % 60

else:
    print("Hora inválida!")
    # encontre um total de todos os minutos
# encontre um número de horas escondido em minutos e atualize a hora
# minutos corretos para cair no intervalo (0..59)
# horas corretas para cair no intervalo (0..23)
print(hora_final, ":", minuto_final)
