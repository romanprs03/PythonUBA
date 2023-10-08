import math

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

def pertenece (lista:list[int], numero:int) -> bool:
    i:int = (len(lista) - 1)
    while numero != lista [i] and i != 0:
        i -= 1
    if i == 0:
        return False
    else:
        return True
