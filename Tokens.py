#Practica #3 Reconocimiento  mediante la funcion findall y expresiones regulares
#NOMBRE; Rene Martinez M.
#VERSION: V3.3
#FECHA: Lunes 19 Octubre 2020
#HORA: 19:32

import re

'''Esta lista no se utiliza por el momento'''
#list_p_reservadas = ['include','stdio','h','float','conio','']

class Lexer():

    '''ATRIBUTOS'''
    #LISTAS
    x               = []
    list_reservadas     = []
    #EXPRESIONES
    exp_identificadores = ""



    def __init__(self):
        self.x = list()
        self.file = open('Area.c', mode='r')
        self.list_identi = list()
        self.list_reservadas ={"main","include","define","struct","void",
                               "break","continue","default","else","for[^a-z]","if","return","Auto",
                               "double","int ","Break","else","long","switch","Case","enum","register",
                               "typedef","Char","extern","return","union","Const","float",
                               "short","unsigned","signed","Default","goto","sizeof","volatile",
                                "Do","static","while"
                               }
        self.exp_identificadores = "[_a-zA-Z][_a-zA-Z0-9 ]{0,30}"


    def getX(self):
        return self.x

    def obtenPractica3(self):

        # Leemos todas las lineas del archivo
        archivo = self.file.read()

        '''Reconocimiento de Identificadores'''
        print("BUSQUEDA DE IDENTIFICADORES")
        self.list_identi = re.findall(self.exp_identificadores, archivo)
        print(self.list_identi)

        '''Reconocimiento de Enteros'''
        print "BUSQUEDA DE ENTEROS"
        self.x = re.findall("[+|-][\d]+|[\d]+", archivo)
        print(self.x)

        '''Reconocimiento de Reales'''
        print "BUSQUEDA DE REALES"
        self.x = re.findall("[\d]+[.][\d]*|[-|+]+[.][\d]*|[-|+]*[.][\d]+|[.][\d]+", archivo)
        print(self.x)

        '''Reconocimiento de comentarios'''
        print "BUSQUEDA DE COMENTARIOS"
        self.x = re.findall("[/][/|*][a-z |A-Za-z]*[ |*/]*", archivo)
        print(self.x)

        '''Operadores Aritmeticos'''
        print "BUSQUEDA DE OPERADORES ARITMETICOS"
        self.x = re.findall("[+|-|*|=|/|%]", archivo)
        print(self.x)

        '''Operadores Logicos'''
        print "BUSQUEDA DE OPERADORES LOGICOS"
        self.x = re.findall("[&&|||>|<|>=|<=]+|/", archivo)
        print(self.x)

        '''Obtener For'''
        self.x = re.findall("for", archivo)
        print "For's"
        print(self.x)

        '''Obtener IF'''
        print "Obten IF's"
        self.x = re.findall("if", archivo)
        print(self.x)

        '''Obtener Saltos'''
        self.x = re.findall("\n+", archivo)
        print "Saltos de Linea"
        print(len(self.x))
        #Cerramos el archivo
        self.file.close()
        #FIN DE LA FUNCION obtenPractica3()

    def obtenPractica4(self):
        aux = list()
        archivo = self.file.read()

        for i in self.list_reservadas:
            print(i)
        '''Reconocimiento de Palabras Reservadas'''
        for elemento in self.list_reservadas:
            aux = re.findall(elemento,archivo)
            if (len(aux)>0):
                self.list_identi.append(aux)

        print(self.list_identi)
"""INSTANCIAS"""

l = Lexer()
#l.obtenPractica3()
l.obtenPractica4()



