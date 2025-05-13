## Instalación Entorno de Desarrollo 

Crear el entorno Virtual de Pyhton

```bash
  python -m venv venv
```

Activar entorno Virtual de Pyhton

```bash
  venv\Scripts\activate  ó Activar mediante selecionar interprete de Visual Studio
```
   

Instalar Dependencias del Proyecto

```bash
  pip install -r requirements.txt
```


## Variables de Entorno

Para la correcta conexión con la base de dato y el adecuado funcionamiento del proyecto es obligatorio crear y rellenar el archivo .env en la carpeta principal (core) con las siguientes variables de entorno (La base de datos utilizada es postgresql)

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`

`FRONT_URL`

## Migración y Ejecución del Proyecto

Como último paso, es necesario migrar la base de datos para así poder ejecutar el proyecto sin problemas 

Migración:
```bash
  python manage.py migrate
```

Ejecución
```bash
  python manage.py runserver
```

## Guardar nuevas dependencias creadas

Es importante que sí agregamos dependencias al proyecto, antes de subir los cambios ejecutemos el siguiente comando
```bash
  pip freeze > requirements.txt  
```
Esto Actualizará el archivo de requerimientos utilizado anteriormente 
