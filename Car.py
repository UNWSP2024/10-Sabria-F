#By: Sabria Fafach
#Date: April 4, 2025
#Title: Car.py

class car:
    def __init__(self,ymod,make):
        self.__year_model=ymod
        self.__make=make
        self.__speed=0

    def accelerate(self):
        self.__speed+=5

    def brake(self):
        self.__speed-=5

    def get_speed(self):
        return self.__speed














