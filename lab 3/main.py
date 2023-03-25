#import reverse_polish_notation as rpn
import random
from reverse_polish_notation import *
from monte_carlo import approximate_pi
import simply_draw as sd
from l_system import draw
def main():
    #print(rvp("((2+7)/3+(8-3)*4)/2")) # 2 7 + 3 / 8 3 − 4 * + 2 /
    #print(solve("2 7 + 3 / 14 3 - 4 * + 2 /"))
    #print(approximate_pi())
    #sd.draw_rect()
    #sd.draw_star()
    #sd.draw_reg_poly(11)
    draw()

if __name__ == "__main__":
    main()