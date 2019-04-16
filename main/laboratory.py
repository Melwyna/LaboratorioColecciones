"""
Solución del laboratorio
"""
from custom_functions.temperature_methods import prommcali
from custom_functions.temperature_methods import maso
from custom_functions.temperature_methods import suma
from custom_functions.temperature_methods import promedion
from custom_functions.temperature_methods import masc
from custom_functions.temperature_methods import prommcali2
from custom_functions.temperature_methods import prommcali3
from custom_functions.temperature_methods import varianza
try:

 print("Digite las temperaturas del departamento de Santander", '\n')
 santander = []
 mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre",
       "diciembre"]

 for x in range(0, 12):
     m = float(input("digite la temperatura {}:".format(mes[x])))
     santander.append(m)

 t1= suma(santander)
 print("Temperatura promedio de la Santander:", t1)
 mesc1= masc(santander)
 mescl1= maso(santander)
 print("El mes mas caliente de Santander es:", mescl1, "-->", mesc1)


 print('\n')
 print("Digite las temperaturas del departamento de Guajira", '\n')
 guajira = []

 for x in range(0, 12):
     m = float(input("digite la temperatura {}:".format(mes[x])))
     guajira.append(m)

 t2 = suma(guajira)
 print("Temperatura promedio de la Guajira:", t2)
 mesc2= masc(guajira)
 mesc22= maso(guajira)
 print("El mes mas caliente de Guajira es:", mesc22, "-->", mesc2)

 print('\n')
 print("Digite las temperaturas del departamento de Nariño", '\n')
 narino = []

 for x in range(0, 12):
     m = float(input("digite la temperatura {}:".format(mes[x])))
     narino.append(m)

 t3 = suma(narino)
 print("Temperatura promedio de la Nariño:", t3)
 mesc3= masc(narino)
 mesc33= maso(narino)
 print("El mes mas caliente de Nariño es:", mesc33, "-->", mesc3)


 print('\n')
 promn=promedion(t1,t2,t3)
 print("La temperatura nacional es de:", promn)

 print('\n')
 prommn=promedion(mesc1,mesc2,mesc3)
 print("La temperatura promedio de los meses más calientes de los 3 departamentos:", prommn)

 print('\n')
 promedcc=prommcali(t1,t2,t3)
 print("El promedio mas caliente de los tres departamentos es:", promedcc)

 print('\n')
 promedcctodo=prommcali2(mesc1,mesc2,mesc3)
 promedcctodo2=prommcali(mesc1,mesc2,mesc3)
 promedcctodo3=prommcali3(santander,guajira,narino)
 print("La temperatura mas caliente de todo el año fue:", promedcctodo, "grados, y se presento en", promedcctodo2, "en el mes de", promedcctodo3)

 print('\n')
 desviestan1=varianza(santander)
 print("La desviacion estandar de la temperatura en Santander es de:", desviestan1)

 print('\n')
 desviestan2=varianza(guajira)
 print("La desviacion estandar de la temperatura en Guajira es de:", desviestan2)

 print('\n')
 desviestan3=varianza(narino)
 print("La desviacion estandar de la temperatura en Nariño es de:", desviestan3)

except ValueError:
 print("No se permite ingresar letras")
except ZeroDivisionError:
 print("hay un valor 0 en division")