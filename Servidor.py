import socket
import os

# Configuración del servidor
host = 'localhost'
port = 12345
buffer_size = 1024

# Función para recibir los datos del email / archivos.
def recibirDatosEmail(client_socket):
    destinatario = client_socket.recv(buffer_size).decode("utf-8")
    asunto = client_socket.recv(buffer_size).decode("utf-8")
    mensaje = client_socket.recv(buffer_size).decode("utf-8")
    
    archivo1 = client_socket.recv(buffer_size).decode("utf-8")
    archivo2 = client_socket.recv(buffer_size).decode("utf-8")
    archivo3 = client_socket.recv(buffer_size).decode("utf-8")
    
    client_socket.close()
    return destinatario, asunto, mensaje, archivo1, archivo2, archivo3

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

        # Obtener los datos del email.
        destinatario, asunto, mensaje, archivo1, archivo2, archivo3 = recibirDatosEmail(client_socket)
        print(f"Destinatario: {destinatario}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print(f"Archivo 1: {archivo1}")
        print(f"Archivo 2: {archivo2}")
        print(f"Archivo 3: {archivo3}")

os.system('cls')
# Iniciar el servidor
start_server()
