
import pygame
import math


class SoundEvent(object):

    def __init__(self):
        pygame.init()
        self.sound = pygame.mixer.Sound('sound/beep.wav')
        self.sound.set_volume(0)
        self.old_x = 0
        self.old_y = 0
        self.old_diff = (0, 0, 0)
        self.min_movement = 2

    def get_movement(self, x, y):
        return math.sqrt(pow(self.old_x - x, 2) + pow(self.old_y - y, 2))

    def mag(self, diff):
        inner = pow(diff[0], 2.0) + pow(diff[1], 2.0) + pow(diff[2], 2.0)
        max_inner = 3.0 * pow(255, 2.0)
        return math.sqrt(inner / max_inner)

    def get_diff(self, color):
        return (color[0] - self.old_diff[0],
                color[1] - self.old_diff[1],
                color[2] - self.old_diff[2])

    def run(self, **kwargs):
        for event in pygame.event.get():
            pass

        x = kwargs.get("x", 0)
        y = kwargs.get("y", 0)
        current_color = kwargs.get("color", (0, 0, 0))
        diff = self.get_diff(current_color)
        movement = self.get_movement(x, y)
        diff_mag = self.mag(diff)
        self.sound.set_volume(diff_mag)
        self.sound.play()
        self.old_x = x
        self.old_y = y
        self.old_diff = diff
