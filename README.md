# Email Attachment Downloader

Este script de Python te permite automatizar la descarga de archivos adjuntos de correos electrónicos que cumplan con ciertos criterios. En este ejemplo, se asume que estás trabajando con Gmail, pero puedes adaptarlo a otros proveedores de correo electrónico.

## Requisitos

- Python 3.x
- [SimpleGmail](https://github.com/abhishekraiyani/SimpleGmail) (una biblioteca para acceder a correos electrónicos de Gmail)
- Cuenta de Gmail y la configuración del servicio Gmail API.

## Configuración

1. Instala la biblioteca SimpleGmail usando pip:


2. Configuración del servicio Gmail API:
- Antes de usar este script, es necesario habilitar la API de Gmail y configurar credenciales de acceso. Puedes seguir los pasos detallados en la [Guía de Configuración del Servicio Gmail API](https://developers.google.com/gmail/api/quickstart) para obtener el archivo `credentials.json`.
- Asegúrate de guardar el archivo `credentials.json` en el mismo directorio donde se encuentra el script `email_attachment_downloader.py`.

## Uso

1. Clona o descarga este repositorio.

2. Abre el archivo `email_attachment_downloader.py` en tu editor de código favorito.

3. Personaliza el script:
- Modifica `query_params` para definir tus criterios de búsqueda de correos electrónicos. Por ejemplo, puedes cambiar la etiqueta o cualquier otro parámetro que desees.
- Ajusta la ruta en la línea que guarda los archivos adjuntos para que se almacenen en el directorio deseado en tu sistema.

4. Ejecuta el script:


El script buscará correos electrónicos que coincidan con tus criterios y descargará los archivos adjuntos (en este ejemplo, archivos PDF) en la ubicación especificada.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este script o agregar nuevas funcionalidades, no dudes en hacer una solicitud de extracción.

## Agradecimientos

- Este script utiliza la biblioteca [SimpleGmail](https://github.com/abhishekraiyani/SimpleGmail) para acceder a correos electrónicos de Gmail. Gracias a su autor y a la comunidad de código abierto.

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE).
