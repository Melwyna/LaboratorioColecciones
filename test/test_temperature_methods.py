import unittest
from custom_functions import temperature_methods

class TestCollectionMethods(unittest.TestCase):

    def test_suma(self):

        lista = [2, 3, 4, 5]
        result1 = temperature_methods.suma(lista)

        self.assertEqual(result1, 3.5)

    def test_promedion(self):

        a=5
        b=1
        c=3
        result2 = temperature_methods.promedion(a,b,c)

        self.assertEqual(result2, 3)

    def test_masc(self):

        lista1 = [1, 2, 3, 4]
        result3 = temperature_methods.masc(lista1)

        self.assertEqual(result3, 4)

    def test_maso(self):

        lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result4 = temperature_methods.maso(lista2)

        self.assertEqual(result4, "diciembre")

    def test_prommcali(self):

        a=15
        b=20
        c=12
        result5 = temperature_methods.prommcali(a,b,c)

        self.assertEqual(result5, "Guajira")

    def test_prommcali2(self):

        a=91
        b=44
        c=65
        result6 = temperature_methods.prommcali2(a,b,c)

        self.assertEqual(result6, 91)

    def test_prommcali3(self):
        """"
        +ES UNA EJEMPLO EN CONTEXTO PARA ENTENDER QUE FUNCIONA+
        
        from custom_functions.temperature_methods import prommcali3
        from custom_functions.temperature_methods import maso

        santander=[1, 2, 3, 4, 5, 6, 12, 8, 9, 10, 11, 7]

        guajira=[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        narino=[36, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 25]


        x1=maso(santander)
        x2=maso(guajira)
        x3=maso(narino)
        print(x1, x2, x3)<--- SON MESES DE LAS TEMPERATURAS MAS ALTAS DE CADA LISTA

        x4=prommcali3(santander,guajira,narino)
        print(x4)<--- ES EL MES DE LA TEMPERATURA MAS ALTA DE LAS 3 LISTAS
        """""

        santander = [1, 2, 3, 4, 5, 6, 12, 8, 9, 10, 11, 7]

        guajira = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        narino = [36, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 25]

        a=santander
        b=guajira
        c=narino
        result7 = temperature_methods.prommcali3(a,b,c)

        self.assertEqual(result7,"enero")

    def varianza(self):

        a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result7 = temperature_methods.varianza(a)

        self.assertEqual(result7,3.45205253)