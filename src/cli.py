from src.ride import Ride


def run_cli():
    fares = {
        "stopped": 0.02,
        "moving": 0.05,
    }

    ride = None

    while True:
        print("\nTaxímetro")
        print("n - Nueva carrera")
        print("m - En movimiento")
        print("s - Parado")
        print("f - Finalizar carrera")
        print("q - Salir")

        option = input("Selecciona una opción: ").strip().lower()

        if option == "q":
            print("¡Hasta pronto!")
            break

        elif option == "n":
            ride = Ride(fares)
            ride.start()
            print("Nueva carrera iniciada")

        elif option == "m":
            if ride is None:
                print("No hay una carrera activa. Pulsa n para iniciar una.")
            else:
                ride.set_status("moving")
                print("Taxi en movimiento")

        elif option == "s":
            if ride is None:
                print("No hay una carrera activa. Pulsa n para iniciar una.")
            else:
                ride.set_status("stopped")
                print("Taxi parado")

        elif option == "f":
            if ride is None:
                print("No hay una carrera activa. Pulsa n para iniciar una.")
            elif ride.finished:
                print("La carrera ya ha finalizado.")
            else:
                total = ride.finish()
                print(f"Total de la carrera: {total:.2f}€")

        else:
            print("Opción no implementada todavía")
        
if __name__ == "__main__":
    run_cli()