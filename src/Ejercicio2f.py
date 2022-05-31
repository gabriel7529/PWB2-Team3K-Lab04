from interpreter import draw
from chessPictures import *
segmento1 = square.join(square.negative())
segmento2 = square.negative().join(square)
horizontal1 = segmento1.horizontalRepeat(3)
horizontal2 = segmento2.horizontalRepeat(3)
segmento3 = horizontal1.up(horizontal2)
vertical = segmento3.verticalRepeat(3)
draw(vertical)