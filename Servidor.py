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

# Variables de estadisticas.
estadisticas = []
totalEnviar = 0
conProblemas = 0

# Función para recibir los datos del email / archivos.
def recibirDatos(client_socket):
    asunto = client_socket.recv(buffer_size).decode("utf-8")
    mensaje = client_socket.recv(buffer_size).decode("utf-8")    
    archivo1 = client_socket.recv(buffer_size).decode("utf-8")
    archivo2 = client_socket.recv(buffer_size).decode("utf-8")
    archivo3 = client_socket.recv(buffer_size).decode("utf-8")    
    client_socket.close()
    return asunto, mensaje, archivo1, archivo2, archivo3

# Funcion para generar las estadisticas de los archivos.
def generarXML(estadisticas_archivo):
    # Crear el documento XML
    doc = minidom.Document()

    # Crear la etiqueta raíz
    root = doc.createElement("root")
    doc.appendChild(root)

    for estadistica_archivo in estadisticas_archivo:
        # Crear el elemento 'estadisticas'
        estadisticas_elem = doc.createElement("estadisticas")
        root.appendChild(estadisticas_elem)

        archivo = doc.createElement('archivo')
        estadisticas_elem.appendChild(archivo)
        archivoTexto = doc.createTextNode(estadistica_archivo['archivo'])
        archivo.appendChild(archivoTexto)

        totalenvios = doc.createElement('totalenvios')
        estadisticas_elem.appendChild(totalenvios)
        totalenviosTexto = doc.createTextNode(str(estadistica_archivo['totalenvios']))
        totalenvios.appendChild(totalenviosTexto)

        fallidos = doc.createElement('fallidos')
        estadisticas_elem.appendChild(fallidos)
        fallidosTexto = doc.createTextNode(str(estadistica_archivo['fallidos']))
        fallidos.appendChild(fallidosTexto)

    # Guardar el documento XML en un archivo
    xml_file = open("Estadisticas.xml", "w")
    xml_file.write(doc.toprettyxml(indent="\t"))
    xml_file.close()
    print('Se ha generado un archivo con las estadisticas!')


# Funcion que envia los correos a cada persona en el archivo.
def enviarCorreos(archivo, remitente, asunto, mensaje):      
    # Variables para almacenar las estadísticas del archivo actual
    estadisticas_archivo = {
        'archivo': archivo.split('\\')[-1],  # Obtener el nombre del archivo
        'totalenvios': 0,
        'fallidos': 0
    }

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
            destinatario = persona.getElementsByTagName("email")[0].childNodes[0].data

            try:
                email = EmailMessage()
                email["From"] = remitente
                email["To"] = destinatario
                email["Subject"] = asunto
                email.set_content(mensaje)

                smtp = smtplib.SMTP_SSL("smtp.gmail.com")
                
                # Adjunatmos el correo del remitente y la clave.
                smtp.login(remitente, "fiqosavbtvqwdcay")
                smtp.sendmail(remitente, destinatario, email.as_string())
                
                # Incrementar el contador de envíos exitosos
                estadisticas_archivo['totalenvios'] += 1                
                smtp.quit()
                print(f"El correo electronico a {destinatario} de {firstname} {lastname} ha sido enviado con éxito!")
                print("-"*70)
            except:
                # Incrementar el contador de envíos exitosos
                estadisticas_archivo['fallidos'] += 1                
                print(f"Ha ocurrido un error al enviar el correo electrónico a {destinatario}")
                print("-" * 70)
                        
        # Agregar las estadísticas del archivo actual a la lista de estadísticas
        estadisticas.append(estadisticas_archivo)        
    else:
        print(f'No se ha encontrado el archivo: {archivo}')


# Funcion para inicializar el servidor.
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
        asunto, mensaje, archivo1, archivo2, archivo3 = recibirDatos(client_socket)

        # Imprimimos los datos recibidos.
        remitente = "bransti20@gmail.com"
        print(f"Remitente: {remitente}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print(f"Archivo 1: {archivo1}")
        print(f"Archivo 2: {archivo2}")
        print(f"Archivo 3: {archivo3}")

        input('\nEnter para continuar...\n')

        # Validar de ejecutar el programa solamente si se mandaron minimo 2 o max 3 archivos.
        if archivo3 == "":
            # Creamos los hilos para mandar los correos concurrentemente.
            hilo1 = threading.Thread(target=enviarCorreos, args=(archivo1, remitente, asunto, mensaje))
            hilo2 = threading.Thread(target=enviarCorreos, args=(archivo2, remitente, asunto, mensaje))

            # Inicializamos los hilos.
            hilo1.start()
            hilo2.start()

            # Esperamos a que los hilos terminen antes del break.
            hilo1.join()
            hilo2.join()
        else:
            # Creamos los hilos para mandar los correos concurrentemente.
            hilo1 = threading.Thread(target=enviarCorreos, args=(archivo1, remitente, asunto, mensaje))
            hilo2 = threading.Thread(target=enviarCorreos, args=(archivo2, remitente, asunto, mensaje))
            hilo3 = threading.Thread(target=enviarCorreos, args=(archivo3, remitente, asunto, mensaje))

            # Inicializamos los hilos.
            hilo1.start()
            hilo2.start()
            hilo3.start()

            # Esperamos a que los hilos terminen antes del break.
            hilo1.join()
            hilo2.join()
            hilo3.join()
        
        break

    # Generar el archivo XML con las estadísticas
    generarXML(estadisticas)

os.system('cls')

start_server()