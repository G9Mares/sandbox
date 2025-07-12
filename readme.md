# Arquteggture

Basada en Features y funciones, que se joda la hexagonal

## Carpetas

### Controllers
Sirve para crear motores de tecnologia externos, como ORMS permite crear funciones generales que se puedan llamar en todo el proyecto, evita andar creando como menso querys por doquier

### Features
Almacena los modulos o entidades que posera tu proyecto, cada carpeta contiene:
{tecnologic}_engine:(De momento solo considera fuentes de datos)
    model:
        Contiene los modelos que usaras junto con los controllers, si usas SQLalchemy necesitas delcar un modelo de esos ahi
    service:
        Es importante que los metodos vayan dentro de una clase y si agregas nuevas tecnologias como redis repliques las mismas funcionalidades 

        El service manda hablar el controller depende del proyecto puedes o declarar la session del controller en el init de la clase o el archivo o pasarlo como parametro, eso permitiria infraestructuras o funcionalidades mas locas
routes:
    Es donde se declaran los endpoints


## Generales 

No crea los modelos en la base de datos, se requeire que ya existan y hace flata pasar el paremtro de session en el controller de ejemplo por que me dio hueva

    