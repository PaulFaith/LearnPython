lista = "Esta es una lista con 10 palabras "
palabras = lista.split()
print("Vamos a ver cuantas palabras hay en la variable lista:\n")
maspalabras = ["Aguila", "Coco", "PIña", "Guajolote"]
for i in range(len(palabras)):    
    print(f"{i+1}.-{palabras[i]}")

print(f"Eso fueron {len(palabras)} palabras")

while len(palabras) != 10 :
  otra = maspalabras.pop()
  print("Agregando", otra)
  palabras.append(otra)
  print(f"Ahora tenemos {len(palabras)}")

while len(palabras) != 0 :
  print(' '.join(palabras))
  print("Ahora quitamos ", palabras.pop(), "y queda: ") 