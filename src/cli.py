from src.ride import Ride
from src.logger import get_logger
from src.storage import save_ride, load_rides
from src.config import load_fares
from datetime import datetime

def format_datetime(datetime_text):
    datetime_object = datetime.fromisoformat(datetime_text)

    return datetime_object.strftime("%d/%m/%Y %H:%M")

def run_cli():
    fares = load_fares()
    logger = get_logger()
    ride = None

    while True:
        print("\nTaxímetro")
        print("n - Nueva carrera")
        print("m - En movimiento")
        print("s - Parado")
        print("f - Finalizar carrera")
        print("h - Historial de carreras")
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

                save_ride(ride.to_dict())
                logger.info("Carrera guardada en rides.json")

        elif option == "h":
            rides = load_rides()

            if not rides:
                print("No hay carreras guardadas.")
            else:
                print("\nHistorial de carreras")

                for index, ride_data in enumerate(rides, start=1):
                    started_at = format_datetime(ride_data["started_at"])
                    total = ride_data["total"]
                    segments = ride_data["segments"]
                    duration = get_total_duration(ride_data)
                    formatted_duration = format_duration(duration)

                    print(f"\n{index}. Inicio: {started_at}")
                    print(f"   Total: {total:.2f}€")
                    print(f"   Duración: {formatted_duration}")
                    print("   Tramos:")

                    for segment in segments:
                        status = segment["status"]
                        seconds = segment["seconds"]

                        print(f"   - {status}: {seconds:.2f} segundos")
                    
                    summary = get_history_summary(rides)

                    print("\nResumen")
                    print(f"Carreras: {summary['total_rides']}")
                    print(f"Duración total: {format_duration(summary['total_duration'])}")
                    print(f"Importe total: {summary['total_amount']:.2f}€")

        else:
            print("Opción no implementada todavía")

def get_total_duration(ride_data):
    total_seconds = 0.0

    for segment in ride_data["segments"]:
        total_seconds += segment["seconds"]

    return total_seconds

def format_duration(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = int(seconds % 60)

    return f"{hours}h {minutes}m {remaining_seconds}s"

def get_history_summary(rides):
    total_rides = len(rides)
    total_duration = 0.0
    total_amount = 0.0

    for ride_data in rides:
        for segment in ride_data["segments"]:
            total_duration += segment["seconds"]

        total_amount += ride_data["total"]

    return {
        "total_rides": total_rides,
        "total_duration": total_duration,
        "total_amount": total_amount,
    }

if __name__ == "__main__":
    run_cli()