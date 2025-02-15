# Importing site packages
import numpy as np
import os
from PIL import Image

# Creating empty classes

class Canvas():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        #Creating a 3d array for canvas creation
        self.data = np.zeros((self.width,self.height,len(self.color)),dtype=np.uint8)
        # Change color according to user input
        self.data[:] = self.color

    def make(self,imagepath,channel):
        img = Image.fromarray(self.data,channel)
        return img.save(imagepath)

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

        # Create a 3d array of a square
        self.squareData = np.zeros((self.x,self.y,self.color),dtype=np.uint8)
        self.squareData[:] = self.squareData

    def draw(self, canvas):
        pass

class Rectangle:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        pass


canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))
canvas_color = list(map(int,input("Enter the color values (0-255): ").split(",",3)))
# print(canvas_color)
drawCanvas = Canvas(canvas_width,canvas_height,canvas_color).make('canvas_test2.png','RGB')
print(drawCanvas)