from email.message import EmailMessage
import smtplib
from xml.dom import minidom
import socket
import threading
import os

# Configuración del servidor
host = 'localhost'
port = 12345
buffer_size = 1024

# Función para recibir los datos del email / archivos.
def recibirDatos(client_socket):
    destinatario = client_socket.recv(buffer_size).decode("utf-8")
    asunto = client_socket.recv(buffer_size).decode("utf-8")
    mensaje = client_socket.recv(buffer_size).decode("utf-8")    
    archivo1 = client_socket.recv(buffer_size).decode("utf-8")
    archivo2 = client_socket.recv(buffer_size).decode("utf-8")
    archivo3 = client_socket.recv(buffer_size).decode("utf-8")    
    client_socket.close()
    return destinatario, asunto, mensaje, archivo1, archivo2, archivo3


def enviarCorreos(archivo):
    print(f'Enviando correos desde el archivo: {archivo}')
    
    if os.path.exists(archivo):
        doc = minidom.parse(archivo)

        # Obtenemos la raíz del documento.
        root = doc.documentElement

        # Obtener un array de los elementos 'empleado' del archivo.
        personas = root.getElementsByTagName("personne")

        # Iterar sobre los elementos "personne"
        for persona in personas:
            # Obtener los valores de cada etiqueta
            firstname = persona.getElementsByTagName("firstname")[0].childNodes[0].data
            lastname = persona.getElementsByTagName("lastname")[0].childNodes[0].data
            phone = persona.getElementsByTagName("phone")[0].childNodes[0].data
            email = persona.getElementsByTagName("email")[0].childNodes[0].data

            # Imprimir los valores obtenidos
            print("Nombre:", firstname)
            print("Apellido:", lastname)
            print("Teléfono:", phone)
            print("Email:", email)
            print("---")
    else:
        print(f'No se ha encontrado el archivo: {archivo}')


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
        destinatario, asunto, mensaje, archivo1, archivo2, archivo3 = recibirDatos(client_socket)

        # Imprimimos los datos recibidos.
        print(f"Destinatario: {destinatario}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print(f"Archivo 1: {archivo1}")
        print(f"Archivo 2: {archivo2}")
        print(f"Archivo 3: {archivo3}")

        # Creamos los hilos para mandar los correos.
        hilo1 = threading.Thread(target=enviarCorreos, args=(archivo1,))
        # hilo2 = threading.Thread(target=enviarCorreos, args=(archivo2,))
        # hilo3 = threading.Thread(target=enviarCorreos, args=(archivo3,))

        hilo1.start()
        # hilo2.start()
        # hilo3.start()

os.system('cls')
# Iniciar el servidor
start_server()