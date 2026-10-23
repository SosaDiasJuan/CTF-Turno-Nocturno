# CTF: Turno nocturno

**Categoría:** Forense / Criptografía  
**Dificultad:** Media  
**Modalidad:** Offline, basado en archivos

## Historia

Durante una guardia nocturna, el equipo de seguridad detectó accesos extraños a un servidor interno. El atacante no dejó un archivo llamado `flag.txt`: hay que correlacionar los registros, identificar la sesión comprometida y recuperar el dato que se llevó.

Tenés los archivos de la carpeta `evidencia/`. No hace falta conectarse a ningún sistema ni instalar herramientas. Se puede resolver leyendo los archivos con un editor de texto y usando las funciones de decodificación disponibles en cualquier entorno habitual.

## Objetivo

Encontrá la flag con formato `flag{...}`.

## Archivos

- `evidencia/auth.log`: inicios de sesión y eventos de autenticación.
- `evidencia/proxy.log`: solicitudes HTTP registradas por el proxy.
- `evidencia/nota_operador.txt`: una nota dejada por el administrador.
- `evidencia/paquete.txt`: contenido recuperado de una solicitud sospechosa.

## Reglas

- Todo lo necesario para resolver el reto está incluido en estos archivos.
- No se necesita escanear ni atacar ningún sistema.
- La flag debe obtenerse a partir de las evidencias, no adivinarse.

