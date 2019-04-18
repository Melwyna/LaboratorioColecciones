#llamamos las funciones a este archivo:

#(A)(E)para calcular el promedio(A) y (E)<---para sacar el promedio de los 3 departamentos
from custom_functions.temperature_methods import suma

#(B)para calcular la suma de los valores o elementos de una lista(B)
from custom_functions.temperature_methods import suma2

#(B)para calcular el promedio de 3 listas de cada una exactamente 12 valores numericos(B)
from custom_functions.temperature_methods import promedion2

#(C)para calcular y con ello saber el mes mas caliente(C)
from custom_functions.temperature_methods import maso

#(C)(D)para calcular y saber el valor del mes mas caliente(C) y (D)<--para sumar las listas
from custom_functions.temperature_methods import masc

#(D)para calcular el promedio de los meses mas calientes de los tres departamentos(D)
from custom_functions.temperature_methods import promedion

#(E)(F)para calcular cual de los promedios de los departamentos fue mayor(E) y (F)<---para saber en que departamento se presento el mes mas caliente del año
from custom_functions.temperature_methods import prommcali

#(F)para saber el valor del mes mas caliente del año(F)
from custom_functions.temperature_methods import prommcali2

#(F)para saber cual fue el mes mas caliente de los departamentos en el año(F)
from custom_functions.temperature_methods import prommcali3

#(G)para saber la desviacion estandar de cada departamento(G)
from custom_functions.temperature_methods import varianza



####
#(1)-ingresar valores a la lista de los diferents departamentos
print("Digite las temperaturas del departamento de Santander", '\n')
santander = []
mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre",
       "diciembre"]

for x in range(0, 12):
 m = float(input("digite la temperatura de {}:".format(mes[x])))
 santander.append(m)
print(santander)
####


print('\n')


####
#(A)-utilizamos la funcion para sacar el promedio
t1= suma(santander)
print("Temperatura promedio de Santander:", t1)
guajira1=[21, 22, 23, 24, 25, 26, 27, 28, 29, 10, 11, 12] # <---esto fue para poner imprimir el promedio de la guajira
narino1=[30, 22, 20, 19, 18, 16, 26, 27, 29, 32, 11, 25] # <---esto fue para poner imprimir el promdedio de nariño
t2 = suma(guajira1)
t3 = suma(narino1)
print("Temperatura promedio de la Guajira:", t2)
print("Temperatura promedio de la Nariño:", t3)
####


print('\n')


####
#(B)-calcular la temperatura nacional ("hay dos formas")

#suma de los valores contenidos en la lista santander
s1=suma2(santander)

#lista del departamento de guajira (ejemplo)
guajira=[21, 22, 23, 24, 25, 26, 27, 28, 29, 10, 11, 12]
#suma de los valores contenidos en la lista guajira
s2=suma2(guajira)

#lista del departamento de nariño (ejemplo)
narino=[30, 22, 20, 19, 18, 16, 26, 27, 29, 32, 11, 25]

#suma de los valores contenidos en la lista narino
s3=suma2(narino)

#promedio de las 3 listas dividido en el numero de elementos
xb=promedion2(s1,s2,s3)
print("El promedio de la temperatura nacional es de:", xb)
####


print('\n')


####
#(C)-utilizamos la funcion para sacar el mes mas caliente de cada departamento
mesc1 = masc(santander) # <---valor de la temperatura del mes mas caliente de santander
mescl1 = maso(santander)
print("El mes mas caliente de Santander es:", mescl1, "-->", mesc1)
####


print('\n')


####
#(D)-utilizamos la funcion para sacar el promedio de los meses mas calientes de los 3 departamentos
mesc2 = masc(guajira) # <---valor de la temperatura del mes mas caliente de guajira
mesc3 = masc(narino) # <---valor de la temperatura del mes mas caliente de nariño
xd = promedion(mesc1,mesc2,mesc3)
print("El promedio de los meses mas calientes de los 3 departamentos es de:", xd)
####


print('\n')


####
#(E)-utilizamos la funcion para saber cual de los 3 departamentos tiene un promedio mayor
#t1= suma(santander) <--- este y t2 y t3 son los promedios de los departamentos
t2 = suma(guajira) # <--- la funcion suma() es para sacar el promedio de una lista
t3 = suma(narino)
xe = prommcali(t1,t2,t3)
print("El departamento con el promedio mas alto es:", xe)
####


print('\n')


####
#(F)-utilizamos la funcion para calcular cual fue la temperatura más caliente del año, en qué departamento se presentó y en que mes
promedf1 = prommcali2(mesc1,mesc2,mesc3) # <---para saber el valor del mes mas caliente del año
promedf2 = prommcali(mesc1,mesc2,mesc3) # <---para calcular cual de los promedios de los departamentos fue mayor
promedf3 = prommcali3(santander,guajira,narino) # <---para saber cual fue el mes mas caliente de los departamentos en el año
print("La temperatura mas caliente de todo el año fue:", promedf1, "grados, y se presento en", promedf2,
      "en el mes de", promedf3)
####


print('\n')


####
#(G)-utilizamos la funcion para calcular la desviacion estandar de cada departamento
xg1 = varianza(santander) # <--- este y xg2 y xg3 son el resultado de utilizar la funcion en las listas de los 3 departamentos
xg2 = varianza(guajira)
xg3 = varianza(narino)
print("La desviacion estandar del departamento de santander fue de:", xg1)
print("La desviacion estandar del departamento de la guajira fue de:", xg2)
print("La desviacion estandar del departamento de nariño fue de:", xg3)
####