from interpreter import draw
from chessPictures import *
bloque1 = rock.join(knight).join(bishop)
bloque2 = bloque1.verticalMirror()
piezazBlancas = bloque1.join(queen).join(king).join(bloque2)
draw(piezazBlancas)