from datetime import datetime # importamos la librería de fechas y horas

from pytz import timezone # importamos la librería de zonas horarias 

zona_horaria = timezone('America/Monterrey') # definimos el uso horario de Monterrey

fecha_hora = datetime.now(zona_horaria) # definimos la variable fecha_hora usando la función now() para saber fecha y hora actual, y le indicamos la zona horaria

fecha_hora_formato = fecha_hora.strftime("%B %d, %Y %H:%M:%S") # le damos formato a la fecha y hora

print("Created on", fecha_hora_formato) # imprimimos la fecha y hora

autor = "William Monroy" # definimos la variable autor con nuestro nombre

print("Author:",autor) # imprimimos nombre del autor