cuenta = [1, 2, 3, 4, 5]
frutitas = ['manzana', 'platano', 'fresa', 'naranja']
morracha = [1, "medio", 2, "cobre", 3, "bicolor"]

for numero in cuenta:
  print(f"Estamos contando numeros {numero}")
  for fruta in frutitas:
    print(f"{numero} {fruta} bien jugosa :...) \n")

for i in morracha:
  for j in morracha:
    print(f"{i} es de color {j}.\n")

varios = []

for i in range(6):
  print(f"Completando el refri con {i}")
  varios.append