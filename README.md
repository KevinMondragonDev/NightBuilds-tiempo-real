# NightBuilds-tiempo-real

> Compras procesadas casi en tiempo real: flujo de eventos, ventanas de tiempo, detección de anomalías y un tablero en D3.js que se actualiza solo.

**Estado:** 🚧 sin empezar · **Categoría:** NightBuilds · **Tipo:** Procesamiento casi en tiempo real · **Módulo del programa:** 08 · Capstone, reto 5

## Qué significa el nombre

El prefijo del repositorio indica el tamaño del proyecto:

| Prefijo | Tamaño | Qué es |
|---|---|---|
| `DevSandbox-` | Hasta 8 h | Un proyecto pequeño para practicar un tema concreto: un espacio para probar, equivocarse y terminar rápido |
| **`NightBuilds-`** ← este | 8 h o más | Un proyecto grande, con varias piezas (base de datos, orquestación, nube o API) y decisiones de diseño propias |

Este es un **NightBuilds**: es un reto del capstone, un problema abierto que se trabaja en cinco entregas.

## La problemática

El equipo antifraude de un banco revisa las compras al día siguiente, cuando el dinero ya salió. Quiere ver lo que pasa mientras pasa, con una señal cuando algo se sale de lo normal, sin perder eventos ni contarlos dos veces.

## Los datos

| Dónde | Qué es |
|---|---|
| `datos/generar_eventos.py` | Fuente de eventos: emite compras sin parar en JSON, con duplicados, eventos tardíos y malformados. No es parte de la solución |

Los archivos de `datos/` son **sintéticos**, generados para practicar: no corresponden a personas ni a operaciones reales.

## Qué hay que construir

El enunciado completo, con sus hitos y cómo comprobar cada uno, está en [`RETO.md`](RETO.md). No trae solución: el diseño es tuyo.

- [`docs/REGLAS.md`](docs/REGLAS.md): cómo se trabaja un NightBuild y qué debe tener este README al terminar.
- [`docs/RUBRICA.md`](docs/RUBRICA.md): con qué criterios se evalúa.
- [`docs/METODO.md`](docs/METODO.md): cómo se trabaja un reto del capstone (cinco entregas) y qué está comprobado que funciona en local.

## Cómo se ejecuta

*Pendiente: se escribe al cerrar el primer hito. Los comandos exactos, desde `git clone`.*

## Decisiones

*Pendiente: tres decisiones técnicas y la alternativa que se descartó en cada una.*

## Qué aprendí

*Pendiente.*

---

Reto del programa de Python e ingeniería de datos: [UNIR_Python_Certification](https://github.com/KevinMondragonDev/UNIR_Python_Certification).
