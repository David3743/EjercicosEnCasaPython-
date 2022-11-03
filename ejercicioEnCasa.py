#Aca se crea un diccionario con llaves las cuales son 101,105,106 y los valores son "Juan valdes", "Paquita la del barrio" y "maria pajon"
huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}


#Aca se imprime el diccionario
print (huespedes)
#Aca imprime las llaves y los valores del diccionario
print (huespedes.items())
#Aca imprime solamente
print (huespedes.keys())
#Aca va a recorrer todos las llaves del diccionario y me los va a imprimir
for key in huespedes:
    print (key)
#Aca se imprime los valores que estan dentro de las llaves osea 'Juan Valdes', 'Paquita la del Barrio', 'Mariana Pajon']
print (huespedes.values())
#Aca recorre todo el diccionario pero saca son los valores, ya que es en la posicion key
for key in huespedes:
    print (huespedes[key])
print()
#Aca recorre el diccionarrio huespedes, entonces recorre la llave  y despues recorre la llave en la posicion habitacion, osea tambien me va imprimir los valores de cada llave
for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion])
print()
#Aca me va a imprimir en diccionario, pero en forma de matriz y el huesped va a ser solamente Mariana Pajon
for habitacion,huesped in huespedes.items():
    print (habitacion,':',huespedes[key])
#Aca me va a imprimir tambien una matriz con todos las llaves y los valores, con la diferencia que van a estar enumerados iniciando desde 1
for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key])
print()
#me va a imprimir "Paquita la del Barrio
print (huespedes[105])
#me va a imprimir "Paquita la del Barrio
print (huespedes.get(105))
#va a imprimir ====================================
print ('====================================')
#Ahora en la llave 102 va a tener el valor "Fanny Lu"
huespedes[102]='Fanny Lu'
#Ahora en la llave 107 va a tener el valor 'Don Omar'
huespedes[107]='Don Omar'
# imprime ('109', 'Luis Miguel')
huespedes.setdefault('109','Luis Miguel')
#Me va a imprimir en forma de lista hacia abajo la llave y su respectivo valor
for huesped in huespedes.items():
    print (habitacion,':',huesped)
print()
#Agrega las llaves 201 , 301 con los valores 'Vicente Fernandez' y Pepe Guardiola
registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
#Agrega las llaves 201 , 301 con los valores 'Vicente Fernandez' y Pepe Guardiola al diccionario huespedes
huespedes.update(registroshoy)
#Imprime en forma de lista hacia abajo todos las llaves y valores que hay en el diccionario huespedes
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped)
print()
#Imprime ====================================
print ('====================================')
#En la llave 107 el nuevo valor va a ser 'Ricky Martin'
huespedes[107]='Ricky Martin'
print (huespedes)

print ('====================================')
#imprime{101: 'Juan Valdes', 105: 'Paquita la del Barrio', 107: 'Ricky Martin', '109': 'Luis Miguel', 201: 'Vicente Fernandez', 301: 'Pepe Guardiola'}

del huespedes[102]
huespedes.pop(202)
print(huespedes)

print ('====================================')
#Crea dos copias del diccionario huespedes
copia1=huespedes.copy()
print ('copia1: ',copia1)
copia2={}
copia2.update(huespedes)
print ("copia2: ",copia2)

print ('====================================')
#imprime {2: 'xxx', 5: 'xxx', 7: 'xxx', 1: 'xxx'}
lista=[2,5,7,1]
diccio=dict.fromkeys(lista,"xxx")
print(diccio)

print ('====================================')
#Imprime {'plata': (500, 2500), 'cartera': ['Cedula', 'Moneda', 'Boletas'], 'mecato': 'Detodito', 'dias': 1}
#{'plata': (500, 2500), 'cartera': ['Boletas', 'Cedula', 'Moneda'], 'mecato': 'Detodito', 'dias': 1}
#{'plata': (500, 2500), 'cartera': ['Boletas', 'Cedula'], 'mecato': 'Detodito', 'dias': 1}
#500
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)
inventario["cartera"].sort()
print(inventario)
inventario["cartera"].remove("Moneda")
print(inventario)
print(inventario.get("plata")[0])