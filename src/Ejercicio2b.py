from chessPictures import *
from interpreter import draw

knight_black = knight.negative()
inv1V = knight.verticalMirror()
inv2V = knight_black.verticalMirror()

fil1 = inv2V.join(inv1V)
fil2 = knight.join(knight_black)

draw(fil1.up(fil2))
