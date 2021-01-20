datos_persona = ['Sujeto', 'Prueba', 18, 1.77, 78]

# Los datos de la lista corresponderán a: nombre, apellido, edad, estatura, peso

nombre, apellido, edad, estatura, peso = datos_persona

imc = peso / estatura ** 2  # Estatura al cuadrado (exponente 2)
imc = peso / estatura ** 2  # Estatura al cuadrado (exponente 2)

if imc <= 18.4:  # si el IMC es menor a 18.4
    print("Peso bajo")
elif imc >= 18.5 and imc <= 24.9:  # sino, si el IMC es mayor a 18.5 y menor 24.9
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:  # sino, si el IMC es mayor a 25 y menor a 29.9
    print("Sobre peso")
else:  # sino cae en ninguno de los rangos anteriores entonces es mayor
    print("Obesidad")

guia = """

      Cómo leer resultados

Nivéles de Peso de acuerdo al IMC:

IMC por debajo de 18.5: Peso bajo

IMC entre 18.5 – 24.9: Peso normal

IMC entre 25.0 – 29.9: Sobrepeso

IMC de más de 30.0: Obesidad"""

print(guia)
