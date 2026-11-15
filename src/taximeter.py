def calculate_total(ride_segments, fares):
    """
    Calcula el importe total de una carrera.

    ride_segments: lista de tramos.
    fares: dicionarrio con las tarifas por segundo.

    Ejemplo de tramo:
    {"status": "stopped", "seconds": 20}
    """
    total = 0
    for segment in ride_segments:
        status = segment["status"]
        seconds = segment["seconds"]

        if status == "stopped":
            rate = fares["stopped"]
        elif status == 'moving':
            rate = fares["moving"]
        else:
            raise ValueError(f"Estado no válido: {status}")
        segment_cost = seconds * rate
        total += segment_cost

    return total

if __name__ == "__main__":
    segments = [
        {"status": "stopped", "seconds": 20},
        {"status": "moving", "seconds": 30},
    ]

    fares = {
        "stopped": 0.02,
        "moving": 0.05,
    }

    total = calculate_total(segments, fares)
    print(f"Total: {total:.2f}€")