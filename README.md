
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

## Cómo he realizado el reto 🧠
#### app.py
1. Crear el archivo .py definiendo una función para crear un archivo JSON eligiendo de manera aleatoria entre 3 opciones definidas
2. Definir la ruta en la que crear los JSON
3. Crear un bucle llamando a la función "generate_data" cada 5 segundos

#### docker-compose.yml
1. Definir la versión de Docker Compose:

• Especificar la versión de Docker Compose utilizada en el archivo, en este caso, la 3.7.

2. Servicio Elasticsearch:

• Utilizar la imagen elasticsearch:7.9.3 desde el repositorio oficial de Elastic.

• Nombrar el contenedor como elasticsearch.

• Establecer variables de entorno para configurar Elasticsearch como un nodo único y desactivar las características de seguridad de X-Pack.

• Mapear el puerto 9200 del host al puerto 9200 del contenedor para que Elasticsearch sea accesible desde el host.

3. Servicio Filebeat:

• Utilizar la imagen filebeat:7.9.3 desde el repositorio oficial de Elastic.

• Nombrar el contenedor como filebeat.

• Establecer una dependencia hacia el servicio elasticsearch, asegurando que Filebeat se inicie después de que Elasticsearch esté corriendo.

• Montar volúmenes para la configuración de Filebeat (filebeat.yml) y el directorio donde se almacenan los logs que Filebeat debe monitorear.

• Definir la variable de entorno ELASTIC_HOSTS para señalar la dirección del servicio Elasticsearch.

#### filebeat.yml
1. filebeat.inputs: 

• Define que Filebeat monitoreará los archivos de log con extensión .json en el directorio especificado. Además, establece un campo personalizado llamado index con el valor "dummy".

2. output.elasticsearch:

• Configura Filebeat para enviar los datos recopilados a Elasticsearch, especificando el host y el índice donde se deben almacenar los datos, usando el campo personalizado index.

3. setup.template:

• Define el nombre y patrón de la plantilla que Filebeat usará para indexar los datos en Elasticsearch.

## Posibles vías de mejora 📈
- Crear más tipos de JSON en vez de solo 3

- Darle un TimeOut para que no siga generando JSON

- Implementar Kibana para poder visualizar los datos
  
- Definir un segundo índice o incluso más índices relativos vinculados al timestamp

## Problemas / Retos encontrados ❗
- Nunca había trabajado con Elastic Search ni File Beats, por lo que estuve leyendo documentación de ambas tecnologías durante un tiempo considerable
