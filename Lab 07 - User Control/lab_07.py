import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Snowman:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):


        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)

    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x


        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class Body:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color,):


        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)

    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x


        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):


        super().__init__(width, height, title)


        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE)

        # Create our snowman
        self.body = Body(250, 320, 0, 0, 30, arcade.csscolor.WHITE)
        self.ball = Snowman(250, 320, 0, 0, 30, arcade.csscolor.WHITE)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.body.draw()

    def update(self, delta_time):
        self.ball.update()
        self.body.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
        if key == arcade.key.LEFT:
            self.body.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.body.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.body.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.body.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.body.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.body.change_y = 0


def main():
    window = MyGame(800, 600, "Trying to get Snowman")
    arcade.run()


main()