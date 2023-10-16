from simplegmail import Gmail
from simplegmail.query import construct_query
import os

print("Current working directory:", os.getcwd())

gmail = Gmail()

# Consulta para obtener correos actuales etiquetados como "PIMA".
query_params = {
    "label": "Tu_Etiquieta_Aquí",
}

messages = gmail.get_messages(query=construct_query(query_params))

# Ordenar los mensajes por fecha de manera descendente (los más recientes primero).
messages.sort(key=lambda message: message.date, reverse=True)

if messages:
    latest_message = messages[0]  # El primer mensaje en la lista es el más reciente.
    print("To: " + latest_message.recipient)
    print("From: " + latest_message.sender)
    print("Subject: " + latest_message.subject)
    print("Date: " + latest_message.date)
    print("Preview: " + latest_message.snippet)

    # Verificar si el correo electrónico contiene un archivo PDF adjunto.
    for attachment in latest_message.attachments:
        if attachment.filename.lower().endswith('.pdf'):
            # Guardar el archivo PDF adjunto en la ubicación deseada.
            attachment.save('C:\\Users\\user\\dir\\dir\\dir\\' + attachment.filename, overwrite=True)


else:
    print("No se encontraron correos electrónicos en la etiqueta 'Tu_Etiquieta_Aquí'.")
