from abc import ABC
from enums import *
from excepciones import *


class Repuesto:
    def __init__(self, nombre: str, proveedor: str, cantidad: int, coste: float):
        self.nombre = nombre
        self.proveedor = proveedor

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.__cantidad = cantidad 

        if coste < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.coste = coste

    # --getters--
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_proveedor(self) -> str:
        return self.proveedor
    
    def get_coste(self) -> float:
        return self.coste

    def get_cantidad(self) -> int:
        return self.__cantidad


    # --seters--
    def set_nombre(self,nombre:str):
        self.nombre = nombre

    def set_proveedor(self,proveedor: str):
        self.proveedor = proveedor

    def set_coste(self,coste:float):
        if coste < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.coste = coste

    def set_cantidad(self, cantidad: int):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.__cantidad = cantidad

class Almacen:

    def __init__(self, nombre: str, localizacion: str):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo_piezas = [] 


    #geters 
    def get_nombre(self):
        return self.nombre
    
    def get_localizacion(self):
        return self.localizacion

    def get_catalogo(self):
        return self.catalogo_piezas

    #setters

    def set_nombre(self, nombre:str):
        self.nombre = nombre

    def set_localizacion(self,localizacion:str):
        self.localizacion = localizacion

    #metodos 
    def agregar_repuesto(self, repuesto: Repuesto):
        self.catalogo_piezas.append(repuesto)

    def buscar_repuesto(self, nombre: str) -> Repuesto:
        """
        El metodo busca dentro del catalogo si existe 
        el repuesto que se se esta buscando

        busca por el nombre no por el objeto

        si no lo encuentra devuelve un -1
        """

        for repuesto in self.get_catalogo():
            if repuesto.get_nombre() == nombre():
                return repuesto
        return (-1)
    
    
class Nave(ABC):

    """
    Clase Nave

    Atributos:
        nombre -> string
        Repuestos -> []
            Repuestos es una lista de que contiene
            los diferentes tipos de repuestos dentro
            de una nave (la lista son de objetos tipo string 
            por lo que seran los nombres)

    Metodos
        mostrar_informacion():
            devuelve un string con la informacion basica de la nave
        añadir_repuestos():
            el metodo añade a la lista un repuesto nuevo
    """

    def __init__(self, nombre:str,**kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.repuestos = []

    #getter

    def get_nombre(self):
        return self.nombre

    def get_repuestos(self):
        return self.repuestos
    
    #setter

    def set_nombre(self,nombre:str):
        self.nombre = nombre

    #metodos

    def mostrar_informacion(self):
        return f"Nombre de nave: {self.get_nombre}\nNumero de repuestos: {len(self.get_repuestos())}"


    def añadir_repuestos(self,repuesto:str):

        # REVISAR PQ NO CUADRA QUE SEA UN STR PARA TEMA DUPLICADOS

        self.get_repuestos().append(repuesto)

class UnidadCombate(ABC):

    def __init__(self, identificador:str,clave_transmision:int, **kwargs):
        super().__init__(**kwargs)
        self.identificador = identificador
        self.clave_transmision = clave_transmision

    #geters
    def get_identificador(self):
        return self.identificador
    
    def get_clave_transmision(self):
        return self.clave_transmision
    
    #setters

    def set_identificador(self, identificador:str):
        self.identificador = identificador

    def set_clave_transmision(self, clave_transmision:int):
        self.clave_transmision = clave_transmision

class NaveEstelar(Nave, UnidadCombate):
    def __init__(self, nombre: str, identificador: str, clave_transmision: int, tripulacion: int, pasaje: int, clase: EClaseNave):
        super().__init__(nombre=nombre, identificador=identificador, clave_transmision=clave_transmision)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

class EstacionEspacial(Nave, UnidadCombate):
    def __init__(self, nombre: str, identificador: str, clave_transmision: int, tripulacion: int, pasaje: int, ubicacion: EUbicacion):
        super().__init__(nombre=nombre, identificador=identificador, clave_transmision=clave_transmision)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class CazaEstelar(Nave, UnidadCombate):
    def __init__(self, nombre: str, identificador: str, clave_transmision: int, dotacion: int):
        super().__init__(nombre=nombre, identificador=identificador, clave_transmision=clave_transmision)
        self.dotacion = dotacion

class Usuario(ABC):
    def __init__(self,ID:str,nombre:str):
        self.ID = ID
        self.nombre=nombre


class Comandante(Usuario):
    def __init__(self, ID, nombre,nave:Nave):
        super().__init__(ID, nombre)
        self.nave = nave

    def get_nave(self):
        return self.nave
    
    def set_nave(self,nave:Nave):
        self.nave = nave

class Operario(Usuario):
    def __init__(self, ID, nombre,almacen:Almacen):
        super().__init__(ID, nombre)
        self.almacen = almacen

    def get_almacen(self):
        return self.almacen
    
    def set_almacen(self, almacen:Almacen):
        self.almacen = almacen

class Admin(Usuario):
    def __init__(self, ID, nombre):
        super().__init__(ID, nombre)