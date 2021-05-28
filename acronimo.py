# INGRESO
frase = input('frase:')

# PROCEDIMIENTO
n = len(frase)

# Convierte frase a MAYUSCULAS
frase = frase.upper()

# inicializa salida z con la primera letra
# de la primera palabra
i = 0
z = frase[i]

# buscar la primera letra de cada palabra
# a partir de la segunda posición
# completar para 'de ' y revisar con 'desarrollo'
i = 1
while not(i>=(n-1)):
    if (frase[i]==' ' and  not(frase[i+1]=='D')):
        if not(frase[i+1]=='Y'):
            z = z + frase[i+1]
    i = i + 1

# SALIDA
print(z)