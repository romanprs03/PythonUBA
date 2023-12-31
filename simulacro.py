# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

# Hechos por mí:

#def ultima_aparicion(s: list, e: int) -> int:
#    recorro_posiciones: int = 1
#    longitud_de_lista: int = len(s)
#    for elemento in reversed(s):
#        if elemento != e:
#            recorro_posiciones += 1
#        else:
#            if recorro_posiciones == longitud_de_lista:
#                return 0
#            elif recorro_posiciones >= round(longitud_de_lista/2) or recorro_posiciones == 1:
#                posicion = longitud_de_lista - recorro_posiciones + 1
#                return posicion
#            else:
#                posicion = longitud_de_lista - recorro_posiciones 
#                return posicion
#    return 0

#def reversed_mio (lista: list) -> list:
#    lista_revertida: list = []
#    lista_aux: list = []
#    for elemento in lista:
#        lista_aux.append(elemento)
#    while lista != []:
#        lista_revertida.append(lista[-1])
#        lista.remove(lista[-1])
#    for elemento in lista_aux:
#        lista.append(elemento)
#    return lista_revertida


#def ultima_aparicion(s: list, e: int) -> int:
#    cantidad_de_apariciones = 0
#    recorro_posiciones = 0
#    for elemento in s:
#        if elemento == e:
#            cantidad_de_apariciones += 1
#    while cantidad_de_apariciones != 0:
#        if s[0] != e:
#            recorro_posiciones += 1
#            s.remove(s[0])
#        elif s[0] == e and cantidad_de_apariciones != 0:
#            recorro_posiciones += 1
#            cantidad_de_apariciones -= 1
#            s.remove(s[0])
#    
#    return recorro_posiciones - 1

# Hechos por el profe

#def ultima_aparicion(s: list, e: int) -> int:
#    cantidad_de_apariciones = 0
#    for elemento in s:
#        if elemento == e:
#            cantidad_de_apariciones += 1
#    for i in range(len(s)):
#        if s[i] == e:
#            cantidad_de_apariciones -= 1
#        if cantidad_de_apariciones == 0:
#           return i   
        
def ultima_aparicion(s: list, e: int) -> int:
    res: int = 0
    for i in range(len(s)):
        if s[i] == e:
            res = i
    return res
                
##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def elementos_exclusivos(s: list, t: list) -> list:
    res: list = []
    for elemento in s:
        if elemento not in t and elemento not in res:
            res.append(elemento)
    for elemento in t:
        if elemento not in s and elemento not in res:
            res.append(elemento)
    return res

##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res: int = 0
    for key, value in ingles.items():
        if key in aleman.keys() and value == aleman[key]:
            res += 1
    return res

##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def lista_particular (lista: list, n: int) -> list:
    nueva_lista = []
    for elemento in lista:
         if elemento == n:
             nueva_lista.append(n)
    return nueva_lista

def convertir_a_diccionario(lista: list) -> dict:
    nueva_lista: list = []
    diccionario : dict = {}
    for elemento in lista:
        if lista_particular(lista, elemento) not in nueva_lista:
            nueva_lista.append(lista_particular(lista, elemento))
    for elemento in nueva_lista:
        diccionario[elemento[0]] = len(elemento)
    return diccionario
