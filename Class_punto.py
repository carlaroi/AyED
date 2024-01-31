import math

class Punto: #Creamos la clase punto 
  def __init__(self, x=0, y=0) 
    self.x = x
    self.y = y

  def __string__(self) #Sobreescribimos el método string para imprimir en el formato (x,y)
    return f"({self.x, self.y})"
    
