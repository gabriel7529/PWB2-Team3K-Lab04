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
    auxself = self.img
    newfigura = []
    for n in range (len(auxself)):
      newfigura.append(auxself[n] + p.img[n])
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(newfigura)

  def up(self, p):
    auxself = self.img
    newfigura = p.img + auxself
    """ Devuelve una nueva figura poniendo la figura recibida como argumento,
        encima de la figura actual """
    return Picture(newfigura)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
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

