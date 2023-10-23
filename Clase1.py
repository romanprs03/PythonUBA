import math
import random
from queue import Queue
from queue import LifoQueue

def imprimir_hola_mundo() -> None: 
    print ("Hola Mundo")

# Ejercicio 1.1 CP:

def perimetro() -> float:
    return 2 * math.pi

# Ejercicio 2.4 CP:

def es_multiplo_de (x: int, y: int) -> bool:
    return x % y == 0

# Ejercicio 2.4 CP:

def es_nombre_largo (string) -> bool:
    return len(string) >= 3 and len(string) <= 8

# Ejercicio 5.1 CP:

def devolver_el_doble_si_es_par (x:int) -> int:
    if x % 2 == 0: 
        x = x * 2
    return x

# Ejercicio 6.2 CP:

def numeros_pares_entre_10_y_40() -> None: 
    x: int = 10
    while x <= 40:
        print (x)
        x += 2 

# Ejercicio 7 CP: (uso 41 ya que no se incluye el último)

def ejercicio_anterior_usando_for_num_in_range() -> None:
    for i in range (10,41,2):
         print (i)

###################### GUIA 6 ###################### 

# Ejercicio 1.1 (hecho antes)

# Ejercicio 1.2

def imprimir_un_verso() -> None:
    print ("Magia Veneno \nDe lo oscuro hacia la luz, todo nuevo \nRespirarse, emborrachar \nMorir y seguir viviendo \nVeo en partes lo que tu ves")

# Ejercicio 1.3

def raiz_de_2() -> float:
    x = 2 ** (1/2) 
    return round (x, 4)

# Ejercicio 1.4 

def factorial_de_2() -> int:
    x: int = 2
    return x * (x - 1) 

# Ejercicio 1.5 (hecho antes)

# Ejercicio 2.1 

def imprimir_saludo (str) -> str:
    print ("Hola " + str)

# Ejercicio 2.2

def raiz_cuadrada_de (numero:int) -> float:
    return numero ** (1/2)

# Ejercicio 2.3

def fahrenheit_a_celsius (temperatura:float) -> float:
    return ((temperatura - 32) * 5) / 9

# Ejercicio 2.4

def imprimir_dos_veces (str) -> str:
    return (str + " ") * 2

# Ejercicio 2.5 (hecho)

# Ejercicio 2.6 

def es_par (numero:int) -> bool:
    return numero % 2 == 0

# Ejercicio 2.7 

def cantidad_de_pizzas (comensales:int, min_cant_de_porciones:int) -> int:
        return math.ceil (comensales / (8 / min_cant_de_porciones))

# Ejercicio 3.1

def algunos_es_0 (num1:float, num2:float) -> bool:
    return num1 == 0 or num2 == 0

# Ejercicio 3.2

def ambos_son_0 (num1:float, num2:float) -> bool:
    return num1 == 0 and num2 == 0

# Ejercicio 3.3 (hecho antes)

# Ejercicio 3.4 

def es_bisiesto (año:int) -> bool:
    return año % 4 == 0 

# Ejercicio 4

def peso_pino (altura:float) -> float:
    altura = altura * 100
    if altura <= 300:
        return altura * 3
    else:
        return ((altura - 300) * 2 + 900)

def es_peso_util (peso:float) -> bool:
    return peso >= 400 and peso <= 1000
    
def sirve_pino (altura:float) -> bool:
    return es_peso_util (peso_pino(altura))

# def peso_pino (altura:float) -> float:
    # min(3, altura) * 300 + max(0, altura-3) * 200 (hecho por el profe)

# Ejercicio 5.1 (hecho antes)

# Ejercicio 5.2 

def devolver_valor_si_es_par_sino_el_que_sigue (numero:int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1
    
# return numero if numero % 2 == 0 else numero (hecho por el profe)

# Ejercicio 5.3

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero:int) -> int:
    if numero % 9 == 0:
        return numero * 3
    if numero % 3 == 0:
        return numero * 2
    else:
        return numero
    
# Ejercicio 5.4

def lindo_nombre (str) -> str:
    if len(str) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
# Ejercicio 5.5

def el_rango (numero:int) -> str:
    if numero < 5:
        return "Menor a 5"
    if numero > 10 and numero < 20:
        return "Entre 10 y 20"
    if numero > 20:
        return "Mayor a 20"
    else:
        return "Su número no está en ningún rango conocido"
    
# Ejercicio 5.6

def vacaciones_o_trabajo (sexo:str, edad:int) -> str:
    if edad < 18:
        return "Andá de vacaciones"
    if edad >= 60 and sexo == "F":
        return "Andá de vacaciones"
    if edad >= 65 and sexo == "M":
        return "Andá de vacaciones"
    else:
        return "Te toca trabajar"

# Ejercicio 6.1

def numeros_del_1_al_10() -> None:
    x:int = 1
    while x <= 10:
        print (x)
        x += 1

# Ejercicio 6.2 (hecho antes)

# Ejercicio 6.3 

def imprimir_eco_10_veces() -> None:
    x:int = 1
    while x <= 10:
        print ("eco")
        x += 1

# Ejercicio 6.4

def cuenta_regresiva (inicio:int) -> None:
    while inicio >= 1:
        print (inicio)
        inicio -= 1
    print ("Despegue")

# Ejercicio 6.5

def viajes_en_el_tiempo (partida:int, llegada:int) -> str:
    while partida > llegada:
        print ("Viajó un año al pasado, estamos en el año " + str(partida - 1)) 
        partida -= 1

# Ejercicio 6.6

def viajes_en_el_tiempo_aristoteles (partida:int) -> str:
    while partida > 384:
        print ("Viajó veinte años al pasado, estamos en el año " + str(partida - 20)) 
        partida -= 20

# Ejercicio 7.1 

def numeros_del_1_al_10_7() -> None:
    for x in range (1,11,1):
        print (x)

# Ejercicio 7.2

def numeros_pares_entre_10_y_40_7() -> None: 
    for x in range (10,42,2):
        print (x)

# Ejercicio 7.3

def imprimir_eco_10_veces_7() -> None:
    for x in range (1,11,1):
        print ("eco")

# Ejercicio 7.4

def cuenta_regresiva_7 (inicio:int) -> None:
    for inicio in range (inicio, 0, -1):
        print (inicio)
    print ("Despegue")

# Ejercicio 7.5

def viajes_en_el_tiempo_7 (partida:int, llegada:int) -> str:
    for partida in range (partida, llegada, -1):
        print ("Viajó un año al pasado, estamos en el año " + str(partida - 1)) 

# Ejercicio 7.6

def viajes_en_el_tiempo_aristoteles_7 (partida:int) -> str:
    for partida in range (partida, 384, -1):
        print ("Viajó veinte años al pasado, estamos en el año " + str(partida - 20)) 

# ------------------------------ GUIA 7 ------------------------------

# Ejercicio 1.1

def pertenece (lista:list, numero:int) -> bool:
    i:int = (len(lista) - 1)
    while numero != lista [i] and i != -1:
        i -= 1
    if i == -1:
        return False
    else:
        return True

# Ejercicio 1.2

def divideATodos (lista:list, numero:int) -> bool:
    for num in lista:
        if num % numero != 0:
            return False
    return True
    
# Ejercicio 1.3

def sumaTotal (lista:list) -> int:
    total:int = 0 
    for num in lista:
        total += num
    return total

# Ejercicio 1.4

def ordenados (lista:list) -> bool:
    i:int = len(lista)-1 
    for posicion in range (0,i,1):
        if lista[posicion] > lista[posicion + 1]:
            return False
    return True
        
# Ejercicio 1.5

def palabraLarga (lista:[str]) -> bool:
    for palabra in lista:
        if len(palabra) >= 7:
            return True
    return False

def palabraLargaMal (lista:list) -> bool:
    i:int = len(lista) 
    for posicion in range (0,i,1):
        if len(lista[posicion]) >= 7:
            return True
    return False

# Ejercicio 1.6

def palindromo (palabra:str) -> bool:
    inicio:int = 0
    final:int = len(palabra)-1
    while(inicio != final and inicio < final):
        if(palabra[inicio] != palabra[final]):
            return False
        inicio += 1
        final -=1
    
    return True

# Ejercicio 1.7

def contraseña (palabra:str) -> str:
    if len(palabra) > 8 and tieneMinusculas(palabra) and tieneMayusculas(palabra) and tieneNumeros(palabra):
        return "Verde"
    elif len(palabra) < 5:
        return "Rojo"
    else:
        return "Amarillo"

def tieneMinusculas (palabra:str) -> bool:
    for letra in palabra:
        if letra.islower():
            return True
    return False

def tieneMayusculas (palabra:str) -> bool:
    for letra in palabra:
        if letra.isupper():
            return True
    return False

def tieneNumeros (palabra:str) -> bool:
    for letra in palabra:
        if letra.isnumeric():
            return True
    return False

# Ejercicio 1.8

def cuentaBancaria (operaciones:list) -> int:
    saldo:int = 0
    operacion:[(str,int)]
    for operacion in operaciones:
        if operacion[0] == "I":
            saldo += operacion[1]
        else:
            saldo += operacion[1]
    return saldo

# Ejercicio 1.9

def vocales (palabra:str) -> bool:
    contador:int = 0
    vocales:str = ["a","e","i","o","u"]
    for letra in palabra:
        if letra.lower() in vocales:
            contador += 1
            vocales.remove(letra.lower())
     
    return contador >= 3 

# Ejercicio 2.1

def listaSinPares (lista:list) -> list:
    for i in range (0, len(lista)):
        if i % 2 == 0:
            lista[i] = 0
    return lista

# Ejercicio 2.2

def listaSinPares2 (lista:list) -> list:
    listaPiola:list = []
    for i in range (0, len(lista)):
        if i % 2 == 0:
            listaPiola.append(0)
        else:
            listaPiola.append(lista[i])
    return listaPiola

# Ejercicio 2.3

def quitarVocales (palabra:str) -> str:
    vocales:str = ["a", "e", "i", "o", "u"]
    for letra in palabra:
        if letra.lower() in vocales:
            palabra = palabra.replace(letra, "")
    return palabra

# Ejercicio 2.4

def reemplazarVocales (palabra:str) -> str:
    vocales :str = ["a", "e", "i", "o", "u"]
    for letra in palabra:
        if letra.lower() in vocales:
            palabra = palabra.replace(letra, "_")
    return palabra
    
# Ejercicio 2.6

def eliminarRepetidos (palabra:str) -> str:
    for letra in palabra:
        if repetido(letra, palabra):
           palabra = palabra.replace(letra, "")
    return palabra
    
def repetido(letra: str, palabra: str) -> bool:
    if letra in palabra:
        lista_de_caracteres = list(palabra)
        lista_de_caracteres.remove(letra)
        return letra in lista_de_caracteres
    else:
        return False

# Ejercicio 3

def aprobado (notas:list) -> int:
    promedio:float = sumaTotal(notas)/len(notas)
    if promedio >= 7 and min(notas) > 4:
        return 1
    elif promedio >= 4 and promedio < 7 and min(notas) > 4:
        return 2
    else:
        return 3
    
# Ejercicio 4.1

def listaEstudiantes () -> list: 
    estudiantes:list = []
    print ("Escriba los nombres de sus estudiantes y cuando finalice escriba 'listo'")
    while True:
        nombre = input()
        estudiantes.append(nombre)
        if nombre == "listo":
            break
    return estudiantes
    
# Ejercicio 4.2

def monederoElectronico () -> list:
    monedero:list = []
    print ("Indicque que operacion desea realizar")
    while True:
        accion = input()
        if accion == "C":
            print ("Indique el monto que desea cargar")
            monto = input()
            monedero.append(("C", monto))
            print ("Indicque que operacion desea realizar")
        elif accion == "D":
            print ("Indique el monto que desea descargar")
            monto = input ()
            monedero.append(("D", monto))
            print ("Indicque que operacion desea realizar")
        elif accion == "X":
            break
        else:
            print("Introduzca C, D o X")
    return monedero

# Ejercicio 4.3

def darNuevaCarta () -> int:
    return random.choice((1,2,3,4,5,6,7,10,11,12))

def sieteYMedio () -> list:
    cartasAcumuladas:float = 0
    historialDeCartas:list = []
    nuevaCarta:int = darNuevaCarta()
    figuras:list = [10,11,12]
    historialDeCartas.append(nuevaCarta)
    print ("Comienza el juego")
    print (nuevaCarta)
    if nuevaCarta in figuras:
        cartasAcumuladas += 0.5
    else:
        cartasAcumuladas += nuevaCarta
    while cartasAcumuladas < 7.5:
        nuevaCarta = darNuevaCarta()
        print ("¿Desea sacar otra carta? (S o N)")
        respuesta = input()
        if respuesta == "S":
            print (nuevaCarta)
            historialDeCartas.append(nuevaCarta)
            if nuevaCarta in figuras:
                cartasAcumuladas += 0.5
            else:
                cartasAcumuladas += nuevaCarta
        elif respuesta == "N":
            break
        else:
            print ("Introduzca S o N")
    if cartasAcumuladas <= 7.5:
        print ("Usted suma " + str(cartasAcumuladas))
    else:
        print ("Ha perdido :(")
    return historialDeCartas    

# Ejercicio 5.1

def perteneceACadaUno (listaDeListas:list, numero:int) -> list:
    respuestas:list = []
    while 0 != len(listaDeListas):
        respuestas.append(pertenece(listaDeListas[0], numero))
        listaDeListas.remove(listaDeListas[0])
    return respuestas

# ------------------------------ GUIA 8 ------------------------------

# Ejercicio 1

# Ejercicio 2

def es_un_comentario (linea:str) -> bool:
    for caracter in linea: 
        if caracter != " ":
            if caracter == "#":
                return True
            else:
                return False

def clonarSinComentarios (nombre_archivo: str) -> None:
    archivo = open(nombre_archivo, "r")
    nombre_archivo_output:str = "sinComentarios.txt"
    archivo_output = open(nombre_archivo_output, "w")
    for line in archivo.readlines():
        if not es_un_comentario(line):
            archivo_output.write(line)

    archivo.close()
    archivo_output.close()

# Ejercicio 10

def buscarElMaximo (p: LifoQueue) -> int:
    valor:int = p.get()
    while not p.empty():
        siguiente_valor = p.get()
        valor = max (siguiente_valor, valor)
    return valor

# Ejercicio 16.1

def armarSecuencideBingo() -> Queue:
    lista: list = list(range(0,100))
    random.shuffle(lista)
    bolillero: Queue = Queue()
    for bolilla in lista:
        bolillero.put(bolilla)
    return bolillero

def jugarCartonDeBingo (carton:list, bolillero:Queue) -> int:
    jugadas:int = 0
    casillas_completas:int = 0
    while not bolillero.empty():
        bola = bolillero.get()
        jugadas += 1
        if bola in carton:
            casillas_completas += 1
        if casillas_completas == len(carton):
            return jugadas
        
bolillero = armarSecuencideBingo()

# Ejercicio 19

def agruparPorLongitud (nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo, "r")
    diccionario = {}
    for line in archivo.readlines():
        for palabra in line.split():
            if len(palabra) in diccionario:
                diccionario[len(palabra)] += 1
            else:
                diccionario[len(palabra)] = 1
    return diccionario
        