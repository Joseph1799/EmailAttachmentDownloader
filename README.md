## Uso del Script para Descargar Archivos Adjuntos de Correos Electrónicos en Gmail

Este script te permitirá conectarte a tu cuenta de Gmail y descargar archivos adjuntos de los correos electrónicos que estén etiquetados con una etiqueta específica. A continuación, se detalla paso a paso cómo utilizar el script. Es importante tener en cuenta que debes cumplir con varios requisitos previos antes de proceder.

### Requisitos Previos

#### 1. Gmail API

Para utilizar este script, necesitas configurar la Gmail API y obtener las credenciales correspondientes (token y secret_key). Aquí hay un resumen de los pasos a seguir:

- Accede a la [Consola de Desarrolladores de Google](https://console.developers.google.com/).
- Crea un nuevo proyecto o selecciona un proyecto existente.
- En el panel de control del proyecto, ve a "API y servicios" y haz clic en "Biblioteca".
- Busca "Gmail API" y actívala para tu proyecto.
- En "Credenciales", crea una nueva credencial de tipo "ID de cliente OAuth".
- Configura la aplicación cliente OAuth para una aplicación de escritorio.
- Descarga el archivo JSON de las credenciales. Asegúrate de que este archivo esté en el mismo directorio que tu script y que lo renombres como `client_secret.json`.

#### 2. Python

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde el [sitio web oficial de Python](https://www.python.org/downloads/).

#### 3. Instalación de Bibliotecas

Instala la biblioteca `simplegmail` utilizando `pip`. Abre una terminal o línea de comandos y ejecuta el siguiente comando:

```sh
pip install simplegmail
```

### Configuración

1. Abre el script en tu editor de código preferido.

2. En el script, localiza la siguiente línea:

   ```python
   "label": "Tu_Etiqueta_Aquí",  # Modifica "Tu_Etiqueta_Aquí" por la etiqueta deseada.
   ```

   Reemplaza `"Tu_Etiqueta_Aquí"` con la etiqueta real que deseas utilizar para filtrar los correos electrónicos que contienen archivos adjuntos.

### Ejecución del Script

1. Abre una terminal o línea de comandos y navega al directorio donde se encuentra el script.

2. Ejecuta el script mediante el siguiente comando:

```sh
email_attachment_downloader.py
```

   Asegúrate de que `email_attachment_downloader.py` sea el nombre real de tu archivo de script.

3. El script se conectará a tu cuenta de Gmail y buscará correos electrónicos etiquetados con la etiqueta que especificaste.

4. Si se encuentran correos electrónicos que coinciden con la etiqueta:

   - El script imprimirá información sobre el correo electrónico más reciente, incluyendo el destinatario, el remitente, el asunto, la fecha y una vista previa del contenido.

   - Luego, verificará si el correo electrónico contiene archivos PDF adjuntos. Si es así, los guardará en la ubicación especificada en la línea:

     ```python
     attachment.save('C:\\Users\\user\\dir\\dir\\dir\\' + attachment.filename, overwrite=True)
     ```

     Asegúrate de reemplazar `C:\\Users\\user\\dir\\dir\\dir\\` con la ubicación de tu preferencia.

5. Si no se encuentran correos electrónicos que coincidan con la etiqueta, el script imprimirá el mensaje: "No se encontraron correos electrónicos en la etiqueta 'Tu_Etiqueta_Aquí'."

### Notas Adicionales

- Mantén tus credenciales de Gmail API (token y secret_key) seguras y no las compartas con nadie más.

- Puedes automatizar la ejecución de este script utilizando programación de tareas o un gestor de tareas, como `cron` en sistemas Unix.

- Este script se proporciona tal cual y es responsabilidad del usuario adaptarlo y utilizarlo de acuerdo a sus necesidades y requerimientos.
