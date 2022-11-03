#define una tupla con 23,'a','Pepe, dentro de esta tupla hay otra tuple que contiene los siguientes valores 2.5,3.7,'x' y dentro de la primera tupla hay una lista con los siguientes valores :"perrito","gatito"
t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
#Imprime la tupla
print (t)
#Imprime la cantidad de valores que hay en la tupla
print (len(t))
#Imprime =====================================
print ('=====================================')
#Imprime 23
print (t[0])
#Imprime ['perrito', 'gatito']
print (t[3])
#Imprime ('a', (2.5, 3.7, 'x'))
print (t[1:3])
#Imprime gatito
print (t[3][1])


print ('====================================')
#Imprime ['perrito', 'gatito']
print (t[3])
#Imprime (23, 'a', (2.5, 3.7, 'x'), ['perrito', 'gatito', 'lorito'], 'Pepe'), le agrega a la posicion 3 el valor lorito
t[3].append('lorito')
print (t)
#Imprime ====================================
print ('====================================')
#Imprime en forma de lista todos los valores dentro de la tupla t
for elemento in t:
    print (elemento)
# Imprime ====================================
print ('====================================')
#Recorre tod@ el tamaño de la lista y va imprimiendo cada valor de la lista y dando salto de linea
for index in range(0,len(t)):
    print (t[index])

print ('====================================')
#Imprime "El elemento 'a' esta en la tupla" ya que la condicion es verdadera
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")

print ('====================================')
#Convierte la tupla t en una lista
lista=list(t)
#Convierte en valor a al valor A
lista[1]='A'
print (lista)
#Convierte la lista en una tupla e imprime la tupla
tupla=tuple(lista)
print (tupla)

print ('====================================')
#Va a imprimir cada pareja de valores y va a dar un salto de linea, esto hasta que se acabe las parejas de valores
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for x, y in l:
    print (x, ':', y)