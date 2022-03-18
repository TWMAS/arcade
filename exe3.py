'''DIBUIXANT ELEMENTS
La llibreria arcade disposa d'unes primitives (funcions de dibuix) que ens permeten dibuixar:'''
import arcade
def arbre (px,py,e):
    arcade.draw_lrtb_rectangle_filled(px, (e*30)+px, (e*120)+py, py, arcade.csscolor.BROWN)
    arcade.draw_circle_filled((e*15)+px, (e*140)+py, (e*60), arcade.csscolor.DARK_GREEN)

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()
arbre(300,300,0.4)

#tronc


"""
#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_lrtb_rectangle_filled(250, 350, 300, 70, arcade.csscolor.BROWN)
arcade.draw_circle_filled(400, 350, 100, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(200, 300, 90, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(270, 300, 70, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(270, 400, 150, arcade.csscolor.DARK_GREEN)
"""

#Cercles: 
"""def arbre (x,y):
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
    arcade.draw_lrtb_rectangle_filled(250, 350, 300, 70, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(400, 350, 100, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(200, 300, 90, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(270, 300, 70, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(270, 400, 150, arcade.csscolor.DARK_GREEN)
"""

#arcade.draw_text("Arbor Day - Plant a Tree!",150, 230,arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
