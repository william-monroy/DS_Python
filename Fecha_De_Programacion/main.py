from datetime import datetime

from pytz import timezone

zona_horaria = timezone('America/Lima')

fecha_hora = datetime.now(zona_horaria)

fecha_hora_formato = fecha_hora.strftime("%B %d, %Y %H:%M:%S")

print("Created on", fecha_hora_formato)

autor = "William Monroy"

print("Author:",autor)