# Arquteggture

Basada en Features y funciones, que se joda la hexagonal

## Carpetas

### Controllers
Sirve para crear motores de tecnologia externos, como ORMS permite crear funciones generales que se puedan llamar en todo el proyecto, evita andar creando como menso querys por doquier

### Features
Almacena los modulos o entidades que posera tu proyecto, cada carpeta contiene:
    tal vez model y service deberian ir la misma carpeta
    model:
        Contiene los modelos que usaras junto con los controllers, si usas SQLalchemy necesitas delcar un modelo de esos ahi
    service:
        El service sirve para ejecutar todo lo que tenga que ver con la fuente de datos en este caso el controller, aun si ocupa modelos o joins de otras features
    logic?:
        Es donde la va la logica del negocio, es opcional y tiene que ir separado del service
    test?: es opcional
    routes:
        Es donde se declaran los endpoints

    ---
    El ***Call Stack***debe ser el siguiente:
    1. Route -> Es el punto de entrada de la app desde aqui se habla a los elementos de logic y     service dando prioridad a logic 
    2. Logic 
    3. Service 

    Es importante nunca llamar al service dentro de logic o visceversa, eso permite que este separado y sea facil de desacoplar y testear

## Generales 

No crea los modelos en la base de datos, se requeire que ya existan y hace flata pasar el paremtro de session en el controller de ejemplo por que me dio hueva

    