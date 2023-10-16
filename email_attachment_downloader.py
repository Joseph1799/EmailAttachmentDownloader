from simplegmail import Gmail
from simplegmail.query import construct_query
import os

# Inicia una conexión a Gmail.
gmail = Gmail()

# Configuración de la consulta para obtener correos electrónicos etiquetados como "Tu_Etiqueta_Aquí".
query_params = {
    "label": "Tu_Etiqueta_Aquí",  # Modifica "Tu_Etiqueta_Aquí" por la etiqueta deseada.
}

# Obtiene los mensajes que coinciden con la consulta.
messages = gmail.get_messages(query=construct_query(query_params))

# Ordena los mensajes por fecha de manera descendente (los más recientes primero).
messages.sort(key=lambda message: message.date, reverse=True)

# Si se encuentran mensajes:
if messages:
    # Obtiene el mensaje más reciente de la lista.
    latest_message = messages[0]
    print("To: " + latest_message.recipient)
    print("From: " + latest_message.sender)
    print("Subject: " + latest_message.subject)
    print("Date: " + latest_message.date)
    print("Preview: " + latest_message.snippet)

    # Verifica si el correo electrónico contiene un archivo PDF adjunto.
    for attachment in latest_message.attachments:
        if attachment.filename.lower().endswith('.pdf'):
            # Guarda el archivo PDF adjunto en la ubicación deseada.
            attachment.save('C:\\Users\\user\\dir\\dir\\dir\\' + attachment.filename, overwrite=True)
else:
    print("No se encontraron correos electrónicos en la etiqueta 'Tu_Etiqueta_Aquí'.")
