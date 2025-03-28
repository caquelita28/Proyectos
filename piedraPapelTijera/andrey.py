import os
from random import choice
from modules.frames import frames
from modules.inputs import datos_user

def logica(usuario, maquina, puntos_user, puntos_maquina):
    # Opción 1
    if usuario == "Piedra" and maquina == "Tijera":
        print("Gana el usuario")
        puntos_user += 1
    elif maquina == "Piedra" and usuario == "Tijera":
        print("Gana la maquina")
        puntos_maquina += 1

    # Opción 2
    elif usuario == "Papel" and maquina == "Piedra":
        print("Gana el usuario")
        puntos_user += 1

    elif maquina == "Papel" and usuario == "Piedra":
        print("Gana la maquina")
        puntos_maquina += 1

    
    # Opción 3
    elif usuario == "Tijera" and maquina == "Papel":
        print("Gana el usuario")
        puntos_user += 1

    elif maquina == "Tijera" and usuario == "Papel":
        print("Gana la maquina")
        puntos_maquina += 1

    elif usuario == maquina:
        print("Empate")

    return puntos_user, puntos_maquina


def reanudar():
    print("""Quieres seguir jugando? 
0 es no || 1 es sí""")
    opcion = int(input())
    if opcion == 0:
        exit()
    elif opcion == 1:
        os.system('clear')
        juego()
    

def juego():
    opciones = ["Piedra", "Papel", "Tijera"]
    numero_partidas = 3
    puntuacion_user = 0
    puntuacion_maquina = 0
    lista_dibujos = frames
    while True:
        opcion_usuario = datos_user()
        # DIBUJITO
        numero_posicion_dibujito = opciones.index(opcion_usuario)
        print(lista_dibujos[numero_posicion_dibujito])
        opcion_maquina = choice(opciones).capitalize()
        print(f"OPCION MAQUINA: {opcion_maquina}")
        # DIBUJITO
        numero_posicion_dibujito_maquina = opciones.index(opcion_maquina)
        print(lista_dibujos[numero_posicion_dibujito_maquina])
        puntuacion_user, puntuacion_maquina = logica(opcion_usuario, opcion_maquina, puntuacion_user, puntuacion_maquina)

        print(f"""
Usuario: {puntuacion_user}
Maquina: {puntuacion_maquina}
""")

        if puntuacion_user == numero_partidas - 1 or puntuacion_maquina == numero_partidas - 1:
            if puntuacion_user > puntuacion_maquina:
                print("El usuario ha ganado la partida")
            else:
                print("La maquina ha ganado la partida")
            
            reanudar()


def main():
    juego()


main()