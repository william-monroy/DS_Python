# Lista de Datos de la persona
datos_persona = ['William', 'Monroy', 20, 1.73, 75]

# Asignacion multiple a cada varible a partir de la lista
nombre, apellido, edad, estatura, peso = datos_persona

# IMC = (peso / estatura) ^ 2
imc = peso / estatura ** 2

# Inicializamos variable para el resultado
resultado = ''

if imc <= 18.4: # Si el IMC es menor o igual a 18.4 entonces
    resultado = 'Peso bajo' # resultado es igual a Peso bajo
elif imc <= 24.9: # SinoSi IMC es menor o igual a 24.9 entonces
    resultado = 'Peso normal'# resultado es igual a Peso normal
elif imc <= 29.9: # SinoSi IMC es menor o igual a 29.9 entonces
    resultado = 'Sobre peso'# resultado es igual a Sobre peso
else: # Sino
    resultado = 'Obesidad'# resultado es igual a Obesidad

# Mostramos un String Literal con los resultados
print('''
──────────────────────────────────
──▄██─────────────────────────██▄─  ░█████╗░░█████╗░██╗░░░░░░█████╗░  ██╗███╗░░░███╗░█████╗░
─████──▄▄▄▄─────────────▄▄▄▄──████  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗  ██║████╗░████║██╔══██╗
─██████▐▐▐▐█████████████▐▐▐▐██████  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝  ██║██╔████╔██║██║░░╚═╝
─████──▀██▀─────────────▀██▀──████  ██║░░██╗██╔══██║██║░░░░░██║░░██╗  ██║██║╚██╔╝██║██║░░██╗
──▀██───██───────────────██───██▀─  ╚█████╔╝██║░░██║███████╗╚█████╔╝  ██║██║░╚═╝░██║╚█████╔╝
────────██───────────────██───────  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░  ╚═╝╚═╝░░░░░╚═╝░╚════╝░
────────██───────────────██───────  
────────██▄█████▄─▄█████▄██───────  
────────███████████████████───────  ¡Hola, {}!
────────████▌▐███████▌▐████───────
────────███████████████████───────
────────███████████████████───────  Tú peso registrado es de: {} kgs
────────█████▌▐█████▌▐█████───────
─────────██████▄▄▄▄▄██████────────  Tú estatura registrada es de: {} mts
──────────███████████████─────────
───────────█████████████──────────  De acuerdo con estos datos tú IMC es de {:.2f} lo que 
────────────▀█████████▀───────────  indica: {}
──────────────▀█████▀─────────────
────────────────▀█▀───────────────
──────────────────────────────────
'''.format(nombre + ' ' + apellido, peso, estatura, imc, resultado))

# Mostramos las instrucciones de lectura
print('''
                                 Cómo leer resultados

                            Nivéles de Peso de acuerdo al IMC:

                            IMC por debajo de 18.5: Peso bajo

                            IMC entre 18.5 – 24.9: Peso normal

                            IMC entre 25.0 – 29.9: Sobrepeso

                            IMC de más de 30.0: Obesidad

''')
