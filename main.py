class Vehiculo:
    Color = "blanco"
    Ruedas = 0
    Puertas = 0
    
class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 0
    Marca = ""
    Modelo = ""
    def __init__(self, Marca, Modelo):
        self.Marca = Marca
        self.Modelo= Modelo
        self.Puertas = 5
        self.Ruedas = 4
        
    
coche = Coche("Ford", "Focus")
    
print("Mi coche tiene {} puertas, es de color {}, y es un {} {}".format(coche.Puertas, coche.Color, coche.Marca, coche.Modelo))