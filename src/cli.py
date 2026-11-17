from src.ride import Ride
from src.logger import get_logger

def run_cli():
    fares = {
        "stopped": 0.02,
        "moving": 0.05,
    }
    logger = get_logger()
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
            logger.info("Carrera iniciada")

        elif option == "m":
            if ride is None:
                print("No hay una carrera activa. Pulsa n para iniciar una.")
                logger.warning("Intento de movimiento sin carrera activa")
            else:
                ride.set_status("moving")
                print("Taxi en movimiento")
                logger.info("Estado cambiado a moving")

        elif option == "s":
            if ride is None:
                print("No hay una carrera activa. Pulsa n para iniciar una.")
                logger.warning("Intento de parada sin carrera activa")
            else:
                ride.set_status("stopped")
                print("Taxi parado")
                logger.info("Estado cambiado a stopped")

        elif option == "f":
            if ride is None:
                print("No hay una carrera activa. Pulsa n para iniciar una.")
                logger.warning("Intento de finalización sin carrera activa")
            elif ride.finished:
                print("La carrera ya ha finalizado.")
                logger.warning("Intento de finalizar una carrera ya finalizada")
            else:
                total = ride.finish()
                print(f"Total de la carrera: {total:.2f}€")
                logger.info(f"Carrera finalizada. Total: {total:.2f}€")

        else:
            print("Opción no implementada todavía")
        
if __name__ == "__main__":
    run_cli()