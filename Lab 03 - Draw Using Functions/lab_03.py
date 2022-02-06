# Library imports
import arcade

# Constants - variables that do not change
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing With Functions Example"


def draw_background():
    """
    This function draws the background. Specifically, the sky and ground.
    """
    # Draw the sky in the top two-thirds
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1 / 3),
                                      arcade.color.SKY_BLUE)

    # Draw the ground in the bottom third
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 3,
                                      0,
                                      arcade.color.DARK_BLUE)


def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)


def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


def draw_sun(x, y):
    """
    This function draws a sun.
    """
    # Draw the sun
    arcade.draw_circle_filled(530, 500, 105, arcade.csscolor.YELLOW)
def draw_snowman(x, y):
    """
    This function draws a snowman
    """
    # Draw a snowman
    arcade.draw_circle_filled(150, 120, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(150, 150, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(150, 180, 15, arcade.csscolor.WHITE)
    # Draw the arms
    arcade.draw_line(150, 150, 80, 170, arcade.csscolor.BLACK, 2)
    arcade.draw_line(150, 150, 230, 180, arcade.csscolor.BLACK, 2)

    # Draw the eyes
    arcade.draw_circle_filled(140.12, 180, 4, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(160, 180, 4, arcade.csscolor.BLACK)


def main():
    """
    This is the main program.
    """

    # Open the window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()

    # Call our drawing functions.
    draw_background()
    draw_pine_tree(50, 250)
    draw_pine_tree(350, 320)
    draw_bird(70, 500)
    draw_bird(470, 550)
    draw_sun(580, 575)
    draw_snowman(130, 230)

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


if __name__ == "__main__":
    main()
