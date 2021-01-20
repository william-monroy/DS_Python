def titulo(txt):
    print()
    print('='*(len(txt)+2))
    print(' '+txt+' ')
    print('='*(len(txt)+2))
    print()

import pandas as pd

data = {
    'apples': [3, 2, 1, 0],
    'oranges': [0, 3, 7, 2]
}

# Convertir diccionario a DataFrame
purchases = pd.DataFrame(data)

print(purchases)

print('\n=================================================\n')

# Convertir diccionario a DataFrame con indices
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)

# Leer archivos csv localmente
df = pd.read_csv('Libreria_Pandas\menu_mcdonalds.csv', index_col=0)
print(df)

print('\n=================================================\n')

# iloc  -->	Permite seleccionar los elementos con base en la posición.
# loc   -->	Permite seleccionar mediante etiquetas o declaraciones condicionales.

# USO DE ILOC
print('''

######  ###     ######  ######
######  ###     ######  ######
  ##    ###     ##  ##  ##
  ##    ###     ##  ##  ##
  ##    ###     ##  ##  ##
######  ######  ######  ######
######  ######  ######  ######

''')

df = pd.read_csv('Libreria_Pandas\imdb.csv',escapechar='\\')
primer_fila = df.iloc[0]
segunda_fila = df.iloc[1]
ultima_fila = df.iloc[-1] 

# Seleccionar Filas

titulo('Primera Fila')
print(primer_fila)
titulo('Segunda Fila')
print(segunda_fila)
titulo('Ultima Fila')
print (ultima_fila)

print('\n------------------------------------------------\n')

# Seleccionar Columnas

titulo('Primera Columna')
print(df.iloc[:, 0]) 
titulo('Segunda Columna')
print(df.iloc[:, 1]) 
titulo('Ultima Columna')
print(df.iloc[:, -1])

print('\n------------------------------------------------\n')

#Seleccion Multiple de Filas y Colmunas

titulo('Primeras cinco filas')
print(df.iloc[0:5]) # Primeras cinco filas
titulo('Primeras cinco columnas')
print(df.iloc[:, 0:5]) # Primeras cinco columnas
titulo('Primera, tercera y segunda filas')
print(df.iloc[[0,2,1]]) # Primera, tercera y segunda filas
titulo('Primera, tercera y segunda columnas')
print(df.iloc[:, [0,2,1]]) # Primera, tercera y segunda columnas


print('\n=================================================\n')

# USO DE LOC

print('''

  ###     ######  ######
  ###     ######  ######
  ###     ##  ##  ##
  ###     ##  ##  ##
  ###     ##  ##  ##
  ######  ######  ######
  ######  ######  ######

''')

# Seleccion de Filas y Columnas