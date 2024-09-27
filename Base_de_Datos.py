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
        
    def actualizar_riego(self):
        riego = validar_riego("Escribe cada cuanto es el tiempo de riego: ")
        self.riego = riego

    def actualizar_tiempo_riego(self):
        tiempo_riego = validar_riego("Escribe durante cuanto tiempo se riega la planta: ")
        self.tiempo_riego = tiempo_riego

    def actualizar_planta(self):
        print("riego, tiempo de riego")
        caracteristica = input("Escribe la caracteristica que quieres actualizar de la planta: ")
        if caracteristica == "riego":
            self.actualizar_riego()
        elif caracteristica == "tiempo de riego":
            self.actualizar_tiempo_riego()
        else:
            print("Error, NO se puede actualizar.")

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

plantas.append(planta(2, "Cilantro", "10° a 24°C.", "2 o 3 veces por semana.", "Durante 3 minutos.", "40 a 70 Cm.", """ El cilantro necesita nitrógeno, fósforo y potasio para crecer de manera óptima.
Además de los nutrientes básicos, también requiere calcio, magnesio y azufre."""))

plantas.append(planta(3, "Calathea", "18° a 24°C.", "1 o 2 veces por semnana.", "Metodo de inversión por 15 minutos.", "12 Cm.", """Las Calathea necesita un suelo húmedo, con buena luz pero no directa al sol
 y buena tierra con mezclas vegetales. """))

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
    print("buscar, actualizar, eliminar, mostrar, salir. ")
    opcion = opcion_predeterminada
    if not opcion_predeterminada:
        opcion = input("Escribe que accion deseas realizar. ").lower()

    if opcion == "buscar":
        print("codigo, nombre. ")
        caracteristica = input("Escribe por que caracteristica quieres buscar la planta. ").lower()

        if caracteristica == "codigo":
            codigo = validar_numero("Escribe el codigo de la planta. ")
            buscar_por_codigo(codigo)
        elif caracteristica == "nombre":
            nombre = input("Escribe el nombre de la planta que deseas buscar. ").lower()
            buscar_por_nombre(nombre)
        else:
            return inventario("buscar")
    elif opcion == "actualizar":
        print("codigo, nombre. ")
        opcion_busqueda = input("Escribe por que caracteristica quieres buscar la planta. ")
        for planta in plantas:
            if opcion_busqueda == "nombre":
                nombre = input("Escribe el nombre de la plata. ")
                if nombre == planta.nombre:
                    planta.actualizar_planta()
                    return inventario()
                
            elif opcion_busqueda == "codigo":
                codigo = validar_numero("Escribe el codigo de la planta. ")
                if codigo == planta.codigo:
                    planta.actualizar_planta()
                    return inventario()
    elif opcion == "eliminar":
        print("codigo, nombre")
        opcion_busqueda = input("Escribe por que caracteristica quieres buscar la planta. ")

        for index in range(len(plantas)):
            planta = plantas [index]
            if opcion_busqueda == "nombre":
                nombre = input("Escribe el nombre de la planta. ")
                if nombre == planta.nombre:
                    planta.actualizar_planta()
                    plantas.pop(index)
                    return inventario()
            elif opcion_busqueda == "codigo":
                codigo = validar_numero("Escribe el codigo del producto. ")
                if codigo == planta.codigo:
                    plantas.pop(index)
                    return inventario()
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