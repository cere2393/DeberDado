from random import randint


def verificar_dado(puntuacion, valor_dado):
    if valor_dado == 1:
        return 0
    else:
        return puntuacion + valor_dado


def mostrar_tabla(puntuacion_jugador, puntuacion_computadora):
    print()
    print("#" * 20)
    print(f"Puntuación del Jugador: {puntuacion_jugador}")
    print(f"Puntuación de la Computadora: {puntuacion_computadora}")
    print("#" * 20)
    print()


puntuacion_jugador = 0
puntuacion_computadora = 0

mensaje_bienvenida = """
          ¡Bienvenido a 'Pig', un juego de dados!
    
    En este juego, un usuario y un oponente computarizado 
    lanzan un dado de 6 caras cada ronda. Si el valor del
    dado es 1, el jugador que lo lanzó pierde todos sus
    puntos. De lo contrario, el jugador suma el valor del
    dado a sus puntos. ¡El primer jugador que llegue a 30
    puntos gana!
"""

print(mensaje_bienvenida)

nombre_usuario = input("¿Cuál es tu nombre? ")

while True:
    input(f"Presiona 'Enter' para lanzar el dado {nombre_usuario}!\n")

    valor_dado_jugador = randint(1, 6)
    print(f"{nombre_usuario} lanza un {valor_dado_jugador}")

    valor_dado_computadora = randint(1, 6)
    print(f"Computadora lanza un {valor_dado_computadora}")

    puntuacion_jugador = verificar_dado(puntuacion_jugador, valor_dado_jugador)
    puntuacion_computadora = verificar_dado(puntuacion_computadora, valor_dado_computadora)

    mostrar_tabla(puntuacion_jugador, puntuacion_computadora)

    if puntuacion_jugador >= 30:
        print(f"¡{nombre_usuario} gana!")
        break
    elif puntuacion_computadora >= 30:
        print("¡Computadora gana!")
        break
