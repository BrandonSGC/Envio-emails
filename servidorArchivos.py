import socket
import struct

def main():
    host = 'localhost'
    puerto = 12345

    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((host, puerto))
        servidor.listen(1)
        print('Servidor en espera de conexiones...')

        while True:
            conexion, direccion = servidor.accept()
            print('Cliente conectado:', direccion)

            while True:
                # Recibe el nombre del archivo
                nombre_archivo = conexion.recv(1024).decode()
                if not nombre_archivo:
                    break

                # Recibe la longitud del archivo en 4 bytes
                longitud_archivo = conexion.recv(4)
                longitud_archivo = struct.unpack('!I', longitud_archivo)[0]

                # Recibe el contenido del archivo
                contenido_archivo = conexion.recv(longitud_archivo).decode()

                # Imprime el nombre y contenido del archivo XML
                print(f"Archivo recibido: {nombre_archivo}")
                print("Contenido:")
                print(contenido_archivo)

            conexion.close()
            print('Cliente desconectado:', direccion)

    except socket.error as e:
        print("Error al iniciar el servidor:", str(e))

    finally:
        servidor.close()

if __name__ == '__main__':
    main()
