from Car import Car
import random
import pygame

class Player(Car):

    def __init__(self, player_name, x_coord, y_coord):
        super().__init__(x_coord,y_coord)
        self.name = player_name
        self.carModelPhoto = self.setCarModelPhoto()
