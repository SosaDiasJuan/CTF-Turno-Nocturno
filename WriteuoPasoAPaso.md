## Paso a paso detallado:
## Cómo resolver el ctf:

1) Se necesita encontrar algo que nos llame la atención, para ello el ctf tiene dentro de la carpeta evidencia, un archivo auth.log.
Podemos ver que 23:48 de la noche existieron intentos fallidos a loguearse desde la IP: 185.77.12.90, pero luego la misma ip pudo ingresar como svc-report.

2) Después se debe revisar en la misma carpeta el archivo proxy.log para ver qué hizo  ese usuario.
A las 23:50 aparece una solicitud /api/export?format=raw con código HTTP 200
Y un segundo después descarga /download?id=8472, también con código 200.
(Los registros coinciden con lo que nos parece sospechoso desde el incio, aunque podría no significar nada si no estamos atentos).

3) Al abrir el archivo nota_operador.tx, la nota indica que el contenido está codificado en Base 64 y que se debe aplicar un XOR contando los caracteres posteriores al guión del nombre del archivo.
El ususario sospechoso recordamos que figuraba como: svc-report, osea que la palabra posterior es report, que tiene 6 caracteres, osea sería un XOR con el número decimal 6.

4) Decodificando el contenido, se abre el paquete.txt, copiamos esa cadena Base64 sin los comentarios:
YGpnYX1laXR0Y2pnZW9paFl/WX5pdFk2MHs=
Para eso utilizaremos el script en Python, que nos dará la flag.

5) Al ejecutar el archivo creado:
Al ejecutar:
python Solution.py 

Obtenemos la flag flag{correlacion_y_xor_06}