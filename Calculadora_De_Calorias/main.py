print('''

───────────▒▒▒▒▒▒▒▒
─────────▒▒▒──────▒▒▒
────────▒▒───▒▒▒▒──▒░▒
───────▒▒───▒▒──▒▒──▒░▒                     
──────▒▒░▒──────▒▒──▒░▒
───────▒▒░▒────▒▒──▒░▒
─────────▒▒▒▒▒▒▒───▒▒                       ░█████╗░░█████╗░██╗░░░░░░█████╗░
─────────────────▒▒▒                        ██╔══██╗██╔══██╗██║░░░░░██╔══██╗
─────▒▒▒▒────────▒▒                         ██║░░╚═╝███████║██║░░░░░██║░░╚═╝
───▒▒▒░░▒▒▒─────▒▒──▓▓▓▓▓▓▓▓                ██║░░██╗██╔══██║██║░░░░░██║░░██╗
──▒▒─────▒▒▒────▒▒▓▓▓▓▓░░░░░▓▓──▓▓▓▓        ╚█████╔╝██║░░██║███████╗╚█████╔╝
─▒───▒▒────▒▒─▓▓▒░░░░░░░░░█▓▒▓▓▓▓░░▓▓▓      ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░
▒▒──▒─▒▒───▓▒▒░░▒░░░░░████▓▓▒▒▓░░░░░░▓▓     
░▒▒───▒──▓▓▓░▒░░░░░░█████▓▓▒▒▒▒▓▓▓▓▓░░▓▓    ░█████╗░░█████╗░██╗░░░░░░█████╗░██████╗░██╗░█████╗░░██████╗
──▒▒▒▒──▓▓░░░░░░███████▓▓▓▒▒▒▒▒▓───▓▓░▓▓    ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
──────▓▓░░░░░░███████▓▓▓▒▒▒▒▒▒▒▓───▓░░▓▓    ██║░░╚═╝███████║██║░░░░░██║░░██║██████╔╝██║███████║╚█████╗░
─────▓▓░░░░░███████▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓░░▓▓     ██║░░██╗██╔══██║██║░░░░░██║░░██║██╔══██╗██║██╔══██║░╚═══██╗
────▓▓░░░░██████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓░░░░▓▓      ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░░██║██║██║░░██║██████╔╝
────▓▓▓░████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓        ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═════╝░
─────▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓            
─────▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓            
──────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
───────▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
─────────▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
───────────▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓
───────────────▓▓▓▓▓▓▓▓


''')

alimento = input("Ingresa el nombre del alimento: ")

carbohidratos = float(input("Ingresa la cantidad de carbohidratos en gramos: "))

lipidos = float(input("Ingresa la cantidad de lipidos en gramos: "))

proteinas = float(input("Ingresa la cantidad de proteinas en gramos: "))

calorias = (carbohidratos * 4) + (lipidos * 9) + (proteinas * 4)

print ("Las calorías proporcionadas por una porcion de {} son:".format(alimento),calorias)