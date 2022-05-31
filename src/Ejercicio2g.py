from interpreter import draw
from chessPictures import *
bloque1 = rock.join(knight).join(bishop)
bloque2 = bloque1.verticalMirror()
bloque3 = bloque1.join(queen).join(king).join(bloque2)
peones = pawn.horizontalRepeat(7)
piezazBlancas = bloque3.up(peones)
segmento1 = square.join(square.negative())
segmento2 = square.negative().join(square)
horizontal1 = segmento1.horizontalRepeat(3)
horizontal2 = segmento2.horizontalRepeat(3)
segmento3 = horizontal2.up(horizontal1)
union1 = segmento3.under(piezazBlancas)
draw(union1)