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

