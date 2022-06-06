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
    lista = self.img
    lista2 = p.img
    for x in range(len(lista2)):
      for y in range(len(lista2[x])):
        if lista2[x][y:y+1] != " ":
          linea = list(lista[x])
          linea[y] = lista2[x][y:y+1]
          lista[x] = "".join(linea)
    return Picture(lista)
  
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

