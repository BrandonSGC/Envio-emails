package GUI;

// Bibliotecas
import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import java.nio.charset.StandardCharsets;


public class InterfacePrincipal extends javax.swing.JFrame {

    /* Creates new form InterfacePrincipal */
    public InterfacePrincipal() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        pnlDatosEmail = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        txtAsunto = new javax.swing.JTextField();
        lblAsunto = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        txtMensaje = new javax.swing.JTextArea();
        lblTitulo = new javax.swing.JLabel();
        btnEnviarEmails = new javax.swing.JButton();
        jLabel2 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        lblArchivo1 = new javax.swing.JLabel();
        lblArchivo2 = new javax.swing.JLabel();
        lblArchivo3 = new javax.swing.JLabel();
        btnCargarArchivo1 = new javax.swing.JButton();
        btnCargarArchivo2 = new javax.swing.JButton();
        btnCargarArchivo3 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        jLabel1.setText("Asunto:");

        txtAsunto.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N

        lblAsunto.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        lblAsunto.setText("Mensaje:");

        txtMensaje.setColumns(20);
        txtMensaje.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        txtMensaje.setRows(5);
        jScrollPane1.setViewportView(txtMensaje);

        lblTitulo.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        lblTitulo.setText("Email");

        btnEnviarEmails.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        btnEnviarEmails.setText("Enviar Emails");
        btnEnviarEmails.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEnviarEmailsActionPerformed(evt);
            }
        });

        jLabel2.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        jLabel2.setText("Por favor seleccione los archivos");

        jLabel4.setText("Archivo #1:");

        jLabel5.setText("Archivo #2:");

        jLabel6.setText("Archivo #3:");

        lblArchivo1.setText("...");

        lblArchivo2.setText("...");

        lblArchivo3.setText("...");

        btnCargarArchivo1.setText("Cargar archivo");
        btnCargarArchivo1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCargarArchivo1ActionPerformed(evt);
            }
        });

        btnCargarArchivo2.setText("Cargar Archivo");
        btnCargarArchivo2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCargarArchivo2ActionPerformed(evt);
            }
        });

        btnCargarArchivo3.setText("Cargar Archivo");
        btnCargarArchivo3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCargarArchivo3ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout pnlDatosEmailLayout = new javax.swing.GroupLayout(pnlDatosEmail);
        pnlDatosEmail.setLayout(pnlDatosEmailLayout);
        pnlDatosEmailLayout.setHorizontalGroup(
            pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlDatosEmailLayout.createSequentialGroup()
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(pnlDatosEmailLayout.createSequentialGroup()
                        .addGap(149, 149, 149)
                        .addComponent(lblTitulo))
                    .addGroup(pnlDatosEmailLayout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jLabel1)
                            .addComponent(lblAsunto)
                            .addComponent(jScrollPane1)
                            .addComponent(txtAsunto, javax.swing.GroupLayout.PREFERRED_SIZE, 350, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(pnlDatosEmailLayout.createSequentialGroup()
                        .addGap(75, 75, 75)
                        .addComponent(jLabel2))
                    .addGroup(pnlDatosEmailLayout.createSequentialGroup()
                        .addGap(95, 95, 95)
                        .addComponent(btnEnviarEmails, javax.swing.GroupLayout.PREFERRED_SIZE, 161, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(8, Short.MAX_VALUE))
            .addGroup(pnlDatosEmailLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(jLabel5)
                    .addComponent(jLabel4)
                    .addComponent(jLabel6))
                .addGap(18, 18, 18)
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(lblArchivo1)
                    .addComponent(lblArchivo2)
                    .addComponent(lblArchivo3))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btnCargarArchivo2)
                    .addComponent(btnCargarArchivo1)
                    .addComponent(btnCargarArchivo3))
                .addGap(20, 20, 20))
        );
        pnlDatosEmailLayout.setVerticalGroup(
            pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, pnlDatosEmailLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(lblTitulo)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(txtAsunto, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(lblAsunto)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel2)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(btnCargarArchivo1)
                    .addComponent(lblArchivo1))
                .addGap(18, 18, 18)
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(btnCargarArchivo2)
                    .addComponent(lblArchivo2))
                .addGap(18, 18, 18)
                .addGroup(pnlDatosEmailLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(btnCargarArchivo3)
                    .addComponent(lblArchivo3))
                .addGap(18, 18, 18)
                .addComponent(btnEnviarEmails, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnlDatosEmail, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnlDatosEmail, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    String archivo1 = "";
    String archivo2 = "";
    String archivo3 = "";
    
    private void btnEnviarEmailsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEnviarEmailsActionPerformed
        if (validarFormulario() && validarArchivos()) {
            sendDataToServer();
        } else {
            JOptionPane.showMessageDialog(null, "Debe ingresar los datos del formulario y minimo 2 archivos o maximo 3.");
        }
    }//GEN-LAST:event_btnEnviarEmailsActionPerformed

    private void btnCargarArchivo1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCargarArchivo1ActionPerformed
        JFileChooser fc = new JFileChooser();
        
        int result = fc.showOpenDialog(null);
        
        if (result == JFileChooser.APPROVE_OPTION) {
            File file = fc.getSelectedFile();
            archivo1 = file.getAbsolutePath();
            lblArchivo1.setText(file.getName());
        }
        
    }//GEN-LAST:event_btnCargarArchivo1ActionPerformed

    private void btnCargarArchivo2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCargarArchivo2ActionPerformed
        JFileChooser fc = new JFileChooser();
        
        int result = fc.showOpenDialog(null);
        
        if (result == JFileChooser.APPROVE_OPTION) {
            File file = fc.getSelectedFile();
            archivo2 = file.getAbsolutePath();
            lblArchivo2.setText(file.getName());
        }
    }//GEN-LAST:event_btnCargarArchivo2ActionPerformed

    private void btnCargarArchivo3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCargarArchivo3ActionPerformed
        JFileChooser fc = new JFileChooser();
        
        int result = fc.showOpenDialog(null);
        
        if (result == JFileChooser.APPROVE_OPTION) {
            File file = fc.getSelectedFile();
            archivo3 = file.getAbsolutePath();            
            lblArchivo3.setText(file.getName());
        }
    }//GEN-LAST:event_btnCargarArchivo3ActionPerformed
    
    // Función que envía los datos del email y los archivos XML.
    private void sendDataToServer() {
        // Obtener datos del email
        String asunto = txtAsunto.getText();
        String mensaje = txtMensaje.getText();

        // Asignar el host y puerto
        String host = "localhost";
        int port = 12345;

        try {
            // Crear una conexión con el servidor
            Socket socket = new Socket(host, port);

            // Obtener el flujo de salida del socket
            OutputStream outputStream = socket.getOutputStream();
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(outputStream, StandardCharsets.UTF_8));

            
            writer.write(asunto);
            writer.flush();
            
            writer.write(mensaje);
            writer.flush();            

            // Enviar los path de los archivos.
            writer.write(archivo1);
            writer.flush();            
            
            writer.write(archivo2);
            writer.flush();
            
            writer.write(archivo3);
            writer.flush(); // Flush para asegurar que los datos se envíen

            // Cerrar la conexión
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    
    private boolean validarFormulario() {
        // Validamos el formulario
        if (txtAsunto.getText().equals("") || txtMensaje.getText().equals("")) {
            return false;
        } 
        return true;
    }
    
    private boolean validarArchivos() {
        // Validamos el formulario
        if (lblArchivo1.getText() != "..." && lblArchivo2.getText() != "...") {
            return true;
        } 
        return false;
    }
        

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnCargarArchivo1;
    private javax.swing.JButton btnCargarArchivo2;
    private javax.swing.JButton btnCargarArchivo3;
    private javax.swing.JButton btnEnviarEmails;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel lblArchivo1;
    private javax.swing.JLabel lblArchivo2;
    private javax.swing.JLabel lblArchivo3;
    private javax.swing.JLabel lblAsunto;
    private javax.swing.JLabel lblTitulo;
    private javax.swing.JPanel pnlDatosEmail;
    private javax.swing.JTextField txtAsunto;
    private javax.swing.JTextArea txtMensaje;
    // End of variables declaration//GEN-END:variables
}
