from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    return Picture(None)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    lista = self.img
    lista2 = p.img
    for x in range(len(lista2)):
      for y in range(len(lista2[x])):
        # Se recorre entre todos los caracteres del objeto que ingresa
        print(lista2[x][y:y+1]) 
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    lista = self.img
    lista2 = []
    cadena = ""
    for i in range(len(lista)):
        for x in range(n+1):
            cadena = cadena+lista[i]
        lista2.append(cadena)
        cadena = ""
    return Picture(lista2)

  def verticalRepeat(self, n):
    lista = self.img
    lista2 = []
    for x in range(n+1):
        lista2 = lista2+lista
    return Picture(lista2)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

