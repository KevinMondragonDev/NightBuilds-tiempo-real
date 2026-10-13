"""Fuente de datos del reto «Casi tiempo real»: emite compras sin parar, una por línea (JSON).

No es parte de la solución: es el «mundo exterior» que produce los eventos. Tu
trabajo empieza al recibirlos. Escribe en la salida estándar; conéctalo a tu flujo:

    python generar_eventos.py --por-segundo 5 | python tu_productor.py

A propósito, algunos eventos llegan DUPLICADOS, otros TARDE (su campo `ocurrio_en`
es anterior al momento en que se emiten) y otros MALFORMADOS. Las proporciones se
controlan con las opciones; con --semilla la secuencia es reproducible.
"""

import argparse
import json
import random
import sys
import time
from datetime import datetime, timedelta, timezone

COMERCIOS = ["Walmart", "Toks", "Netflix", "Pemex", "Volaris", "Cinépolis", "CFE", "Soriana"]


def evento(rng: random.Random, numero: int, ahora: datetime, tardios: float) -> dict:
    retraso = timedelta(seconds=rng.randrange(30, 600)) if rng.random() < tardios else timedelta(0)
    monto = rng.lognormvariate(6, 0.9)
    if rng.random() < 0.01:
        monto *= 40  # de vez en cuando, una compra anómala
    return {"evento_id": f"e-{numero:08d}", "cuenta_id": rng.randrange(1, 201),
            "ocurrio_en": (ahora - retraso).isoformat(timespec="seconds"),
            "monto": round(monto, 2), "comercio": rng.choice(COMERCIOS)}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--por-segundo", type=float, default=2.0)
    p.add_argument("--total", type=int, default=0, help="0 = sin límite")
    p.add_argument("--duplicados", type=float, default=0.03)
    p.add_argument("--tardios", type=float, default=0.05)
    p.add_argument("--malformados", type=float, default=0.01)
    p.add_argument("--semilla", type=int, default=None)
    a = p.parse_args()
    rng, numero = random.Random(a.semilla), 0
    try:
        while not a.total or numero < a.total:
            numero += 1
            linea = json.dumps(evento(rng, numero, datetime.now(timezone.utc), a.tardios), ensure_ascii=False)
            if rng.random() < a.malformados:
                linea = linea[: rng.randrange(10, len(linea) - 5)]  # JSON cortado
            print(linea, flush=True)
            if rng.random() < a.duplicados:
                print(linea, flush=True)
            if a.por_segundo > 0:
                time.sleep(1 / a.por_segundo)
    except (BrokenPipeError, KeyboardInterrupt):
        sys.exit(0)


if __name__ == "__main__":
    main()
