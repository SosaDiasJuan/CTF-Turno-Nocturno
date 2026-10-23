# Manual de ejecución — Turno nocturno

## Requisitos
- Un navegador o editor de texto.
- No requiere instalación, servicios, contenedores, credenciales ni conexión a una red.

## Cómo publicar
1. Publicar el directorio del desafío en un repositorio GitHub.
2. Mantener juntos el `README.md` y la carpeta `evidencia/`, respetando sus nombres.
3. El jugador lee el enunciado y analiza los cuatro archivos de evidencia.

## Cómo jugar
1. Leer `README.md`.
2. Correlacionar `auth.log` con `proxy.log` para detectar la sesión anómala.
3. Consultar `nota_operador.txt` para obtener el procedimiento de recuperación.
4. Decodificar el contenido Base64 de `paquete.txt` y aplicar XOR byte a byte con la clave indicada.
5. La salida resultante contiene la flag.

## Validación del desafío
La solución esperada está documentada en `writeup.md`. Para una evaluación sin spoilers, se recomienda entregar el enunciado y las evidencias al jugador, y compartir el manual y el write-up por separado con el docente.
