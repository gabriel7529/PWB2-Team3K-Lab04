from chessPictures import *
from interpreter import draw

knight_black = knight.negative()

fil1 = knight_black.join(knight)
fil2 = knight.join(knight_black)

draw(fil1.up(fil2))