def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\n========================= Turno", turno, "=========================")
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        daño = jugador_1.daño(jugador_2)
        jugador_2.vida -= daño
        print(jugador_1.nombre, "ha realizado", daño, "puntos de daño a", jugador_2.nombre)

        if jugador_2.esta_vivo():
            print("Vida de", jugador_2.nombre, "es", jugador_2.vida)
        else:
            jugador_2.morir()
            break

        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        daño = jugador_2.daño(jugador_1)
        jugador_1.vida -= daño
        print(jugador_2.nombre, "ha realizado", daño, "puntos de daño a", jugador_1.nombre)

        if jugador_1.esta_vivo():
            print("Vida de", jugador_1.nombre, "es", jugador_1.vida)
        else:
            jugador_1.morir()
            break

        turno += 1

    print("\n=========================== Fin ===========================")
    if jugador_1.esta_vivo():
        print("Ha ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("Ha ganado", jugador_2.nombre)
    else:
        print("Empate")
