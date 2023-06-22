import socket

def main():
    host = 'localhost'
    puerto = 12345

    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((host, puerto))
        servidor.listen(1)
        print('Servidor en espera de conexiones...')

        conexion, direccion = servidor.accept()
        print('Cliente conectado:', direccion)

        while True:
            nombre_archivo = conexion.recv(1024).decode()
            if not nombre_archivo:
                break

            tamano_archivo = conexion.recv(4)  # Recibe el tamaño del archivo en 4 bytes
            tamano_archivo = int.from_bytes(tamano_archivo, byteorder='big')  # Convierte los bytes a un entero

            contenido_archivo = b''
            bytes_recibidos = 0
            while bytes_recibidos < tamano_archivo:
                datos = conexion.recv(min(tamano_archivo - bytes_recibidos, 1024))
                contenido_archivo += datos
                bytes_recibidos += len(datos)

            # Imprime el nombre y contenido del archivo XML
            print(f"Archivo recibido: {nombre_archivo}")
            print("Contenido:")
            print(contenido_archivo.decode())

        conexion.close()
        servidor.close()
    except socket.error as e:
        print("Error al iniciar el servidor:", str(e))

if __name__ == '__main__':
    main()