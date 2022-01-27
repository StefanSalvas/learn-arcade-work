#import the arcade
import arcade
arcade.open_window(600, 600, "Drawing example")

# Set the background color
arcade.set_background_color(arcade.csscolor.BLUE)

# Get ready to draw
arcade.start_render()
# Draw snow
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.ALICE_BLUE)
# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SANDY_BROWN)
# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.WHITE_SMOKE)
# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.BANANA_YELLOW)
# Draw a snowman
arcade.draw_circle_filled(250, 320, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(250, 350, 25, arcade.csscolor.WHITE)
arcade.draw_circle_filled(250, 380, 15, arcade.csscolor.WHITE)
#Draw the arms
arcade.draw_line(250, 350, 180, 370, arcade.csscolor.BLACK, 2)
arcade.draw_line(250, 350, 320, 370, arcade.csscolor.BLACK, 2)
#Draw the eyes
arcade.draw_circle_filled(240.12, 380, 3, arcade.csscolor.BLACK)
arcade.draw_circle_filled(260, 380, 3, arcade.csscolor.BLACK)

#Finish drawing
arcade.finish_render()

arcade.run()
