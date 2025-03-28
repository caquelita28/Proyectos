from inputs import eleccion_usuario
from dibujos import dibujos_lista
from random import choice
import os

def logica(usuario, maquina, puntuacion_usuario, puntuacion_maquina):
    if usuario == "Piedra" and maquina == "Tijera":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif usuario == "Piedra" and maquina == "Lagarto":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif maquina == "Piedra" and usuario == "Tijera":
        puntuacion_maquina += 1
        print("Maquina gana")
    elif maquina == "Piedra" and usuario == "Lagarto":
        puntuacion_maquina += 1
        print("Maquina gana")


    if usuario == "Papel" and maquina == "Piedra":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif usuario == "Papel" and maquina == "Spock":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif maquina == "Papel" and usuario == "Piedra":
        puntuacion_maquina += 1
        print("Maquina gana")
    elif maquina == "Papel" and usuario == "Spock":
        puntuacion_maquina += 1
        print("Maquina gana")


    if usuario == "Tijera" and maquina == "Papel":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif usuario == "Tijera" and maquina == "Lagarto":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif maquina == "Tijera" and usuario == "Papel":
        puntuacion_maquina += 1
        print("Maquina gana")
    elif maquina == "Tijera" and usuario == "Lagarto":
        puntuacion_maquina += 1
        print("Maquina gana")

    if usuario == "Lagarto" and maquina == "Spock":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif usuario == "Lagarto" and maquina == "Papel":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif maquina == "Lagarto" and usuario == "Spock":
        puntuacion_maquina += 1
        print("Maquina gana")
    elif maquina == "Lagarto" and usuario == "Papel":
        puntuacion_maquina += 1
        print("Maquina gana")

    if usuario == "Spock" and maquina == "Tijera":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif usuario == "Spock" and usuario == "Piedra":
        puntuacion_usuario += 1
        print("Usuario gana")
    elif maquina == "Spock" and usuario == "Tijera":
        puntuacion_maquina += 1
        print("Maquina gana")
    elif maquina == "Spock" and usuario == "Piedra":
        puntuacion_maquina += 1
        print("Maquina gana")

    elif usuario == maquina:
        print("Empate")



    return puntuacion_usuario, puntuacion_maquina



def replay():
    desicion = input("""
    ¿Quieres seguir jugando? (S/N) """).capitalize() # si

    if desicion == "S":
        os.system("cls")
        jugar()

    else:
        exit()

    


def jugar():
    dibujos = dibujos_lista
    opciones = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]
    puntuacion_usuario = 0
    puntuacion_maquina = 0
    puntuacion_maquina_2 = 0
    print("BIENVENID@, éste el juego de Piedra, Papel, Tijera, Lagarto , Spock. Vamos a jugar al mejor de 3")
    

    opcion_juego = int(input("""
    1 - Juego contra máquina 
    2 - Juego automático. """))

    if opcion_juego == 1:

        while True:
            # USUARIO
            input_usuario = eleccion_usuario()
            numero_dibujo = opciones.index(input_usuario)
            print(dibujos[numero_dibujo])


            # MAQUINA
            opcion_maquina = choice(opciones)
            print(f"Opcion maquina: {opcion_maquina}")
            numero_dibujo_maquina = opciones.index(opcion_maquina)
            print(dibujos[numero_dibujo_maquina])
            
            puntuacion_usuario, puntuacion_maquina = logica(input_usuario, opcion_maquina, puntuacion_usuario, puntuacion_maquina)
            print(f"""
    Jugador:{puntuacion_usuario}
    Maquina:{puntuacion_maquina}            
    """)

            if puntuacion_usuario == 2 or puntuacion_maquina == 2:
                if puntuacion_usuario > puntuacion_maquina:
                    print("ENHORABUENA!! usuario gana partida")
                else:
                    print("IA gana partida")
                
                replay()
                break
    
    elif opcion_juego == 2:

        while True:
           

            # MAQUINA1
            opcion_maquina = choice(opciones)
            print(f"Opcion maquina: {opcion_maquina}")
            numero_dibujo_maquina = opciones.index(opcion_maquina)
            print(dibujos[numero_dibujo_maquina])

            # MAQUINA2
            opcion_maquina_2 = choice(opciones)
            print(f"Opcion maquina: {opcion_maquina_2}")
            numero_dibujo_maquina_2 = opciones.index(opcion_maquina_2)
            print(dibujos[numero_dibujo_maquina_2])
            
            puntuacion_maquina, puntuacion_maquina_2 = logica(opcion_maquina, opcion_maquina_2, puntuacion_maquina, puntuacion_maquina_2)
            print(f"""
    Maquina1:{puntuacion_maquina}
    Maquina2:{puntuacion_maquina_2}            
    """)
            input("Pulsa para continuar.")

            if puntuacion_maquina == 2 or puntuacion_maquina_2 == 2:
                if puntuacion_maquina > puntuacion_maquina_2:
                    print("ENHORABUENA!! máquina1 gana partida")
                else:
                    print("Máquina2 gana partida")
                
                replay()
                break

    


def main():
    jugar()


main()