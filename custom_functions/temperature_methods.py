#Promedio de cada depatamento
def suma(a):

 sum=0
 for item in a:
  sum=sum+item
 prome=sum/len(a)
 return prome

#Promedio nacional y temperatura promedio de los meses más calientes de los 3 departamentos
def suma2(a):

 sum=0
 for item in a:
  sum=sum+item
 return sum

def promedion2(a,b,c):
 ter2=(a+b+c)/36
 return ter2

def promedion(a,b,c):
 ter=(a+b+c)/3
 return ter

#Valor del mes mas caliente del departamento
def masc(a):
 mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
 mascaliente=a[0]
 for item in a:
  if item>mascaliente:
   mascaliente=item
 return mascaliente

#El mes mas caliente del departamento
def maso(a):
 mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
 mascaliente=a[0]
 for item in a:
  if item>mascaliente:
   mascaliente=item
 if mascaliente==a[0]:
  return "enero"
 else:
  if mascaliente==a[1]:
   return "febrero"
  else:
   if mascaliente==a[2]:
    return "marzo"
   else:
    if mascaliente==a[3]:
     return "abril"
    else:
     if mascaliente==a[4]:
      return "mayo"
     else:
      if mascaliente==a[5]:
       return "junio"
      else:
       if mascaliente==a[6]:
        return "julio"
       else:
        if mascaliente==a[7]:
         return "agosto"
        else:
         if mascaliente==a[8]:
          return "septiembre"
         else:
          if mascaliente==a[9]:
           return "octubre"
          else:
           if mascaliente==a[10]:
            return "noviembre"
           else:
            if mascaliente==a[11]:
             return "diciembre"

#El promedio mas caliente de los tres departamentos y la temperatura más caliente del año, en qué departamento se presentó y en cual mes se presento
def prommcali(a,b,c):

 if a>b and a>c:
  return "Santander"
 if b>c and b>a:
  return "Guajira"
 if c>b and c>a:
  return "Nariño"

#Valor del mes mas caliente de cada departamento y la temperatura más caliente del año, en qué departamento se presentó y en cual mes se presento
def prommcali2(a,b,c):

 if a>b and a>c:
  return a
 if b>c and b>a:
  return b
 if c>b and c>a:
  return c

#La temperatura más caliente del año, en qué departamento se presentó y en cual mes se presento
def prommcali3(a,b,c):
 mesc11 = maso(a)
 mesc22 = maso(b)
 mesc33 = maso(c)
 if a>b and a>c:
  return mesc11
 if b>c and b>a:
  return mesc22
 if c>b and c>a:
  return mesc33

#Desviación estándar de la temperatura en cada departamento
import math
def varianza(a):
    suma = 0

    for item in a:
        suma = suma + item

    promedio = suma / len(a)

    v1 = promedio - a[0]
    if v1 < promedio:
        v1 = (v1) * (-1)
    else:
        v1 = v1

    v2 = promedio - a[1]
    if v2 < promedio:
        x2 = (v2) * (-1)
    else:
        x2 = v2

    v3 = promedio - a[2]
    if v3 < promedio:
        x3 = (v3) * (-1)
    else:
        x3 = v3

    v4 = promedio - a[3]
    if v4 < promedio:
        x4 = (v4) * (-1)
    else:
        x4 = v4

    v5 = promedio - a[4]
    if v5 < promedio:
        x5 = (v5) * (-1)
    else:
        x5 = v5

    v6 = promedio - a[5]
    if v6 < promedio:
        x6 = (v6) * (-1)
    else:
        x6 = v6

    v7 = promedio - a[6]
    if v7 < promedio:
        x7 = (v7) * (-1)
    else:
        x7 = v7

    v8 = promedio - a[7]
    if v8 < promedio:
        x8 = (v8) * (-1)
    else:
        x8 = v8

    v9 = promedio - a[8]
    if v9 < promedio:
        x9 = (v9) * (-1)
    else:
        x9 = v9

    v10 = promedio - a[9]
    if v10 < promedio:
        x10 = (v10) * (-1)
    else:
        x10 = v10

    v11 = promedio - a[10]
    if v11 < promedio:
        x11 = (v11) * (-1)
    else:
        x11 = v11

    v12 = promedio - a[11]
    if v12 < promedio:
        x12 = (v12) * (-1)
    else:
        x12 = v12

    varia = (
                        v1 ** 2 + v2 ** 2 + v3 ** 2 + v4 ** 2 + v5 ** 2 + v6 ** 2 + v7 ** 2 + v8 ** 2 + v9 ** 2 + v10 ** 2 + v11 ** 2 + v12 ** 2) / len(
        a)
    varianza = math.sqrt(varia)

    return (varianza)