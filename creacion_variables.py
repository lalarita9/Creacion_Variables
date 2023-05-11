#Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra “ejercicio”. 
#Luego, crear un set que contendrá cada una de las variables que creamos, y será asignado a una variable. 
#A continuación, crearemos una lista que contendrá el set creado anteriormente, y una variable con el valor lógico False. 
#Esta lista la asignaremos a una variable que luego imprimiremos en pantalla.

#Creación de variable con datos dados
a = 8
b = 10.5
c = "ejercicio"
#Creación de varible, agrupando las variables dadas
grupo_variables = {a,b,c}
#Se crea una lista
lista = list(grupo_variables)
#Se usa la función print para imprimir lista
print(lista)
#Se agrega el valor False
lista.append(False)
#Se usa la función print para imprimir lista con el nuevo valor
print(lista)





