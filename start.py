import subprocess
import time
import webbrowser
import os

# Rutas a los directorios del backend y frontend
backend_dir = os.path.join(os.path.dirname(__file__), "backend")
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")

# Comandos para iniciar el backend y el frontend
backend_command = ["python", "app.py"]
frontend_command = ["npm", "start"]

# Iniciar el backend
print("Iniciando el backend de Flask...")
backend_process = subprocess.Popen(backend_command, cwd=backend_dir)

# Iniciar el frontend
print("Iniciando el frontend de React...")
# En Windows, para establecer variables de entorno para npm, se usa set en el mismo comando
# o se usa $env:PORT=3001; npm start en PowerShell. Aquí usaremos una forma compatible.
# Para simplificar, asumiremos que npm start preguntará por el puerto si el 3000 está ocupado
# o que el usuario ya ha configurado el puerto por defecto.
# Si se necesita un puerto específico, se puede modificar el comando.
frontend_process = subprocess.Popen(["cmd.exe", "/c", "set PORT=3001 && npm start"], cwd=frontend_dir, shell=True)

# Esperar un tiempo para que los servidores se inicien
print("Esperando a que los servidores se inicien...")
time.sleep(15) # Ajusta este tiempo si los servidores tardan más en iniciar

# Abrir el navegador con la URL del frontend
frontend_url = "http://localhost:3001"
print(f"Abriendo el navegador en {frontend_url}...")
webbrowser.open(frontend_url)

print("Los servidores están corriendo. Presiona Ctrl+C para detenerlos.")

# Mantener los procesos vivos hasta que el script principal sea terminado
try:
    backend_process.wait()
    frontend_process.wait()
except KeyboardInterrupt:
    print("Deteniendo los servidores...")
    backend_process.terminate()
    frontend_process.terminate()
    print("Servidores detenidos.")