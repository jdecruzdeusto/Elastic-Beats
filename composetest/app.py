import json
import time
from datetime import datetime

# Función para generar datos dummy
def generate_data():
    timestamp = datetime.utcnow()
    messages = [
        "Error en la aplicacion XYZ",
        "Advertencia de memoria baja",
        "Aviso de parada de emergencia"
    ]
    levels = ["error", "warn", "info"]
    
    # Crear un log dummy seleccionando un mensaje y nivel aleatorio
    log_entry = {
        "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "message": messages[timestamp.second % len(messages)],
        "level": levels[timestamp.second % len(levels)]
    }
    return log_entry

# Ruta al archivo JSON donde se guardarán los logs
file_path = '/home/juan/composetest/logs/dummy_logs.json'

# Bucle infinito para generar datos cada 5 segundos (debe ser manejado en tu entorno local)
while True:
    data = generate_data()
    # Añadir datos al archivo JSON
    with open(file_path, 'a') as file:
        file.write(json.dumps(data) + "\n")
    time.sleep(5)  # Esperar 5 segundos antes de generar el próximo dato
