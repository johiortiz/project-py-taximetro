import time
from datetime import datetime

class Ride:
    def __init__(self, fares):
        self.fares = fares
        self.status = None
        self.started_at = None
        self.finished_at = None
        self.last_change_at = None
        self.segments = []
        self.finished = False
        self.total = 0.0

    def start(self):
        if self.started_at is not None:
            raise ValueError("La carrera ya ha empezado")
        now = time.monotonic()

        self.status = "stopped"
        self.started_at = now
        self.last_change_at = now
        self.started_at_real = datetime.now()

    def set_status(self, new_status):
        if self.started_at is None:
            raise ValueError("La carrera no ha empezado")

        if self.finished:
            raise ValueError("La carrera ya ha terminado")

        if new_status not in ("stopped", "moving"):
            raise ValueError("Estado no válido")

        elapsed_seconds = time.monotonic() - self.last_change_at

        self.segments.append({
            "status": self.status,
            "seconds": elapsed_seconds,
        })

        self.status = new_status
        self.last_change_at = time.monotonic()

    def finish(self):
        if self.started_at is None:
            raise ValueError("La carrera no ha empezado")

        if self.finished:
            raise ValueError("La carrera ya ha terminado")

        elapsed_seconds = time.monotonic() - self.last_change_at

        self.segments.append({
            "status": self.status,
            "seconds": elapsed_seconds,
        })

        self.finished = True
        self.finished_at_real = datetime.now()

        return self.get_total()
        

    def get_total(self):
        total = 0.0
        for segment in self.segments:
            fare = self.fares[segment["status"]]
            total += segment["seconds"] * fare

        self.total = total
        return self.total

    def to_dict(self):
        return{
                "started_at": self.started_at_real.isoformat(),
                "finished_at": self.finished_at_real.isoformat(),
                "segments": self.segments,
                "total": self.total,
        }
            