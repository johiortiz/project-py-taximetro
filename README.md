# Project Py Taxímetro

Aplicación de consola para calcular el coste de una carrera de taxi.

## Funcionalidades

- Iniciar una nueva carrera.
- Cambiar entre estado parado y en movimiento.
- Finalizar una carrera y calcular su importe.
- Guardar las carreras finalizadas en un archivo JSON.
- Mostrar el historial de carreras, con duración, tramos y resumen.
- Registrar eventos importantes en un archivo de log.
- Leer las tarifas desde un archivo de configuración externo.

## Requisitos

- Python 3.12 o superior.
- pytest para ejecutar los tests.

## Instalación

Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala pytest:

```bash
pip install pytest
```

## Ejecución

Desde la raíz del proyecto:

```bash
python3 -m src.cli
```

## Opciones de la CLI

| Opción | Acción |
|---|---|
| `n` | Inicia una nueva carrera |
| `m` | Cambia el estado a en movimiento |
| `s` | Cambia el estado a parado |
| `f` | Finaliza la carrera y muestra el total |
| `h` | Muestra el historial de carreras |
| `q` | Sale de la aplicación |

## Configuración

Las tarifas se leen desde `config.ini`:

```ini
[fares]
stopped = 0.02
moving = 0.05
```

## Datos generados

- `logs/taximeter.log`: registro de eventos.
- `data/rides.json`: historial de carreras finalizadas.

## Tests

Ejecuta los tests con:

```bash
pytest
```