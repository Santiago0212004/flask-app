# Flask-App
Pasos para configurar el proyecto:

1. Crear un archvio llamado "database.db".
   
2. Crear un archivo llamada ".env", en este poner:

  ```
  SECRET_KEY=tu_clave_secreta_aqui
  DATABASE_URL=sqlite:///database.db
  ```

3. Abrir una terminal 
   
4. Crear un entorno virtual:
  ```python -m venv venv```

5. Activar el entorno virtual:
   ```venv/bin/activate```

6. En caso de que aparezcan errores de las librerías, escribir ```ctrl+P```, luego escribir ```>``` y cambiar el python interpreter por el del entorno virtual:

   ![image](https://github.com/user-attachments/assets/2dd8b83a-b985-4378-b76c-30668874d395)

   Presionar enter y luego seleccionar la que diga "venv":

   ![image](https://github.com/user-attachments/assets/946c3d12-c345-4df9-9dcd-fa11f3309f4d)

   
8. Instalar las dependencias:
  ```pip install -r requirements.txt```

9. Ejecutar el archivo de inicialización:
   ```python init.py```

10. Ejecutar la aplicación:
   ```python app.py``` 

11. Para detener la ejecución presionar ```ctrl+C```, y para salir del entorno virtual escribir ```deactivate```
