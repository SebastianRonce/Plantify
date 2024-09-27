from Base_de_Datos import plantas
class planta:
    def __init__(self, codigo: int, nombre: str, temperatura: str, riego: str, tiempo_riego: str, altura: str, recomendacion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.temperatura = temperatura
        self.riego = riego
        self.tiempo_riego = tiempo_riego
        self.altura = altura
        self.recomendacion = recomendacion

    def mostrar_planta(self):
        print("-----------------------------------------------------------------------------------------------")
        print(f"Codigo = {self.codigo}")
        print(f"Nombre = {self.nombre}")
        print(f"Temperatura = {self.temperatura}")
        print(f"Riego = {self.riego}")
        print(f"Tiempo de riego = {self.tiempo_riego}")
        print(f"Altura = {self.altura}")
        print(f"Recomendacion = {self.recomendacion}")
        print("----------------------------------------------------------------------------------------------")
        
plantas: list[planta] = []

def buscar_por_nombre(nombre: str):
    for planta in plantas:
        if planta.nombre == nombre:
            planta.mostrar_planta()
            return
    print("La planta no se encuentra en la base de datos ")

def buscar_por_codigo(codigo: int):
    for planta in plantas:
        if planta.codigo == codigo:
            planta.mostrar_planta()
            return
    print("La planta no se encuentra en la base de datos ")

plantas.append(planta(1, "Sabila", "20° a 25°C.", "Una cada 10 o 14 dias.", "Durante 3 minutos.", "20 a 25 Cm.", """ La sabila necesita suelos ricos en materia orgánica
y con buen drenaje que eviten los encharcamientos. """))


def validar_numero(mensaje):
    cantidad = input(mensaje)
    if not cantidad.isnumeric():
        print("ERROR!: ")
        print("--------------------/n")
        return validar_numero(mensaje)
    
    return int(cantidad)

def validar_riego(mensaje):
    texto = input(mensaje)
    if not texto.isalpha():
        print("ERROR!: ")
        print("--------------------\n")
        return validar_riego(mensaje)
    
    return str(texto)

def inventario(opcion_predeterminada=None):
    print("Elige una acción. ")
    print("Buscar, Mostrar, salir. ")
    opcion = input("Escribe que accion deseas realizar. ").lower()

    if opcion == "buscar":
        print("codigo, nombre. ")
        caracteristica = input("Escribe por que caracteristica quieres buscar la planta. ").lower()

        if caracteristica == "codigo":
            codigo = validar_numero("Escribe el codigo de la planta. ")
            buscar_por_codigo(codigo)
        elif caracteristica == "nombre":
            nombre = input("Escribe el nombre de la planta que deseas buscar. ")
            buscar_por_nombre(nombre)
        else:
            return inventario("buscar")
    elif opcion == "mostrar":
        for planta in plantas:
            print("")
            planta.mostrar_planta()
            print("")
    elif opcion == "salir":
        return
    else:
        print("Opción incorrecta. ")

    inventario()


inventario()