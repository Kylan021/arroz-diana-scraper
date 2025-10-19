import os
import signal
import time

pids_file = os.path.join(os.path.dirname(__file__), "pids.txt")

def stop_servers():
    if not os.path.exists(pids_file):
        print("No se encontró el archivo pids.txt. Asegúrate de que los servidores estén corriendo.")
        return

    with open(pids_file, "r") as f:
        pids = f.readlines()

    for pid_str in pids:
        try:
            pid = int(pid_str.strip())
            os.kill(pid, signal.SIGTERM)  # Terminar el proceso
            print(f"Proceso con PID {pid} terminado.")
        except ProcessLookupError:
            print(f"El proceso con PID {pid} no se encontró o ya estaba terminado.")
        except Exception as e:
            print(f"Error al intentar terminar el proceso con PID {pid}: {e}")

    # Esperar un momento para que los procesos terminen
    time.sleep(2)

    # Eliminar el archivo pids.txt
    if os.path.exists(pids_file):
        os.remove(pids_file)
        print("Archivo pids.txt eliminado.")

if __name__ == "__main__":
    stop_servers()