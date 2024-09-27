class planta:
    def __init__(self, codigo: int, nombre: str, temperatura: str, riego: str, tiempo_riego: str, altura: str, recomendacion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.temperatura = temperatura
        self.riego = riego
        self.tiempo_riego = tiempo_riego
        self.altura = altura
        self.recomendacion = recomendacion

plantas: list[planta] = []

plantas.append(planta(1, "Sabila", "20° a 25°C.", "Una cada 10 o 14 dias.", "Durante 3 minutos.", "20 a 25 Cm.", """ La sabila necesita suelos ricos en materia orgánica
y con buen drenaje que eviten los encharcamientos. """))

plantas.append(planta(2, "Cilantro", "10° a 24°C.", "2 o 3 veces por semana.", "Durante 3 minutos.", "40 a 70 Cm.", """ El cilantro necesita nitrógeno, fósforo y potasio para crecer de manera óptima.
Además de los nutrientes básicos, también requiere calcio, magnesio y azufre."""))

plantas.append(planta(3, "Calathea", "18° a 24°C.", "1 o 2 veces por semnana.", "Metodo de inversión por 15 minutos.", "12 Cm.", """Las Calathea necesita un suelo húmedo, con buena luz pero no directa al sol
 y buena tierra con mezclas vegetales. """))

