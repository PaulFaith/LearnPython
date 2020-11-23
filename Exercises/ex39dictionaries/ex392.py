words = {
  'tractor' : 'TR',
  'bombilla' : 'BB',
  'cigüeña' : 'CG',
  'boton' : 'BT',
  'mesa' : 'MS'
}

conections = {
  'TR' : 'Tierra',
  'BT' : 'Negro',
  'MS' : 'Madera'
}

conections['BB'] = 'Luz'
conections['CG'] = 'Plumas'

print ('-' * 15)
print("The abreviation BB is connected with: ", conections['BB'], " try to know the word for the abreviation.")
print("The abreviation TR is connected with: ", conections['TR'], " try to know the word for the abreviation.")

print('-' * 15)
print("Cigüeña abreviation is: ", words['cigüeña'])

print('-' * 15)
print("Ok the word ", conections[words['bombilla']], "  is connected with the abreviation BB, so BB is the abreviation for BOMBILLA!!!!")

