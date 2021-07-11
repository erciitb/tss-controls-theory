# Hello! Welcome to the week 2 assignment!

# This file contains the starter code for the method related to distance from path.
# Your goal with this file will be to implement the PID part of the project.

# If you run the file now(python line_follower_dist.py) you should be able to see
# the environment for drawing and the car ready.

# You can draw a path using your mouse starting from any point on the canvas and the
# car should accordingly reposition and start moving along a straight line.

# It is your job to make the car follow the line, all on its own, without any help
# from you!

# Certain functions in this file deal with stuff that you do not need to bother much
# about, since they deal with the aesthetics, getting pygame to work, etc.
# I have mentioned something like "Ignore this function" or similar near those.

# Contrary to the above, there are certain parts of the code that you must study
# carefully in order to complete your implementation properly. For example
# understanding the usage of some methods/properties of the class Car will be important.

# Now go over to the PID() function and read on.

import pygame
import math
import os

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Follower")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

DARK_GREY = (90, 90, 90)
LIGHT_GREY = (180, 180, 180)

BG_COLOR = LIGHT_GREY
PAINT = DARK_GREY

screen.fill(BG_COLOR)
pygame.display.flip()

mouse = pygame.mouse
canvas = screen.copy()

# This variable is pivotal to the program
# It contains a list(similar to an array from cpp) of all the points in the path as drawn
# by the mouse of the user.
# This is pretty much our definition of the path. You can use this to calculate distance,
# angle, etc. There are many ways to implement functions to find each of these so don't
# be afraid to experiment.
# Now head over to the while loop at the bottom of the file.
points = []

THRESHOLD = 0.001
TIME_PER_FRAME = 50


# Important methods and properties
# 1. Car.turn(theta)
# 2. Car.direction
# 3. Car.pos
class Car:
    def __init__(self, surface):
        self.direction = pygame.Vector2(1, 0)  # direction of car
        self.is_set = False  # is the car set to the initial position(based on path drawn)
        self.pos = pygame.math.Vector2(100, 400)  # position of the center of the car
        self.theta = 0  # angle of the car with positive x
        self.surface = surface  # surface on which car is drawn
        self.speed = 1.5  # speed of the car
        self.img_original = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'car.png')),
                                                   (100, 100))  # the original image of the car
        self.img = self.img_original  # the current image to be drawn

    def draw(self):
        if len(points) > 1:
            self.step()
        self.surface.blit(self.img, self.pos - pygame.Vector2(self.img.get_size()) / 2)

    def step(self):
        self.pos += self.direction * self.speed

    def turn(self, theta):
        self.theta += theta
        self.direction = pygame.Vector2(math.cos(self.theta), math.sin(self.theta))
        self.img = pygame.transform.rotate(self.img_original, - 180 * self.theta / math.pi)
        self.img = self.img.convert_alpha()

    def set_car(self):
        if len(points) < 10 or car.is_set:
            return
        self.pos = pygame.Vector2(list(points[0]))
        for i, point in enumerate(points):
            if (point - points[0]).magnitude() != 0:
                self.direction = point - points[0]
                self.direction /= self.direction.magnitude()
                self.turn(math.atan2(self.direction.y, self.direction.x))
                self.is_set = True
                return


prev_x = None
prev_y = None


# Ignore this function completely: Helps in drawing the path with mouse
def draw_path(brush_size=20, steps=200):
    global prev_x
    global prev_y

    x, y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, PAINT, (x, y), brush_size)

    click = pygame.mouse.get_pressed(3)
    if click[0] == 1:
        if 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
            pygame.draw.circle(canvas, PAINT, (x, y), brush_size)

        if prev_x is not None:
            diff_x = x - prev_x
            diff_y = y - prev_y
            steps = max(abs(diff_x), abs(diff_y), steps)
            if steps > 0:
                dx = diff_x / steps
                dy = diff_y / steps
                for _ in range(steps):
                    prev_x += dx
                    prev_y += dy
                    pygame.draw.circle(canvas, PAINT, (round(prev_x), round(prev_y)), brush_size)
                    points.append(pygame.math.Vector2(prev_x, prev_y))
        prev_x = x
        prev_y = y
    else:
        prev_x = None
        prev_y = None


def PID():
    return 0
    # This function will contain the meat of your program. You have to design this function
    # to return the angle by which the car should rotate to follow along the path.
    # Think about what parameters you could input, the one I tried was perpendicular distance,
    # but you might also want to try and come up with your own ideas.
    # The parameter will provide you an error term and then you follow standard PID.
    # Now head over to the definition of the points variable towards the top of the file


# This is the game loop, where all the magic happens.
# This loop will keep running while the game is still on the screen. Now the important part
# that you need to pay attention to is the if condition inside of which PID() and car.turn(angle)
# are called.
# If you are going to be calculating some parameters as input for your PID function then you may
# calculate them right before the call to PID() and take them as params.
# Now you should be all set to get working on the project, best of luck!
clock = pygame.time.Clock()
loop = True
car = Car(screen)
while loop:
    clock.tick(TIME_PER_FRAME)
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed(3)

    screen.fill(BG_COLOR)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    draw_path(brush_size=30)
    car.draw()

    if len(points) > 1 and car.is_set:
        angle = PID()
        car.turn(angle)

    if not car.is_set and len(points) > 1:
        car.set_car()
    pygame.display.flip()

pygame.quit()
