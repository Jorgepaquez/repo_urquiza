tiempo_real = 3
tiempo_de_juego = 0

print("Ingrese el tiempo estimado para la entrega")
horas = float(input("Horas: "))
minutos = float(input("Minutos: "))

minutos_horas = horas / 60
tiempo_de_juego = minutos_horas + minutos

tiempo_estimado = tiempo_de_juego / tiempo_real

print(f"Tu entrega tiene una demora aproximada de {tiempo_estimado} minutos en la vida real")