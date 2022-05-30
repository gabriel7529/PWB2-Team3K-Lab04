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
    lista = self.img 
    cadena = ""
    listaV = []
    for i in lista:
      for letra in i:
        cadena = letra + cadena
      listaV.append(cadena)
      cadena = ""  
    return Picture(listaV)
    

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    lista = self.img
    listaH = []
    x = len(lista) - 1
    while x > 0:
      listaH.append(lista[x])
      x -=1
    return Picture(listaH)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    lista = self.img
    listaN = []
    aux1 = aux2 = aux3 = aux4 = False
    x = len(lista)-32  #mitad de los string de img
    if -1 != lista[x].find("="): 
      aux1 = True
    if -1 != lista[x].find("_"):
      aux2 = True
    if -1 != lista[x].find("."):
      aux3 = True
    if -1 != lista[x].find("@"):
      aux4 = True  
    for i in lista:
      if aux1:
        i = i.replace("=",self._invColor("="))
      if aux2:
        i=i.replace("_",self._invColor("_"))
      if aux3:
        i=i.replace(".",self._invColor("."))
      if aux4:
        i=i.replace("@",self._invColor("@"))
      listaN.append(i)      
    return Picture(listaN)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

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

