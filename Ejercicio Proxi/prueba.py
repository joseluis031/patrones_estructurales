from proxi import *



carpeta_principal = Carpeta("Principal")
    # Si el archivo no existe, simplemente continuamos con una carpeta vacía
carpeta_principal = Carpeta("Principal")
documento1 = Documentos_Leaf("Documento1", "Texto", 10)
documento2 = Documentos_Leaf("Documento2", "Imagen", 20)
enlace1 = Enlace_Leaf("Enlace1", "http://enlace1.com")
proxy_documento1 = Proxy(documento1)
proxy_documento1.operation()
proxi_documento2 = Proxy(documento2)

proxi_documento2.operation()
carpeta_principal.add(proxy_documento1)
carpeta_principal.add(documento2)

carpeta_principal.add(proxi_documento2)
# Convertir la estructura a JSON
estructura_json = carpeta_principal.to_dict()
print(estructura_json)


