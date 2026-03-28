1. EJECUCION DE PROGRAMA
    ejecutar el programa mediante el main.py, el main contiene
    unos datos precargados con los que poder trabajar

    estos son: CMD-01, CMD-02, OP-99 y ADMIN
    asi como las naves, almacenes y un repuesto "Deflector" en el unico almacen, con esto se puede ejecutar todo lo necesario sin tener que entrar en ADMIN para crear nuevos objetos (los objetos repuesto se crean con el OP-99)

2. INICIAR SESION
    Al iniciar un programa pide iniciar sesion, esto son las ID de cada usuario
        CMD-01: Comandante1
        CMD-02: Comandante2
        OP-99: Operario1
        ADMIN: Admin

3. ACCIONES DE USUARIO
    cada usuario tiene unas acciones diferentes

    COMANDANTE:
        ENCONTRAR REPUESTO: Pide al usuario el nombre del repuesto, y devuelve en que almacenes se encuentra y en que cantidad

        ADQUIRIR REPUESTO: Pide al usuario el nombre del repuesto, el almacen y la cantidad y suma esa cantidad a la nave y la resta al almacen

        ENVIAR MENSAJE: Pide al usuario la clave de destino (número) y el texto del mensaje, y transfiere la comunicación a la bandeja de la nave correspondiente.

        CONSULTAR MENSAJES: No pide parámetros, simplemente lee y muestra por pantalla todos los mensajes que ha recibido la nave que el comandante tiene asignada.

        CONSULTAR NAVE: Devuelve el numero de repuestos de la nave

    OPERARIO:
        ACTUALIZAR STOCK: Pide al usuario el nombre de un repuesto que ya exista y la cantidad a sumar, y actualiza el inventario disponible en su almacén.

        CONSULTAR ALMACÉN: No pide parámetros, revisa el catálogo de su almacén asignado y devuelve una lista detallada con todas las piezas y sus cantidades actuales.

        CREAR NUEVO REPUESTO: Pide al usuario los datos necesarios para crear un objeto repuesto y lo asigna al almacen correspondiente del usuario

    ADMIN:
        CREAR COMANDANTE: Pide al usuario los datos básicos (ID y nombre) y la nave que se le va a asignar, y lo registra en el sistema como un nuevo usuario con permisos para acceder a la flota.

        CREAR OPERARIO: Pide al usuario los datos básicos (ID y nombre) y el almacén donde va a trabajar, y lo registra en el sistema como un nuevo usuario con permisos de logística.

        CREAR NAVE: Pide al usuario el tipo específico de nave (Estación Espacial, Nave Estelar o Caza Estelar) junto con sus atributos correspondientes (nombre, identificador, clave, tripulación, etc.), y la añade a la flota operativa del Imperio.

        CREAR ALMACÉN: Pide al usuario el nombre de la nueva instalación y su ubicación, y lo añade a la red logística del sistema para que pueda empezar a recibir repuestos.

        LISTA USUARIOS: No pide parámetros, simplemente muestra por pantalla un listado con todos los usuarios (tanto comandantes como operarios) que están dados de alta actualmente en el sistema.

        LISTA NAVES: No pide parámetros, devuelve por pantalla un listado completo de todas las naves y estaciones espaciales registradas en la base de datos.

        LISTA ALMACENES: No pide parámetros, imprime por pantalla la lista de todos los almacenes físicos dados de alta y sus ubicaciones.


    Decisiones: En todos los casos el pgroama mira siemrpe la estacion de trabajo del usuario (naves y almacenes) y para hacer cualquier accion acude al atributo de ese usuario para acceder a esa estacion.

    

4. TEST
    ejecutar con Pytest
