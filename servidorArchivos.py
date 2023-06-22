import socket
import struct
import re
import io
import os
import xml.etree.ElementTree as ET

def main():
    os.system('cls')
    host = 'localhost'
    puerto = 12345

    try:
        # Conectamos el socket
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((host, puerto))
        servidor.listen(1)
        print('Servidor en espera de conexiones...')

        while True:
            # Aceptamos la conexion del cliente.
            conexion, direccion = servidor.accept()
            print('Cliente conectado:', direccion)

            # Recibe archivos hasta que se envíe "FIN_ARCHIVO"
            while True:
                obtenerArchivosXML(conexion, direccion)
                # Aqui deberiamos de recibir los demas archivos...

            conexion.close()
            print('Cliente desconectado:', direccion)

    except socket.error as e:
        print("Error al iniciar el servidor:", str(e))

    finally:
        servidor.close()

def obtenerArchivosXML(conexion, direccion):
    # Recibe el nombre del archivo.
    nombre_archivo = conexion.recv(1024).decode()
    if not nombre_archivo:
        return

    # Comprueba si se ha alcanzado la condición de salida
    if nombre_archivo == "FIN_ARCHIVO":
        return

    # Recibe la longitud del archivo en 4 bytes.
    longitud_archivo = conexion.recv(4)
    longitud_archivo = struct.unpack('!I', longitud_archivo)[0]

    # Recibe el contenido del archivo en fragmentos
    contenido_archivo = b""
    bytes_recibidos = 0
    while bytes_recibidos < longitud_archivo:
        fragmento = conexion.recv(min(1024, longitud_archivo - bytes_recibidos))
        if not fragmento:
            break
        contenido_archivo += fragmento
        bytes_recibidos += len(fragmento)

    if bytes_recibidos < longitud_archivo:
        print(f"Error al recibir el archivo: {nombre_archivo}")
        return

    # Imprime el nombre y contenido del archivo XML
    print(f"Archivo recibido: {nombre_archivo}")
    print("Contenido:")
    print(contenido_archivo.decode())

    # Genera el archivo XML en el servidor
    generar_archivo_xml(nombre_archivo, contenido_archivo)


def generar_archivo_xml(nombre_archivo, contenido_xml):
    # Crea el árbol XML a partir del contenido recibido
    root = ET.fromstring(contenido_xml)

    # Crea el objeto ElementTree
    tree = ET.ElementTree(root)

    # Elimina los caracteres no imprimibles del nombre del archivo
    nombre_archivo = re.sub(r'[^\x20-\x7E]+', '', nombre_archivo)

    # Genera el nombre del archivo de salida
    #nombre_archivo_salida = nombre_archivo + "_salida.xml"
    nombre_archivo_salida = nombre_archivo

    # Crea un objeto BytesIO para escribir el contenido XML
    output = io.BytesIO()
    tree.write(output, encoding='utf-8', xml_declaration=True)

    # Obtiene los bytes del objeto BytesIO
    xml_bytes = output.getvalue()

    # Escribe los bytes en un archivo
    with open(nombre_archivo_salida, "wb") as file:
        file.write(xml_bytes)

    print(f"Archivo XML generado: {nombre_archivo_salida}")


if __name__ == '__main__':
    main()