package com.mycompany.cliente.java;
import java.io.BufferedInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;

public class pruebaArchivos {
    public static void main(String[] args) {
        // Variables de mientras...
        String host = "localhost";
        int puerto = 12345;        
        String archivo = "C:\\\\Users\\\\brans\\\\OneDrive\\\\Escritorio\\\\Personas.xml";
        String archivo2 = "C:\\\\Users\\\\brans\\\\OneDrive\\\\Escritorio\\\\Personas2.xml";
        String archivo3 = "C:\\\\Users\\\\brans\\\\OneDrive\\\\Escritorio\\\\Personas3.xml";
                
        enviarArchivoXML(host, puerto, archivo);               
        enviarArchivoXML(host, puerto, archivo2);
        enviarArchivoXML(host, puerto, archivo3);
    }
    
    public static void enviarArchivoXML(String host, int puerto, String archivo) {
        try {
            Socket socket = new Socket(host, puerto);
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

            File file = new File(archivo);
            FileInputStream fis = new FileInputStream(file);
            BufferedInputStream bis = new BufferedInputStream(fis);

            byte[] buffer = new byte[(int) file.length()];
            bis.read(buffer, 0, buffer.length);

            // Envía el nombre del archivo
            dos.writeUTF(file.getName());
            // Envía el tamaño del archivo
            dos.writeInt(buffer.length);
            
            // Envía el contenido del archivo
            dos.write(buffer, 0, buffer.length);
            dos.writeUTF("FIN_ARCHIVO");

            bis.close();
            fis.close();

            dos.close();
            socket.close();
            System.out.println("Archivos enviados correctamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}