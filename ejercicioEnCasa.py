#Aca se crea un diccionario con llaves las cuales son 101,105,106 y los valores son "Juan valdes", "Paquita la del barrio" y "maria pajon"
huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}


#Aca se imprime el diccionario
print (huespedes)
#Aca imprime las llaves y los valores del diccionario
print (huespedes.items())
#Aca imprime solamente
print (huespedes.keys())
#Aca va a recorrer todos las llaves del diccionario huespedes  y me los va a imprimir
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
#me va a imprimir "Paquita la del Barrio"
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
#Crea un diccionario llamado registroshoy que va a tener las llaves 201, 301 y los valores Vicente Fernandez y Pepe Guardiola
registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
#Une al final de la lista huespedes los valores que estaban el la lista registroshoy
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
#Elimina las llaves 102 y 202 del diccionario huespedes 

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
#Primero crea un diccionario llamado inventario, dentro de este diccionario, dentro de este diccionario se almacenan agunos valores, tuplas y listas
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)
#Hace que todos los valores  de la llave llamada cartera se ordenen en orden alfabetico
inventario["cartera"].sort()
print(inventario)
#remueve el valor "Moneda" de la llave cartera 
inventario["cartera"].remove("Moneda")
print(inventario)
#Imprime 500, que es el valor que esta ubicado en la posicion 0 de la llave plata 
print(inventario.get("plata")[0])
