# ⚡ Reto 5 — Casi tiempo real

**Repositorio:** `NightBuilds-tiempo-real` · **Nivel:** avanzado · **Entorno:** Redis Streams o Kinesis en Floci, S3 y PostgreSQL · **Método y evaluación:** [`README.md`](docs/METODO.md)

## El caso

El equipo antifraude de un banco revisa las compras al día siguiente, cuando el dinero ya salió. Quieren ver lo que pasa **mientras pasa**: cada compra, en segundos, con una señal cuando algo se sale de lo normal. Y todo lo que ocurra debe quedar guardado para analizarlo después.

## Lo que debe existir al terminar

- **La fuente de eventos conectada a tu flujo.** No la escribes tú: `datos/generar_eventos.py` emite compras sin parar, una por línea en JSON, y a propósito incluye duplicados, eventos que llegan tarde y alguno malformado.
- **Un flujo** (Redis Streams o Kinesis) entre quien produce y quien consume.
- **Un consumidor** que calcule agregados por ventanas de tiempo (por ejemplo, gasto por cuenta en el último minuto) y marque lo anómalo con una regla que tú defines.
- **Dos destinos:** una vista «caliente» para consultar al instante y el histórico completo en el data lake.
- **Una API con actualizaciones en vivo** y una **visualización en D3.js que se mueve sola**, sin recargar la página.
- **Una medición:** cuántos segundos pasan desde que ocurre un evento hasta que aparece en pantalla.

## Restricciones

- Si el consumidor se cae y vuelve a arrancar, no pierde eventos ni cuenta ninguno dos veces. Demuéstralo matándolo en vivo.
- Un evento malformado no detiene el flujo: se aparta con su motivo.
- Un evento que llega tarde se suma a **su** ventana, no a la actual, hasta un límite que tú fijas.

## Preguntas que tu diseño debe responder

- ¿Qué es «tarde»? ¿Qué haces con un evento que llega después del límite?
- Hora del evento frente a hora de llegada: ¿cuál usas para las ventanas y por qué?
- ¿Cómo sabe el consumidor por dónde iba al reiniciarse?
- ¿De verdad hacía falta tiempo real? ¿Qué habría costado un lote cada cinco minutos?

## Defensa: lo que te van a preguntar

- Mata el consumidor, espera diez segundos y levántalo. Enséñanos los totales.
- Multiplica por diez el ritmo de eventos. ¿Qué se queda atrás primero?
- ¿Cuántos segundos tarda un evento en verse y de qué depende?

## Súbelo de nivel

- Cambia Redis Streams por Kafka y explica qué ganaste.
- Dos consumidores en paralelo que se reparten el trabajo sin pisarse.
- Une los eventos en vivo con el modelo dimensional del reto 2 para enriquecerlos al vuelo.
