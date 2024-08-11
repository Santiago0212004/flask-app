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

6. En caso de que aparezcan errores de las librerías, cambiar el python interpreter por el del entorno virtual:

   ![image](https://github.com/user-attachments/assets/2dd8b83a-b985-4378-b76c-30668874d395)

   ![image](https://github.com/user-attachments/assets/946c3d12-c345-4df9-9dcd-fa11f3309f4d)

   
7. Instalar las dependencias:
  ```pip install -r requirements. txt```

8. Ejecutar el archivo de inicialización:
   ```python init.py```

9. Ejecutar la aplicación:
   ```python app.py``` 
