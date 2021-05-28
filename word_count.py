# cuenta-elementos-de-lista-1.py

cadenaPalabras = 'Hola me llamo Fernando y me gustan los videojuegos '
cadenaPalabras += 'Hola me llamo Maria y me encantan las telenovelas'

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))