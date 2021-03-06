#!/usr/bin/env python

#This is a simple game. 
#Copyright (C) 2016 Nathan Guerrero/PoniesFiM
"""This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>."""

#We have to print some copyright stuff.
print("RandomGame Copyright (C) 2016 Nathan Guerrero/PoniesFiM") #First line
print("This program comes with ABSOLUTELY NO WARRANTY; for details go to GPL.txt or README.txt") #Second line
print("This is free software, and you are welcome to redistribute it") #Third line
print("under certain conditions.") #Fourth line.
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n") #Separator.

#We need to import some of the things we need.
print("Importing things...")
import pygame, sys
import random
import os
import time
from pygame.locals import *
print("Imported...")

#We now need to initialize Pygame and do other things.
print("Initializing PyGame...")
pygame.mixer.pre_init(44100, -16, 2, 2048) #Before we initialize, we need to set up how the sounds will be played.
pygame.init() #We can now initialize Pygame and its modules.
pygame.mixer.set_num_channels(64) #Allow more sounds to play at once.
print("Initialized!")

#We now have to make a window where we put all the things we render.
print("Setting up the window...")
#Sets up the main window.
MAINWINDOW = pygame.display.set_mode((640,480)) #This makes a window that is 640 pixels by 480 pixels, basically 480p/i. 4:3 ratio.
print("Set up the window!")

#We now have to make a caption for the window. (The title basically)
print("Setting up a caption...")
pygame.display.set_caption("RandomGame 1.9") #This is the title of the window we use.
print("Set up the caption!")

#We have to fill in the window with black for the time the game loads.
MAINWINDOW.fill((0,0,0))
pygame.display.update() #This updates the screen.

#We now have to load the images for many of the objects in the game.
print("Now loading the main characters, the enemies, the particles, and other stuff.")

#The background images.
rust = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "rust.png"))
hijacked = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "hijacked.png"))
nuketown = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "nuketown.png"))

#The blurred background images. They show up when the game is paused.
rustblur = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "rustblurred.png"))
hijackedblur = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "hijackedblurred.png"))
nuketownblur = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "nuketownblurred.png"))

#The images.
mainSniper = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "sniper.png")) #Main character(you play this).

#Enemies.
otherSniper = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "sniper.png")) #The other sniper.
creeper = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "creeper.png")) #The creeper.

#Particles.
mlg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "mlg.jpg")) #A particle.
machinima = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "machinima.png")) #A particle.
hacker1 = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "hacker.png")) #A particle.
hacker2 = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "hacker2.png")) #A particle.

#Other stuff.
cursorImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "cursor.png")) #We use this as a our "cursor".
cursorClick = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "cursorclicked.png")) #We use this as a our "cursor" when clicked.
logo = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "poniesfimlogo.png")) #The logo of the main developer.
leaf = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "weed.png")) #The cannabis leaf for the 420 combo.
icon = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "icon.png")) #The icon for the game window.
print("Finished loading those things!")

#Set up the icon.
print("Setting up the icon...")
pygame.display.set_icon(icon) #Set the icon to the one we just loaded.
print("Set up the icon!")

#We have some sounds we need to get.
print("Loading the sounds...")

#The sounds
#Rage
kiddingMe = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "wombocombo1.ogg")) #A rage sound that plays when an enemy is killed.
comeOn = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "momgetthecamera1.ogg")) #A rage sound that plays when an enemy is killed.
what = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "ohmygod.ogg")) #A rage sound that plays when an enemy is killed.

#Extras.
endSound = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "end.ogg")) #The end sound when an enemy approaches you.
gunshot = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "50Cal.ogg")) #The sound the plays when you click the mouse(shoot a gun).
weed = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "weed.ogg")) #Extra sound that plays when kill.
tripleKill = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "triplekill.ogg"))  #Extra sound that plays when kill.
toasty = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "toasty.ogg")) #Extra sound that plays when kill.
damnSon = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds", "damnson.ogg")) #Combo sound that plays when score is divisible by 100.
print("Finished loading the sounds...")

#We now have some fonts to prepare.
print("Loading fonts...")
RegFont = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), "runescape_uf.ttf"), 40) #This loads the custom font at size 40, without bold, or italics.
print("Finished loading fonts...")

#We now have to set up statistics for the character, such as the position.
print("Setting up parameters for the main character...")
#Parameters for the main character.
characterX = 220 #This is the X(horizontal) position. We use this to move.
characterY = 300 #This is the Y(vertical) position. We generally don't need this to move. This is just the Y position.
print("Finished with that...")


#We now have to make colors with variables. Typing BLACK or WHITE is easier and simpler than typing (0, 0, 0) or (255, 255, 255).
print("Setting up the colors...")
#Sets up basic colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Sets up other/nicer colors. From Adobe Kuler. kuler.adobe.com
DARKISHBLUE = (14, 164, 178)
LIGHTERBLUE = (66, 238, 255)
BRIGHTBLUE = (40, 23, 255)
BROWN = (178, 75, 0)
ORANGE = (255, 130, 40)
print("Set up the colors!")

#We now do the initial draw of everything before the game loop.
print("Setting up shapes, backgrounds, and other things...")
#Shapes for the game.
#Fills the screen.
MAINWINDOW.fill(DARKISHBLUE) #We fill the window with this color.

#The actual shapes.
#We draw the shapes(terrain) here.
pygame.draw.rect(MAINWINDOW, GREEN, (0, 440, 640, 450)) #The grass.
pygame.draw.rect(MAINWINDOW, BROWN, (0, 450, 640, 480)) #The dirt.
print("Finished!")

print("Starting the game...")
directionToGoFirst = 1 #The enemies have to go one direction, and on different sides. So we use this.
pygame.display.update() #This updates the screen.

MAINWINDOW.blit(mainSniper, (characterX, characterY)) #We have to initially draw the main character on the screen.

#We have to initially set variables for the game loop. If this is done in the game loop, there would be many problems.
characterXLeft = False #This is the variable that represents the state of when the character is going left. 
leftSpeed = 0.0 #This is the variable that represents the speed of the character going left.
characterXRight = False #This is the variable that represents the state of when the character is going right.
rightSpeed = 0.0 #This is the variable that represents the speed of the character going right.

hitCreeper = False #This is the variable that represents the state of when the Creeper is shot.
hitCreeperTime = 30 #This is the variable that represents the time of when the particle appears. 1 equals one tick. The game refreshes 1000 times a second, so 1000 ticks should be equal to 1 second.

hitSniper = False #This is the variable that represents the state of when the Sniper is shot.
hitSniperTime = 8 #This is the variable that represents the time of when the particle appears. 1 equals one tick. The game refreshes 1000 times a second, so 1000 ticks should be equal to 1 second.

score = 0 #This is the variable that holds the score.
globalDirection = 90 #This is the variable that holds the direction of the particles.
otherKilled = False #Unknown purpose.
onePlay = False #This represents the state of the sound that gets played when the Creeper is hit. When the Creeper gets hit, this is set to true, so the sound will play. This variable is set to False after a sound plays to make sure that it plays once.
twoPlay = False #This represents the state of the sound that gets played when the enemy Sniper is hit. When the enemy Sniper gets hit, this is set to true, so the sound will play. This variable is set to False after a sound plays to make sure that it plays once.
rekt = False #This represents the state of when the enemy approaches the character.
rektColor = BLACK #This represents the color when the enemy approaches the character.
endPlayOne = True #This represents the state of when the end sound plays. If rekt = True, then the sounds will play and rekt will be set to False just to make sure the end sound plays one time.
waitTillEnd = 11000 #This is how much time the game has until exiting if the enemy approaches the main character. This variable lowers itself every refresh. The game refreshes 1000 times a second, so 4000 ticks = 4 seconds.
cClick = False #This represents the cursor state when clicked.
bgImage = random.randint(1,3) #This chooses what background image shows.
pauseTime = 0 #This is how much time the pause takes.
frameDebug = False #This is whether to show frame times.
prevScore = 0 #This is the previous score that the 100 combo has written down.
creeperShoot = 1500 #This is how many ticks time has to take after the creeper shot.
sniperShoot = 1500 #This is how many ticks time has to take after the creeper shot.
weedCombo = False #This is whether the 420 combo has been set off.
weedTicks = 2000 #This is how much time the cannabis leaf shows for the 420 combo.

#This initially draws the enemies.
if directionToGoFirst == 1:
    MAINWINDOW.blit(otherSniper, (-200, 300)) #This draws the enemy sniper on the left side of the screen.
    MAINWINDOW.blit(creeper, (640, 300)) #This draws the enemy creeper on the right side of the screen.
    otherX2 = 640 #This is the X position of the creeper.
    otherX1 = -200 #This is the X position of the enemy sniper.

#The game loop setup.
whiles = True
clock = pygame.time.Clock() #The clock for delta time.

#The actual game loop.
while whiles:
    #We find how much milliseconds the last frame has taken, so we can apply it to frame-dependent variables.
    currentFrameTime = clock.tick() - pauseTime
    pauseTime = 0
    
    pygame.mouse.set_visible(False) #This makes the cursor invisible, so we can use an image as a cursor.
    
    for event in pygame.event.get(): #looks for events.
        if event.type == QUIT: #This is what happens when someone wants to close the program.
            #We have to print some copyright stuff. Again.
            print("RandomGame Copyright (C) 2014 Nathan Guerrero/PoniesFiM") #First line
            print("This program comes with ABSOLUTELY NO WARRANTY; for details go to GPL.txt or README.txt") #Second line
            print("This is free software, and you are welcome to redistribute it") #Third line
            print("under certain conditions.") #Fourth line.
            print("\n")
            print("GitHub at https://github.com/OfficialPoniesFiM/RealRandomGame") #Refers people to the GitHub link.
            whiles = False
        
        if event.type == pygame.KEYDOWN: #Checks when someone is pressing a key.
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: #Checks when someone is pressing the A/left key.
                characterXLeft = True #This variable is set to True, so the main character can move to the left.
                #print("Character now at " + str(characterX) + ", " + str(characterY))
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #Checks when someone is pressing the D/right key.
                characterXRight = True #This variable is set to True, so the main character can move to the right.
                #print("Character now at " + str(characterX) + ", " + str(characterY))
            
            if event.key == pygame.K_ESCAPE:
                whiles = False #Marks the game to exit at the end of the loop when the escape key is hit.
            
            if event.key == pygame.K_f: #Checks when someone is pressing the F key.
                if frameDebug == False: #If frameDebug is False, change it to True.
                    frameDebug = True
                else: #If frameDebug is True, change it to False.
                    frameDebug = False
        
        if event.type == pygame.KEYUP: #Checks when someone stopped pressing the A/left key.
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: #Checks when someone stopped pressing the A/left key.
                characterXLeft = False #This variable gets set to false, so the character stops moving to the left/can move to the right.
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #Checks when someone stopped pressing the D/right key.
                characterXRight = False #This variable gets set to false, so the character stops moving to the right/can move to the left.

        if event.type == pygame.MOUSEBUTTONDOWN: #Checks when someone is clicking on the mouse.
            cClick = True #This variable gets set to True, so the cursor changes to indicate the click.

        if event.type == pygame.MOUSEBUTTONUP: #Checks when someone releases a click on the mouse.
            cClick = False #This variable gets set to False, so the cursor changes to indicate the release of the click.
    
    #We have to update the character parameters to move the thing at all properly.
    if directionToGoFirst == 1: #Mostly useless.
        if hitSniper == False: #This checks if the enemy Sniper isn't hit.
            otherX1 += .15 * currentFrameTime #The enemy sniper goes to the left by adding .15 * milliseconds from last frame to its X position. Only happens when not hit.
        
        if hitCreeper == False: #This checks if the Creeper isn't hit.
            otherX2 -= .15 * currentFrameTime #The Creeper goes to the right by removing .15 * milliseconds from last frame from its X position. Only happens when not hit.
    
    if characterXLeft == characterXRight: #If the player isn't pressing the left(or A), or right(or D) keys, or pressing both at the same time.
        filler = 0 #Nothing really happens. Just a filler variable set to make sure nothing wrong happens.
        
        if leftSpeed > 0: #If no one is moving, then slow down both sides.
            leftSpeed -= .025
        
        if rightSpeed > 0:
            rightSpeed -= .025
    
    elif characterXLeft == True: #If the character is moving left,
        characterX -= leftSpeed * currentFrameTime #.15 * currentFrameTime is removed from its X position to move left.
        if characterX > 440: #Makes sure sniper doesn't get out of the window.
            characterX = 440 #Sets the character X position to 440 if the X position is too much, to make sure the character doesn't get out of the window.
        
        elif characterX < 0: #Makes sure sniper doesn't get out of the window.
            characterX = 0 #Sets the character X position to 0 if the X position is too little, to make sure the character doesn't get out of the window.
        
        if leftSpeed < .50: #If you're going left, increase leftSpeed while slowing rightSpeed.
            leftSpeed += .025
        
        if rightSpeed > 0:
            rightSpeed -= .025
    
    elif characterXRight == True: #If the character is moving right,
        characterX += rightSpeed * currentFrameTime #.15 * milliseconds from last frame is added to its X position to move right.
        
        if characterX > 440: #Makes sure sniper doesn't get out of the window.
            characterX = 440 #Sets the character X position to 440 if the X position is too much, to make sure the character doesn't get out of the window.
        
        elif characterX < 0: #Makes sure sniper doesn't get out of the window.
            characterX = 0 #Sets the character X position to 0 if the X position is too little, to make sure the character doesn't get out of the window.
        
        if rightSpeed < .50: #If you're going left, increase rightSpeed while slowing leftSpeed.
            rightSpeed += .025
        
        if leftSpeed > 0:
            leftSpeed -= .025
    
    doneforever = 1 #This variable is used to make sure the mouse X and mouse Y get captured properly.
    for x in pygame.mouse.get_pos(): #pygame.mouse.get_pos() returns a tuple with the X and Y position, so we have to get each individual part properly.
        if doneforever == 1: #If the doneforever variable is 1,
            mouseX = int(x) #Store the X position in a variable.
            doneforever = 2 #And set the doneforever variable to 2, so the program knows to store the Y position in another variable.
        
        elif doneforever == 2: #If the doneforever variable is 2,
            mouseY = int(x) #store the Y position in a variable.
    globalDirection += 1 * currentFrameTime #This sets the direction of the particles.
    rmlg = pygame.transform.rotate(mlg, globalDirection) #The rotated version of this particle is stored in another "variable".
    rmachinima = pygame.transform.rotate(machinima, globalDirection) #The rotated version of this particle is stored in another "variable".
    rhacker1 = pygame.transform.rotate(hacker1, globalDirection) #The rotated version of this particle is stored in another "variable".
    rhacker2 = pygame.transform.rotate(hacker2, globalDirection) #The rotated version of this particle is stored in another "variable".
    
    if pygame.mouse.get_pressed() == (False, False, True): #If the right mouse button is clicked, and the others aren't,
        if creeperShoot == 1500: #If the time is on,
            gunshot.play() #Play a gunshot sound.
            creeperShoot -= currentFrameTime #Remove the current frame time from creeperShoot.
        if directionToGoFirst == 1 and otherX2 < 540: #If the Creeper is in the right position,
            onePlay = True #Set the onePlay variable to True, to make the sound play.
            hitCreeper = True #Set the hitCreeper variable to true.
            hitCreeperX = otherX2 #Set the hitCreeperX variable to the current X position, so the particles know where to render.
            otherX2 = 640 #Move back to the right. Out of the window.
            score += 1 #Score gets higher.
    
    elif pygame.mouse.get_pressed() == (True, False, False): #If the left mouse button is clicked, and the others aren't,
        if sniperShoot == 1500: #If the time is on,
            gunshot.play() #Play a gunshot sound.
            sniperShoot -= currentFrameTime #Remove the current frame time from sniperShoot.
        if directionToGoFirst == 1 and otherX1 > -100: #If the enemy sniper is in the right position,
            twoPlay = True #Set the twoPlay variable to True, to have the sound play.
            hitSniper = True #Set the hitSniper variable to true.
            hitSniperX = otherX1 #Set the hitSniperX variable to the current X position, so the particles know where to render.
            otherX1 = -200 #Go back to the left. Out of the window.
            score += 1 #Score gets higher.
    
    if creeperShoot < 1500 and creeperShoot > 0: #If creeperShoot is less than 1500 ticks and greater than 0 ticks,
        creeperShoot -= currentFrameTime #Remove current frame time from creeperShoot.
    elif creeperShoot <= 0: #If the time runs out,
        creeperShoot = 1500 #Reset creeperShoot to 1500.

    if sniperShoot < 1500 and sniperShoot > 0: #If sniperShoot is less than 1500 ticks and greater than 0 ticks,
        sniperShoot -= currentFrameTime #Remove current frame time from sniperShoot.
    elif creeperShoot <= 0: #If the time runs out,
        sniperShoot = 1500 #Reset sniperShoot to 1500.
    
    if hitCreeper == True: #If the creeper gets hit,
        hitCreeperTime -= 1 #Makes game remove ticks until goes to 0.
        if hitCreeperTime == 0: #If we ran out of time,
            hitCreeper = False #Set it to False for other things, such as to move.
            hitCreeperTime = 120 #Time gets reset to 60 ticks/1 second.
    
    else:
        if otherKilled == False: #If otherKilled(unknown purpose) is False, set hitCreeperTime to 60.
            hitCreeperTime = 120
        particle = random.randint(1,4) #Sets what particle to use/render.
    
    if hitSniper == True: #If the sniper got hit,
        hitSniperTime -= 1 #Remove 1 tick from this variable until time runs out. Time is used to render particles.
        if hitSniperTime == 0: #If time runs out(at 0),
            hitSniper = False #Set hitSniper to False, to let the enemy sniper move, and to stop rendering the particle.
            hitSniperTime = 120 #Reset the time for later.
            otherKilled = False #Unknown purpose.
    else:
        hitSniperTime = 120 #Reset the time to 60 ticks/1 second to make sure time goes correctly.
        otherKilled = False #Unknown purpose.
    
    if onePlay == True: #When the game wants to play a sound because of a Creeper being hit,
        current1play = random.randint(1,3) #Get a random number.
        current1play2 = random.randint(1,4) #Get another random number.
        
        if current1play == 1: #If the number is 1,
            kiddingMe.play() #Play this sound.
        elif current1play == 2: #If the number is 2,
            comeOn.play() #Play this sound.
        elif current1play == 3: #If the number is 3,
            what.play() #Play this sound.
        
        if current1play2 == 1:
            filler = 0 #Unknown purpose.
        elif current1play2 == 2:
            weed.play() #Play this sound.
        elif current1play2 == 3:
            tripleKill.play() #Play this sound.
        elif current1play2 == 4:
            toasty.play() #Play this sound.
        
        onePlay = False #Set this variable to false to make sure sounds don't play again until Creeper gets hit again.
    
    if twoPlay == True: #When the game wants to play a sound because of an enemy Sniper being hit,
        current2play = random.randint(1,3) #Get a random number.
        current2play2 = random.randint(1,4) #Get another random number.
        if current2play == 1: #If the number is 1,
            kiddingMe.play() #Play this sound.
        elif current2play == 2: #If the number is 2,
            comeOn.play() #Play this sound.
        elif current2play == 3: #If the number is 3,
            what.play() #Play this sound.
        
        if current2play2 == 1:
            filler = 0 #Unknown purpose.
        elif current2play2 == 2:
            weed.play() #Play this sound.
        elif current2play2 == 3:
            tripleKill.play() #Play this sound.
        elif current2play2 == 4:
            toasty.play() #Play this sound.
        
        twoPlay = False #Set this variable to false to make sure sounds don't play again until enemy Sniper gets hit again.
    if characterX > otherX2 - 125: #If the Creeper approaches the character,
        rekt = True #set rekt to true, to make the game know that it has to do things.
    elif characterX < otherX1 + 185: #If the enemy Sniper approaches the character,
        rekt = True #set rekt to true, to make the game know that it has to do things.

    if (score % 100) == 0 and prevScore != score: #If the score is divisible by 100, and the score isn't the same as before,
        damnSon.play() #Play the damn son sound.
        prevScore = score #Change the previous score to the score the game had when divisible by 100.

    if score == 420 and weedCombo == False: #If the score is 420, and the combo hasn't been set off yet,
        weedCombo = True #Set the weedCombo to True so this doesn't trigger again.
        weed.play() #Play the smoke weed sound.
        weedTicks -= currentFrameTime #Remove currentFrameTime from weedTicks to trigger the timer.
    elif weedTicks < 2000 and weedTicks > 0: #If weedTicks is more than 0 and less than 2000,
        weedTicks -= currentFrameTime #Remove currentFrameTime from weedTicks.
    
    #Due to issues with the sniper, we have to redraw the thing every refresh.
    #The background
    if bgImage == 1:
        MAINWINDOW.blit(rust, (0, 0)) #We draw rust if bgImage = 1.
    elif bgImage == 2:
        MAINWINDOW.blit(hijacked, (0, 0)) #We draw hijacked if bgImage = 2.
    elif bgImage == 3:
        MAINWINDOW.blit(nuketown, (0, 0)) #We draw nuketown if bgImage = 3.
    
    #Draw the cannabis leaf
    if weedTicks < 2000 and weedTicks > 0: #If weedTicks is less than 2000, and more than 0,
        MAINWINDOW.blit(leaf, (110, 32)) #Draw the cannabis leaf at the center of the screen.
    
    #The ground(terrain)
    pygame.draw.rect(MAINWINDOW, GREEN, (0, 440, 640, 450)) #We draw the grass(a green rectangle,
    pygame.draw.rect(MAINWINDOW, BROWN, (0, 450, 640, 480)) #and then the dirt(a brown rectangle).
    
    #Main character
    MAINWINDOW.blit(mainSniper, (characterX, characterY)) #We now draw the main character at its positions.
    
    #Enemies
    MAINWINDOW.blit(otherSniper, (otherX1, 300)) #We draw the enemy sniper at its positions.
    MAINWINDOW.blit(creeper, (otherX2, 250)) #We draw the creeper at its positions.
    
    #Particles. (Only rendered if Creeper or Sniper gets hit.)
    if hitCreeper == True: #If the Creeper got hit, 
        if particle == 1: #If the random number was 1, 
            MAINWINDOW.blit(rmlg, (hitCreeperX, 350)) #We draw the MLG logo.
        elif particle == 2: #If the random number was 2,
            MAINWINDOW.blit(rmachinima, (hitCreeperX, 350)) #We draw the Machinima logo.
        elif particle == 3: #If the random number was 3,
            MAINWINDOW.blit(rhacker1, (hitCreeperX, 350)) #We draw a version of the text, "U HACKER".
        elif particle == 4: #If the random number was 4, 
            MAINWINDOW.blit(rhacker2, (hitCreeperX, 350)) #We draw another version of the text, "U HACKER".
    
    if hitSniper == True: #If the enemy sniper got hit,
        if particle == 1: #If the random number was 1, 
            MAINWINDOW.blit(rmlg, (hitSniperX, 300)) #We draw the MLG logo.
        elif particle == 2: #If the random number was 2, 
            MAINWINDOW.blit(rmachinima, (hitSniperX, 300)) #We draw the Macinima logo.
        elif particle == 3:#If the random number was 3, 
            MAINWINDOW.blit(rhacker1, (hitSniperX, 300)) #We draw a version of the text, "U HACKER".
        elif particle == 4: #If the random number was 4, 
            MAINWINDOW.blit(rhacker2, (hitSniperX, 300)) #We draw another version of the text, "U HACKER".

    playerName = RegFont.render("Player", 1, YELLOW) #Define playerName to display on top of the main character
    MAINWINDOW.blit(playerName, (characterX + 10, 260)) #Draw "Player" on top of the character.
    
    scoretext = "Score: " + str(score) #Define what the text for the score is.
    textscore = RegFont.render(scoretext, 1, YELLOW) #Define the actual text to draw.
    if (score % 100) == 0 and score != 0: #If score is divisible by 100,
        scoretext = "Score: " + str(score) + " (DAMN SON!)" #Define what the text for the score is, along with (damn son!).
        textscore = RegFont.render(scoretext, 1, BLACK) #Define the actual text to draw as black.
    elif score == 420: #If score is 420,
        scoretext = "Score: " + str(score) + " BLAZE IT" #Define what the text for the score is, along with BLAZE IT.
        textscore = RegFont.render(scoretext, 1, GREEN) #Define the actual text to draw as black.
    MAINWINDOW.blit(textscore, (5, 0)) #Draw the text on the screen.

    if frameDebug == True: #If frameDebug is True,
        frameText = "Frame Time: " + str(currentFrameTime) + " ms" #Define the text frameText, with Frame Time: (frame time) ms.
        frameTextRender = RegFont.render(frameText, 1, YELLOW) #Define the actual text to draw.
        MAINWINDOW.blit(frameTextRender, (5, 445)) #Draw the frame time on the screen.
    
    if rekt == True: #If an enemy approached the character,
        if endPlayOne == True: #If we haven't play the sound yet.
            endSound.play() #Play the end sound.
            endPlayOne = False #Set the variable to false to make sure the sound doesn't play multiple times/sound peculiar.
        
        if rektColor == BLACK: #If the color is black,
            endRekt = RegFont.render("#REKT", 1, BLACK) #Define the text, "#REKT", as black.
            rektColor = WHITE #Change the color to white.
        elif rektColor == WHITE: #If the color is white,
            endRekt = RegFont.render("#REKT", 1, WHITE) #Define the text, "#REKT", as white.
            rektColor = RED #Change the color to red.
        elif rektColor == RED: #If the color is red,
            endRekt = RegFont.render("#REKT", 1, RED) #Define the text, "#REKT", as red.
            rektColor = GREEN #Change the color to green.
        elif rektColor == GREEN: #If the color is green,
            endRekt = RegFont.render("#REKT", 1, GREEN) #Define the text, "#REKT", as green.
            rektColor = BLUE #Change the color to blue.
        elif rektColor == BLUE: #If the color is blue,
            endRekt = RegFont.render("#REKT", 1, BLUE) #Define the text, "#REKT", as blue.
            rektColor = YELLOW #Change the color to yellow.
        elif rektColor == YELLOW: #If the color is yellow,
            endRekt = RegFont.render("#REKT", 1, YELLOW) #Define the text, "#REKT", as yellow.
            rektColor = BLACK #Change the color to black again.
            
        MAINWINDOW.blit(endRekt, (280 + random.randint(-5, 5), 240 + random.randint(-5,5))) #Render the text.
        waitTillEnd -= 1 * (currentFrameTime) #Remove 1 tick from the variable until we run out. This is useful for the sound and other things.
        if waitTillEnd <= 0: #If we run out,
            #We have to print some copyright stuff. Again.
            print("RandomGame Copyright (C) 2016 Nathan Guerrero/PoniesFiM") #First line
            print("This program comes with ABSOLUTELY NO WARRANTY; for details go to GPL.txt or README.txt") #Second line
            print("This is free software, and you are welcome to redistribute it") #Third line
            print("under certain conditions.") #Fourth line.
            print("\n")
            print("GitHub at https://github.com/OfficialPoniesFiM/RealRandomGame") #Refers people to the GitHub link.
            
            whiles = False
    
    #Cursor/Scores/similar
    MAINWINDOW.blit(logo, (540, 380)) #Draw the logo of the main developer.
    if cClick == False:
        MAINWINDOW.blit(cursorImage, (mouseX - 8, mouseY - 8)) #Draw the "cursor" at the mouse position.
    else:
        MAINWINDOW.blit(cursorClick, (mouseX - 8, mouseY - 8)) #Draw the "cursor" at the mouse position when clicked.
    
    pygame.mixer.unpause() #It ensures the audio keeps playing when not paused.
    
    #The game updates.
    pygame.display.update()

    if pygame.mouse.get_focused() == False: #If the mouse does not hover over the window,
        #Blit the blurred image.
        if bgImage == 1:
            MAINWINDOW.blit(rustblur, (0, 0)) #We draw rust with blur if bgImage = 1.
        elif bgImage == 2:
            MAINWINDOW.blit(hijackedblur, (0, 0)) #We draw hijacked with blur if bgImage = 2.
        elif bgImage == 3:
            MAINWINDOW.blit(nuketownblur, (0, 0)) #We draw nuketown with blur if bgImage = 3.
        
        pauseText = RegFont.render("Paused", 1, BLACK) #Define the text, "pauseText"
        MAINWINDOW.blit(pauseText, (255, 220)) #Render pauseText to indicate the game has been paused.
        pygame.display.update() #Update the window once to finish the frame and indicate the game has been paused.
    
    while pygame.mouse.get_focused() == False: #If the mouse does not hover over the window,
        for event in pygame.event.get(): #It will check for events to stop the game from not responding and for quitting.
            if event.type == pygame.QUIT: #If the game gets exited while paused, it immediately quits and exits.
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Checks if the escape key gets hit. If it does, the game exits.
                    pygame.quit()
                    sys.exit()
        
        pygame.mixer.pause() #It pauses the audio.
        time.sleep(.1) #It also waits .1 second until the loop runs again. This is to save CPU cycles.
        pauseTime += 100

pygame.quit() # Pygame quits.
sys.exit() # Sys exits.
