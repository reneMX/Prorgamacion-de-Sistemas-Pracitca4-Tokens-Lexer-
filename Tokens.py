#Practica #3 Reconocimiento  mediante la funcion findall y expresiones regulares
#NOMBRE; Rene Martinez M.
#VERSION: V3.3
#FECHA: Lunes 19 Octubre 2020
#HORA: 19:32

import re
import numpy as np

'''Esta lista no se utiliza por el momento'''
#list_p_reservadas = ['include','stdio','h','float','conio','']

class Lexer():

    '''ATRIBUTOS'''
    #LISTAS
    x               = []
    list_reservadas     = []
    #EXPRESIONES
    exp_identificadores = ""
    exp_enteros         = ""
    exp_reales          = ""
    exp_comentarios     = ""
    exp_aritmeticos     = ""
    exp_logicos         = ""
    exp_fin_linea       = ""



    def __init__(self):
        self.x = list()
        self.file = open('Area.c', mode='r')
        self.list_identi = list()
        self.list_reservadas =[r"main",r"include",r"define",r"struct",r"void",
                               r"break",r"continue",r"default",r"else",r"for",r"if",r"return",r"Auto",
                               r"double",r"int ",r"Break",r"else",r"long",r"switch",r"Case",r"enum",r"register",
                               r"typedef",r"Char",r"extern",r"return",r"union",r"Const",r"float",
                               r"short",r"unsigned",r"signed",r"Default",r"goto",r"sizeof",r"volatile",
                               r"Do",r"static",r"while", r"getch"
                               ]
        self.exp_identificadores = r"[_a-zA-Z][_a-zA-Z0-9 ]{0,30}"
        self.exp_enteros = r"[+|-][\d]+|[\d]+"
        self.exp_reales = r"[\d]+[.][\d]*|[-|+]+[.][\d]*|[-|+]*[.][\d]+|[.][\d]+"
        self.exp_comentarios = r"[/][/|*][a-z |A-Za-z]*[ |*/]*"
        self.exp_aritmeticos = r"[+|-|*|=|/|%]"
        # self.exp_logicos = "[&&|||>|<|>=|<=]+|/"
        self.exp_logicos = r"([|][|])|[>][=]|[<][=]|[&][&]+"
        self. exp_fin_linea = r"\n"



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
        matriz = np.zeros((len(self.list_reservadas),len(self.list_reservadas)))



        archivo = self.file.read()
        #
        # for i in self.list_reservadas:
        #     print(i)
        '''Reconocimiento de Palabras Reservadas'''
        # for elemento in self.list_reservadas:
        #     aux = re.findall(elemento,archivo)
        #     if (len(aux)>0):
        #         self.list_identi.append(aux)
        # print(self.list_identi)

        '''Reconocimiento de Numero de Lineas del archivo'''
        # aux = re.findall("\n",archivo)
        # print(len(aux)+1)

        '''Reconocimiento de la linea donde esta cada Lexema'''


        line_num = 1
        i = 0

        # for elemento in self.list_reservadas:
        #     with open('Area.c') as f:
        #         for linea in f:
        #             aux = re.findall(elemento, linea)
        #             if aux:
        #                 print("Lexema", aux, "Linea ", line_num)
        #
        #
        #
        #         line_num += 1
        #                 # i += 1


        with open('Area.c') as f:
            for linea in f:

                for elemento in self.list_reservadas:
                    list_pr  = re.findall(elemento,linea)
                    if list_pr:
                        print 'PALABRA RESERVADA: {} Linea: {}'.format(list_pr, line_num)

                list_ent = re.findall(self.exp_enteros, linea)
                if list_ent:
                    print 'ENTEROS: {} Linea: {}'.format(list_ent, line_num)

                list_rea = re.findall(self.exp_reales, linea)
                if list_rea:
                    print 'REALES: {} Linea: {}'.format(list_rea, line_num)

                """BUSCAMOS SI HAY COMENTARIOS EN LA LINEA DONDE ESTAMOS"""
                list_comen = re.findall(self.exp_comentarios, linea)
                if list_comen:
                    print 'COMENTARIOS: {} Linea: {}'.format(list_comen, line_num)

                """BUSCAMOS SI HAY OPERADORES ARITMETICOS EN LA LINEA DONDE ESTAMOS"""
                list_arit = re.findall(self.exp_aritmeticos, linea)
                if list_arit:
                    print 'ARITMETICOS: {} Linea: {}'.format(list_arit, line_num)

                """BUSCAMOS SI HAY OPERADORES LOGICOS EN LA LINEA DONDE ESTAMOS"""
                list_log = re.findall(self.exp_logicos, linea)
                if list_log:
                    print 'LOGICOS: {} Linea: {}'.format(list_log, line_num)

                        # diccionario = { aux[i]:line_num}


                line_num += 1
                    # i += 1




    """Numero de Lineas de codigo con re.search"""
    # for elemento in archivo:
    #     aux1 = re.search(r"\n",elemento)
    #     if (aux1 != None):
    #          c += 1
    # print(c+1)





    #...PRUEBAS PARA  IDENTIFICAR LA LINEA DONDE ESTA EL LEXEMA

    # line_num = 1
    # line_start = 0


    #...Integracion de for re.finditer y lista de reservadas

    # for match in re.finditer(self.dameReservadas() | r"\n", archivo):
    #     s = match.start()
    #     e = match.end()
    #     print 'String match "%s" at %d:%d' % (archivo[s:e], s, e)





    #...Impresion de lista de palabras reservadas
    # for i  in range(len(self.list_reservadas)):
    #     print self.list_reservadas[i]





    # for mo in re.finditer(, archivo):
    #
    #     print mo.group()
    #print
    # kind = mo.lastgroup
    # value = mo.group()
    # if value  ==
    # if kind == r"\n":
    #     line_start = mo.end()
    #     line_num += 1
    #     print(line_num)



    # for elemento in self.list_reservadas:
    #     aux1 = re.search(elemento,archivo)
    #     if(aux1 != None):
    #         c += 1
    #
    # print(c)
    #

    # for elemento in re.finditer(self.list_reservadas,archivo):
    #
    #     kind = elemento.lastgroup



    # for elemento in self.list_reservadas:
    #     for match in re.finditer(elemento, archivo):
    #         s = match.start()
    #         e = match.end()
    #         print('Found {!r} at {:d}:{:d}'.format(
    #             archivo[s:e], s, e))


    # def  dameReservadas(self):
    #     for i in range(len(self.list_reservadas)):
    #         return  self.list_reservadas[i]


"""INSTANCIAS"""

l = Lexer()
#l.obtenPractica3()
l.obtenPractica4()



