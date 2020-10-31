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
    list_identi     = []
    #EXPRESIONES
    exp_identificadores = ""



    def __init__(self):
        self.x = list()
        self.file = open('Area.c', mode='r')
        self.list_identi = list()
        self.exp_identificadores = "[_a-zA-Z][_a-zA-Z0-9 ]{0,30}"


    def getX(self):
        return self.x


    def obtenIdentificadores(self):
        self.file = open('Area.c', mode='r')
        #Leemos todas las lineas del archivo
        archivo = self.file.read()
        print("BUSQUEDA DE IDENTIFICADORES")
        #V1
        # x = re.findall("[^\d+.\d{1,2}|^#|^%]*",archivo)
        #V2
        #self.x = re.findall("[^//a-z]+[_a-zA-Z][_a-zA-Z0-9 ]{0,30}[^(\"\/nA-Za-z \")+]", archivo)
        #V3
        self.list_identi = re.findall(self.exp_identificadores, archivo)
        print(self.list_identi)
        self.file.close()


    def obtenEnteros(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        print "BUSQUEDA DE ENTEROS"
        #VR1
        #self.x = re.findall("[\d][^*|^.\d[f|d|i|c|s]]",archivo)
        #VR2
        self.x = re.findall("[+|-][\d]+|[\d]+",archivo)
        print(self.x)
        self.file.close()

    def obtenReales(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        print "BUSQUEDA DE REALES"
        #VR1
        #self.x = re.findall("[\d]+[.][\d]*",archivo)
        #VR2
        self.x = re.findall("[\d]+[.][\d]*|[-|+]+[.][\d]*|[-|+]*[.][\d]+|[.][\d]+",archivo)
        print(self.x)

    def obtenComentarios(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        print "BUSQUEDA DE COMENTARIOS"
        #VR!
        #self.x = re.findall("//[A-Za-z ]*",archivo)

        #VR2
        self.x = re.findall("[/][/|*][a-z |A-Za-z]*[ |*/]*", archivo)
        print(self.x)


    def obtenAritmeticos(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        print "BUSQUEDA DE OPERADORES ARITMETICOS"
        self.x = re.findall("[+|-|*|=|/|%]", archivo)
        print(self.x)

    def obtenLogicos(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        print "BUSQUEDA DE OPERADORES LOGICOS"
        self.x = re.findall("[&&|||>|<|>=|<=]+|/", archivo)
        print(self.x)
    def obtenFor(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        self.x = re.findall("for", archivo)
        print "For's"
        print(self.x)

    def obtenIf(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        self.x = re.findall("if", archivo)
        print "IF's"
        print(self.x)
    def obtenSaltos(self):
        self.file = open('Area.c', mode='r')
        archivo = self.file.read()
        self.x = re.findall("\n+", archivo)
        print "SAltos de Linea"
        print(len(self.x))



"""INSTANCIAS"""
l = Lexer()

'''Reconocimiento de Identificadores'''
#l.obtenIdentificadores()

'''Reconocimiento de Enteros'''
#l.obtenEnteros()

'''Reconocimiento de Reales'''
#l.obtenReales()

'''Reconocimiento de comentarios'''
#l.obtenComentarios()

'''Operadores Aritmeticos'''
#l.obtenAritmeticos()

'''Operadores Logicos'''
#l.obtenLogicos()

'''Obtener For'''
l.obtenFor()
'''Obtener IF'''
l.obtenIf()
'''Obtener Saltos'''
l.obtenSaltos()


