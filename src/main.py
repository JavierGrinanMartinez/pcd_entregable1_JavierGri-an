from clases import NaveEstelar, Almacen, Repuesto, Comandante, Operario
from enums import EClaseNave
from sistema import Sistema
from excepciones import UsuarioNoEncontradoError, AccesoDenegadoError, StockInsuficienteError


sistema = Sistema()
#
base_endor = Almacen("Almacen de endor","Endor")
destructor = NaveEstelar("ejecutor","ID-001",12345,25000,38000,EClaseNave.EJECUTOR)

Vader = Comandante("VADER-01","Darth Vader",destructor)
operario1 = Operario("OP-01","Operario1",base_endor)

sistema.registrar_almacenes(base_endor)
sistema.registrar_naves(destructor)

sistema.registrar_usuario(Vader)
sistema.registrar_usuario(operario1)
#



#pruebas

print(sistema.iniciar_sesion("OP-01"))
sistema.cerrar_sesion()

print(sistema.iniciar_sesion("OP-01"))
sistema.crear_repuesto("aleron","provedor",50,100)
