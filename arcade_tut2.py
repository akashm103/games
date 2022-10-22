from typing import Tuple, Optional

import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "starterscreen"
SCALING = 0.1


class StarterGame(arcade.Window):
    def __init__(self, fullscreen: bool = False, resizable: bool = False,
                 update_rate: Optional[float] = 1 / 60, ):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, fullscreen, resizable, update_rate)

        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.enemies = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        self.player = arcade.Sprite("robot.png", SCALING)
        self.player.center_x = 10
        self.player.center_y = 200
        self.player.left = 10
        self.all_sprites.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()


def main():
    startgame = StarterGame()
    startgame.setup()
    startgame.run()


if __name__ == '__main__':
    main()
