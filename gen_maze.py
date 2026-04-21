#
# Maze / map loading, pygame window, and rendering.
# Based on genMaze Version 1.0 Phil Smith May 2016
#
import pygame
from car import *

filedata = []
Walls = []
Screen = ""
background = ""
maxRows = 0
maxCols = 0

def main(fn, robot):

    print("gen_maze version 1.3.0.2")
    # robot = Car()
    global Screen, background
    # screen_size is a tuple
    screen_size = load_file(fn)
    # print(filedata)
    Screen = init(screen_size)
    # initialise walls
    init_car(robot)

    # Create The Backgound
    background = pygame.Surface(Screen.get_size())
    background = background.convert()
    background.fill((200, 200, 200))
    # Create the pygame clock object
    clock = pygame.time.Clock()
    # Desired FPS
    FPS = 30
    # do not go faster then the frame rate
    # milliseconds = clock.tick(FPS)
    pygame.time.Clock().tick(FPS)

    # Draw Everything
    render(robot)


def render(car):
    # print("render")
    global Screen, background

    Screen.blit(background, (0, 0))
    # Plot the Maze
    blockcolor = pygame.Color(255,255,255)
    playcolor = pygame.Color(0,255,0)
    linecolor = pygame.Color(0,0,0)
    stationcolor = pygame.Color(100,100,100)
    #ycnt = len(filedata)
    #xcnt = len(filedata[0])
    # print("Size = X:%s Y:%s" % (str(xcnt),str(ycnt)))
    ycnt = 0
    for y in filedata:
        xcnt = 0
        ypos = ycnt * 20
        for x in y:
            # print("X:%s Y:%s value:%s" % (str(xcnt),str(ycnt),str(x)))
            if x == "0":
                xpos = xcnt * 20
                pygame.draw.rect(Screen,linecolor,(xpos,ypos, 20,20),0)
            if x == "1":
                xpos = xcnt * 20
                pygame.draw.rect(Screen,blockcolor,(xpos,ypos, 20,20),0)
            if int(x) > 3:
                xpos = xcnt * 20
                pygame.draw.rect(Screen,stationcolor,(xpos,ypos, 20,20),0)
            xcnt += 1
        ycnt += 1

    # Plot the car
        ypos =  car.line * 20
        xpos = car.col * 20
        pygame.draw.rect(Screen,playcolor,(xpos+2,ypos+2, 16,16),0)

    pygame.display.update()

def init_car(car):
    global filedata
    ycnt = 0
    for y in filedata:
        xcnt = 0
        for x in y:
            # print("X:%s Y:%s value:%s" % (str(xcnt),str(ycnt),str(x)))
            if x == "2":
                car.line = ycnt
                car.col = xcnt
                # print("Car Y: %s X: %s" % (str(ycnt), str(xcnt)))
                return
                # pygame.draw.rect(scr,playcolor,(xpos+2,ypos+2, 16,16),0)
            xcnt += 1
        ycnt += 1

def init(scr_size):
    if not pygame.font: print ('Warning, fonts disabled')
    if not pygame.mixer: print ('Warning, sound disabled')
    # Initialize Everything
    pygame.init()
    pygame.display.set_caption('Car Game')
    pygame.mouse.set_visible(0)
    return pygame.display.set_mode(scr_size)

def close_Maze():
    pygame.quit()

def load_file(fn):
    # default values for screen width and height
    global maxRows, maxCols, filedata
    scrwidth = 500
    scrheight = 500
    f = open(fn, 'r')
    # filedata = f.read().splitlines()
    for line in f:
        # print(line)
        line=line.rstrip()
        Wall = line.split(',')
        filedata.append(Wall)
    #
    # calculate the actual screen size
    # each block is a 20x20 pixels
    scrheight = len(filedata) * 20
    maxRows = len(filedata)
    # print("Screen width: %s" % str(scrwidth))
    scrwidth = len(filedata[0]) * 20
    maxCols = len(filedata[0])
    # print("Screen height: %s" % str(scrheight))
    # return a tuple
    return scrwidth,scrheight

def isAWall(x,y):
    if filedata[y][x] == 1:
        return True
    else:
        return False

def isALine(x,y):
    if filedata[y,x] == 0:
        return True
    else:
        return False

def return_data(x,y):
    return filedata[y][x]

if __name__ == "__main__":
	main("DemoMaze.csv",Car())
