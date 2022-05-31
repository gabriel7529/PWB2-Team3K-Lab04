from interpreter import draw
from chessPictures import *

figura = Picture.join(square,square.negative())
figuraT = Picture.horizontalRepeat(figura,3)
draw(figuraT)
