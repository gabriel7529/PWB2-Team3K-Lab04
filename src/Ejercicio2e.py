from interpreter import draw
from chessPictures import *

figura = Picture.join(square.negative(), square)
figuraT = Picture.horizontalRepeat(figura, 3)
draw(figuraT)

