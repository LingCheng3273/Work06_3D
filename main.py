from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
red = [255, 0, 0]

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, transform, screen, color )

##matrix = new_matrix()
##add_sphere(matrix, 300, 300, 300, 50, 100)
##for point in range (len(matrix)):
##    draw_line( int(matrix[point][0]),
##                   int(matrix[point][1]),
##                   int(matrix[point][0]),
##                   int(matrix[point][1]),
##                   screen, color)
##
##display(screen)
