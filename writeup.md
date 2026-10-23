# Write-up: Turno nocturno

Análisis Forense / Criptografía  

## 1. Revisar los accesos

En `auth.log` aparecen intentos fallidos desde `185.77.12.90` y, unos segundos después, un acceso exitoso para `svc-report` desde esa misma IP. Es el evento más sospechoso.

Luego la cuenta ejecuta `tar` sobre `/srv/reports`, lo que podría explicar la preparación de un paquete para extraer información.

## 2. Correlacionar con el proxy

En `proxy.log`, la cuenta `svc-report` realiza un POST a `/api/export?format=raw` con código `200` a las 23:50:44 y descarga el recurso `id=8472` un segundo después. Coincide temporalmente con la sesión sospechosa.

## 3. Recuperar el contenido

`paquete.txt` indica que el contenido está codificado en Base64. La nota explica que, después de decodificarlo, hay que aplicar XOR a cada byte.

La cuenta sospechosa es `svc-report`. La parte posterior al guion es `report`, que tiene 6 caracteres. Por lo tanto, la clave XOR decimal es `6`.

## 4. Obtener la flag

1. Copiar únicamente la cadena Base64 de `paquete.txt`.
2. Decodificarla como Base64 para obtener los bytes.
3. Hacer XOR de cada byte con el valor decimal `6`.
4. Interpretar los bytes resultantes como texto.

La flag obtenida es:

`flag{correlacion_y_xor_06}`

## Qué aprendí

El reto combina análisis de registros y una transformación criptográfica simple. La parte importante no era mirar un único archivo, sino relacionar los eventos por hora, usuario e IP. Base64 no cifra el contenido; solo lo representa de otra forma. XOR con una clave pequeña tampoco es un mecanismo seguro, pero sirve como ejercicio para recuperar un mensaje cuando la clave se obtiene de otra evidencia.
