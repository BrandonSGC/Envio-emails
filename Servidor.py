import socket
import os

# Configuración del servidor
host = 'localhost'
port = 12345
buffer_size = 1024

def receive_data(client_socket):
    # Recibir datos del correo
    destinatario = client_socket.recv(buffer_size).decode()
    asunto = client_socket.recv(buffer_size).decode()
    mensaje = client_socket.recv(buffer_size).decode()

    # Imprimir los datos del correo
    print("Datos del correo:")
    print(f"Destinatario: {destinatario}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}\n")

    # Recibir cantidad de archivos
    files_count = int.from_bytes(client_socket.recv(4), byteorder='big')
    print(f"Cantidad de archivos: {files_count}")

    # Recibir archivos
    for i in range(files_count):
        # Recibir nombre del archivo
        file_name_length = int.from_bytes(client_socket.recv(4), byteorder='big')
        file_name = client_socket.recv(file_name_length).decode()
        print(f"Nombre del archivo {i + 1}: {file_name}")

        # Recibir contenido del archivo
        with open(file_name, 'w') as file:
            while True:
                data = client_socket.recv(buffer_size)
                if not data:
                    break
                file.write(data)

        print(f"Archivo {file_name} recibido y guardado.")

    # Cerrar la conexión con el cliente
    client_socket.close()



def start_server():
    # Crear un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket al host y puerto
    server_socket.bind((host, port))

    # Escuchar conexiones entrantes
    server_socket.listen(1)
    print("Servidor en espera de conexiones...")

    while True:
        # Esperar una nueva conexión
        client_socket, address = server_socket.accept()
        print(f"- Conexión establecida desde: {address}\n")

        # Manejar la conexión en un hilo separado
        receive_data(client_socket)


os.system('cls')
# Iniciar el servidor
start_server()
