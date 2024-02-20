
# Reto: Beats

Introducción a Filebeat y Análisis de Logs

## Descripción:

• Montar en un Docker Compose Elastic search y Filebeat

• Crear un fichero JSON desde Python con datos dummy compatible con FileBeat

• Añadir el código de creación al Docker Compose e ingerir los datos a Elastic desde FileBeat

• Subir datos a dos índices diferentes de FileBeat*

• Comprobar los datos en los índices de Elastic utilizando Postman

## Estructura 🏗️

![image](https://github.com/jdecruzdeusto/Elastic-Beats/assets/125390240/81c7c59a-ca03-442a-82c6-d9cdb76fc1dc)

## Ejecución 🚀

1. Ejecutar el archivo app.py para generar JSONs cada 5 segundos:
```bash
python3 app.py
```

2. Abrir otra terminal bash y ejecutar el comando de docker:
```bash
sudo docker compose up -d
```

3. Comprobar el estado de los containers:
```bash
sudo docker compose up -d
```
### Postman 🧑‍🚀
4. Sacamos el index y vemos la cantidad de JSONs mediante una llamada GET a esta URL:
```
http://localhost:9200/_cat/indices?v
```

5. Hacemos una llamada GET a la URL con el index del anterior paso añadiendo "/_search" al final:
```
http://localhost:9200/INDEX A RELLENAR/_search
```
