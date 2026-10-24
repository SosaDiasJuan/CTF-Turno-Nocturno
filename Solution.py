import base64

dato = base64.b64decode("YGpnYX1laXR0Y2pnZW9paFl/WX5pdFk2MHs=")
resultado = bytes(b ^ 6 for b in dato)

print(resultado.decode("utf-8"))