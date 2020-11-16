import pygame
import time
import random
import os
fps = 60
bgr = 255
bgb = 255
bgg = 255
Clock = pygame.time.Clock()
clear = lambda: os.system('cls')
bgrandomb = False
bgrandomr = False
bgrandomg = False
randomcr = False
randomcb = False
randomcg = False
r = 255
g = 0
b = 0
x2 = 1500
y2 = 1000
xSpos = 750
ySpos = 500
yvel = 20
xvel = 15
xsize = 50
ysize = 50
setupdone = False
clear()
print("This is the setup.") 
print("Type help for a list of commands.")
while not setupdone:
    question = input(">>>")
#help
    if question == ("help"):    
        print("Useable commands include:")
        print("-start")
        print("-colour")
        print("-resolution")
        print("-help")
        print("-speed")
        print("-exit")
        print("-spos")
        print("-fps")
        print("-background")
        print("-size")
        print("-config")
    elif question == ('help start'):
        print("Start exits the setup and launches a pygame window.")
    elif question == ("help spos"):
        print("Spos lets you change the start position of the cube.")
    elif question == ("help colour"):
        print("Colour lets you change the colour of the cube.")
    elif question == ("help resolution") or question == ("help res"):
        print("Resolution lets you change the size of the pygame window.")
    elif question == ("help speed"):
        print("Speed allows you to change the vertical and horizontal speed of the cube.")
    elif question == ("help exit"):
        print("Exits the program.")
    elif question == ("help fps"):
        print("Fps allows you to change the maximum fps of the pygame window.")
    elif question == ("help background") or question == ("help bg"):
        print("Background lets you change the colour of the background.")     
    elif question == ("help config"):
        print("Config loads a basic configuration that is meant for testing purposes.")
    elif question == ("help size"):
        print("Size lets you change the height and width of the cube.")
#start
    elif question == ("start"):
        print("Have you set up the color, the resolution, the speed and the startposition?")
        question2 = input()
        if question2 == ("y") or question2 == ("yes"):
            setupdone = True
#colour
    elif question == ("colour"):
        rcolorsetup = True
        while rcolorsetup == True:
            print("Give me a red value under 256.")
            rcolor = input()
            if rcolor.isdigit():
                rcolor = int(rcolor)
                if rcolor > (255):
                    print("I require a value under 256.")
                elif rcolor < (0):
                    print("I require a value above -1")
                else:
                    r = rcolor
                    rcolorsetup = False
                    randomcr = False
            elif rcolor == ('random'):
                randomcr = True
                rcolorsetup = False
                
            else:
                print("I require an interger")



        bcolorsetup = True
        while bcolorsetup == True:
            print("Give me a blue value under 256.")
            bcolor = input()
            if bcolor.isdigit():
                bcolor = int(bcolor)
                if bcolor > (255):
                    print("I require a value under 256.")
                elif bcolor < (0):
                    print("I require a value above -1")
                else:
                    b = bcolor
                    bcolorsetup = False
                    randomcb = False
            elif bcolor == ('random'):
                randomcb = True
                bcolorsetup = False
            else:
                print("I require an interger.")


        gcolorsetup = True
        while gcolorsetup == True:
            print("Give me a green value under 256.")
            gcolor = input()
            if gcolor.isdigit():
                gcolor = int(gcolor)
                if gcolor > (255):
                    print("I require a value under 256.")
                elif gcolor < (0):
                    print("I require a value above -1")
                else:
                    g = gcolor
                    gcolorsetup = False
                    randomcg = False
            elif gcolor == ('random'):
                randomcg = True
                gcolorsetup = False
            else:
                print("I require an interger.")
#resolution
    elif question == ("resolution") or question == ('res'):
        xsetup = True
        while xsetup == True:
            print("Give me a value for the x resolution of the window.")
            xcolor = input()
            if xcolor.isdigit():
                xcolor = int(xcolor)
                x2 = xcolor
                xsetup = False
            else:
                print("I require a valid value.")
        ysetup = True
        while ysetup == True:
            print("Give me a value for the y resolution of the window.")
            ycolor = input()
            if ycolor.isdigit():
                ycolor = int(ycolor)
                y2 = ycolor
                ysetup = False
            else:
                print("I require a valid value.")
#speed
    elif question == ("speed"):
        xspeedGot = False
        while not xspeedGot:
            print("Give me a p/f(pixels per frame) amount for horizontal movement.")
            xspeed = input()
            if xspeed.isdigit():
                xspeed = int(xspeed)
                xvel = xspeed
                xspeedGot = True
            else:
                print(xspeed, "Isn't a valid awnser.")
        yspeedGot = False
        while not yspeedGot:
            print("Give me a p/f(pixels per frame) amount for vertical movement.")
            yspeed = input()
            if yspeed.isdigit():
                yspeed = int(yspeed)
                yvel = yspeed
                yspeedGot = True
            else:
                 print(yspeed, "Isn't a valid awnser.")
#exit
    elif question == ("exit"):
        exit()
#spos
    elif question == ("spos"):
        xSposSetup = True
        while xSposSetup:
            print("Give me an x coordinate to start from.")
            xpos = input()
            if xpos.isdigit():
                xpos = int(xpos)
                xSpos = xpos
                xSposSetup = False
            else:
                print('I need a valid number.')
        ySposSetup = True
        while ySposSetup:
            print("Give me an y coordinate to start from.")
            ypos = input()
            if ypos.isdigit():
                ypos = int(xpos)
                ySpos = xpos
                ySposSetup = False
            else:
                print('I need a valid number.')
#fps
    elif question == ("fps"):
        fpsSetup = True
        while fpsSetup:
            print("What is the refreshrate of your monitor?")
            tempFps = input()
            if tempFps.isdigit:
                tempFps = int(tempFps)
                fps = tempFps
#background
    elif question == ('background') or question == ('bg'):
        bgrSetup = True
        while bgrSetup:
            print('Give me a red value for the background')
            backgroundr = input()
            if backgroundr.isdigit():
                backgroundr = int(backgroundr)
                if backgroundr > (255):
                    print("I need a value under 256.")
                elif backgroundr < 0:
                    print("I need a value above -1")
                else:
                    bgr = backgroundr
                    bgrSetup = False
                    bgrandomr = False
            elif backgroundr == ('random'):
                bgrandomr = True
                bgrSetup = False
            else:
                print("I require a valid value")
        bgbSetup = True
        while bgbSetup:
            print('Give me a blue value for the background')
            backgroundb = input()
            if backgroundb.isdigit():
                backgroundb = int(backgroundb)
                if backgroundb > (255):
                    print("I need a value under 256.")
                elif backgroundb < 0:
                    print("I need a value above -1")
                else:
                    bgb = backgroundb
                    bgbSetup = False
                    bgrandomb = False
            elif backgroundb == ('random'):
                bgrandomb = True
                bgbSetup = False
            else:
                print("I require a valid value")
        bggSetup = True
        while bggSetup:
            print('Give me a green value for the background')
            backgroundg = input()
            if backgroundg.isdigit():
                backgroundg = int(backgroundg)
                if backgroundg > (255):
                    print("I need a value under 256.")
                elif backgroundg < 0:
                    print("I need a value above -1")
                else:
                    bgg = backgroundg
                    bggSetup = False
                    bgrandomg = False
            elif backgroundg == ('random'):
                bggandomg = True
                bggSetup = False
            else:
                print("I require a valid value")
#config
    elif question == ("config"):
        r = 255
        g = 0
        b = 0
        x2 = 1500
        y2 = 1000
        xSpos = 750
        ySpos = 500
        yvel = 20
        xvel = 15
        print('config executed')
#size
    elif question == ('size'):
        ysizeSetup = True
        while ysizeSetup:
            print("What should be the height of the cube?")
            height1 = input()
            if height1.isdigit:
                height1 = int(height1)
                ysize = height1
                ysizeSetup = False
            else:
                print("I require a valid value.")
        xsizeSetup = True
        while xsizeSetup:
            print("What should be the width of the cube?")
            width1 = input()
            if width1.isdigit:
                width1 = int(width1)
                xsize = width1
                xsizeSetup = False
            else:
                print("I require a valid value.")
if bgrandomr:
    bgr = random.randrange(256)
if bgrandomb:
    bgb = random.randrange(256)
if bgrandomg:
    bgg = random.randrange(256)
x = xSpos
y = ySpos
screensetup = (x2, y2)
screen = pygame.display.set_mode(screensetup)
screen.fill((bgr, bgb, bgg))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if randomcr:
        r = random.randrange(256)
    if randomcb:
        b = random.randrange(256)
    if randomcg:
        g = random.randrange(256)
    #draw shit
    pygame.draw.rect(screen, [r, g, b], [x, y, xsize, ysize], 0)
    #end draw shit
    #boink
    x = x + xvel
    y = y + yvel
    if x >= x2:
        xvel = xvel * (-1)
    elif x <= 0:
        xvel = xvel * (-1)
    elif y >= y2:
        yvel = yvel * (-1)
    elif y <= 0:
        yvel = yvel * (-1)
    pygame.display.flip()
    Clock.tick(fps)
pygame.quit
exit()
#list of vars
#setupvars
    #setupdone - setup loop
    #rcolorsetup - red colour setup
    #bcolorsetup - blue colour setup
    #gcolorsetup - green coulour setup
    #xsetup - x resolution setup 
    #ysetup - y resolution setup
    #xspeedGot - x speed setup
    #yspeedGot - y speed setup
    #xSposSetup - x start position setup
    #ySposSetup - y start position setup
    #fpsSetup - max fps setup
    #bgrSetup - red value of background setup
    #bgbSetup - blue value of background setup
    #bggSetup - green value of background setup
    #ysizeSetup - height setup
    #xsizeSetup - width setup
    #done - main loop
#tempvars
    #rcolor
    #bcolor
    #gcolor
    #ycolor
    #xcolor
    #xspeed
    #yspeed
    #xpos
    #ypos
    #tempFps
    #backgroundr
    #backgroundb
    #backgroundg
    #ysize
    #xsize
#randoms
    #randomcr
    #randomcb
    #randomcg
    #bgrandomr
    #bgrandomb
    #bgrandomg