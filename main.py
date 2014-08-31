#!/usr/bin/env python

#This is a simple game. 
#Copyright (C) 2014 Nathan Guerrero/PoniesFiM
"""This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>."""

#We have to print some copyright stuff.
print("RandomGame Copyright (C) 2014 Nathan Guerrero/PoniesFiM") #First line
print("This program comes with ABSOLUTELY NO WARRANTY; for details go to GPL.txt or README.txt") #Second line
print("This is free software, and you are welcome to redistribute it") #Third line
print("under certain conditions.") #Fourth line.
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n") #Separator.

#We need to import some of the things we need.
print("Importing things...")
import pygame, sys
import random
from pygame.locals import *
print("Imported...")

print("Creating save file...")
randomCode = [] #All the code for the name of the save that is generated will be appended here.
randomNumber = 0 #This is the random number.
randomStuff = "" #This is the random character.
isCapital = 0 #This variable represents the state of if a character is a capital.
for everything in "1 2 3 4 5 6 7 8 9 10".split(): #For everything in 1-10,
    randomNumber = random.randint(0, 35) #Generate a random number.
    
    if randomNumber == 0: #If the random number is 0,
        randomStuff = str(0) #The random character is 0 as a string.
    elif randomNumber == 1: #If the random number is 1,
        randomStuff = str(1) #The random character is 1 as a string.
    elif randomNumber == 2: #If the random number is 2,
        randomStuff = str(2) #The random character is 2 as a string.
    elif randomNumber == 3: #If the random number is 3,
        randomStuff = str(3) #The random character is 3 as a string.
    elif randomNumber == 4: #If the random number is 4,
        randomStuff = str(4) #The random character is 4 as a string.
    elif randomNumber == 5: #If the random number is 5,
        randomStuff = str(5) #The random character is 5 as a string.
    elif randomNumber == 6: #If the random number is 6,
        randomStuff = str(6) #The random character is 6 as a string.
    elif randomNumber == 7: #If the random number is 7,
        randomStuff = str(7) #The random character is 7 as a string.
    elif randomNumber == 8: #If the random number is 8,
        randomStuff = str(8) #The random character is 8 as a string.
    elif randomNumber == 9: #If the random number is 9,
        randomStuff = str(9) #The random character is 9 as a string.
    elif randomNumber == 10: #If the random number is 10,
        randomStuff = "a" #The random character is "a".
    elif randomNumber == 11: #If the random number is 11,
        randomStuff = "b" #The random character is "b".
    elif randomNumber == 12: #If the random number is 12,
        randomStuff = "c" #The random character is "c".
    elif randomNumber == 13: #If the random number is 13,
        randomStuff = "d" #The random character is "d".
    elif randomNumber == 14: #If the random number is 14,
        randomStuff = "e" #The random character is "e".
    elif randomNumber == 15: #If the random number is 15,
        randomStuff = "f" #The random character is "f".
    elif randomNumber == 16: #If the random number is 16,
        randomStuff = "g" #The random character is "g".
    elif randomNumber == 17: #If the random number is 17,
        randomStuff = "h" #The random character is "h".
    elif randomNumber == 18: #If the random number is 18,
        randomStuff = "i" #The random character is "i".
    elif randomNumber == 19: #If the random number is 19,
        randomStuff = "j" #The random character is "j".
    elif randomNumber == 20: #If the random number is 20,
        randomStuff = "k" #The random character is "k".
    elif randomNumber == 21: #If the random number is 21,
        randomStuff = "l" #The random character is "l".
    elif randomNumber == 22: #If the random number is 22,
        randomStuff = "m" #The random character is "m".
    elif randomNumber == 23: #If the random number is 23,
        randomStuff = "n" #The random character is "n".
    elif randomNumber == 24: #If the random number is 24,
        randomStuff = "o" #The random character is "o".
    elif randomNumber == 25: #If the random number is 25,
        randomStuff = "p" #The random character is "p".
    elif randomNumber == 26: #If the random number is 26,
        randomStuff = "q" #The random character is "q".
    elif randomNumber == 27: #If the random number is 27,
        randomStuff = "r" #The random character is "r".
    elif randomNumber == 28: #If the random number is 28,
        randomStuff = "s" #The random character is "s".
    elif randomNumber == 29: #If the random number is 29,
        randomStuff = "t" #The random character is "t".
    elif randomNumber == 30: #If the random number is 30,
        randomStuff = "u" #The random character is "u".
    elif randomNumber == 31: #If the random number is 31,
        randomStuff = "v" #The random character is "v".
    elif randomNumber == 32: #If the random number is 32,
        randomStuff = "w" #The random character is "w".
    elif randomNumber == 33: #If the random number is 33,
        randomStuff = "x" #The random character is "z".
    elif randomNumber == 34: #If the random number is 34,
        randomStuff = "y" #The random character is "y".
    elif randomNumber == 35: #If the random number is 35,
        randomStuff = "z" #The random character is "z".
    isCapital = random.randint(0,1) #The program creates a random number that represents the state of if a letter is a capital and stores it in a variable called "isCapital".
            
    if str(randomNumber) in "10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35".split() and isCapital == 1: #If the random number is 10-35(which means the character is a letter, and not another type of character), and the random number that represents the state of when a letter is capital is 1,
        randomStuff = randomStuff.upper() #Make the current random character uppercase.
        randomCode.append(randomStuff) #Append the character to a list.
newOldSaveTrue = False
newCode = "" #Another variable.
newCode = newCode.join(randomCode) #Add everything in the list of characters to this variable, newCode.
print(newCode)
saveFileName = "Saves\\" + newCode + ".txt"
saveFile = open(saveFileName, "w")

#We need to set up how many times per second Pygame will update, and how we will tick it.
print("Setting FPS up...")
FPS = 60 #The number of how many times Pygame will refresh each second.
fpsClock = pygame.time.Clock() #The way we will delay things.
print("Set up!")

#We now need to initialize Pygame and do other things.
print("Initializing PyGame...")
pygame.mixer.pre_init(44100, -16, 2, 2048) #Before we initialize, we need to set up how the sounds will be played.
pygame.init() #We can now initialize Pygame and its modules.
print("Initialized!")

#We now have to load the images for many of the objects in the game.
print("Now loading the main characters, the enemies, the particles, and other stuff.")
#The images.
mainSniper = pygame.image.load("Pictures\\sniper.png") #Main character(you play this).

#Enemies.
otherSniper = pygame.image.load("Pictures\\sniper.png") #The other sniper.
creeper = pygame.image.load("Pictures\\creeper.png") #The creeper.

#Particles.
mlg = pygame.image.load("Pictures\\mlg.jpg") #A particle.
machinima = pygame.image.load("Pictures\\machinima.png") #A particle.
hacker1 = pygame.image.load("Pictures\\hacker.png") #A particle.
hacker2 = pygame.image.load("Pictures\\hacker2.png") #A particle.

#Other stuff.
cursorImage = pygame.image.load("Pictures\\cursor.png") #We use this as a our "cursor".
logo = pygame.image.load("Pictures\\poniesfimlogo.png") #The logo of the main developer.
print("Finished loading those things!")

#We have some sounds we need to get.
print("Loading the sounds...")
#The sounds
#Rage
kiddingMe = pygame.mixer.Sound('Sounds\\wombocombo1.ogg') #A rage sound that plays when an enemy is killed.
comeOn = pygame.mixer.Sound('Sounds\\momgetthecamera1.ogg') #A rage sound that plays when an enemy is killed.
what = pygame.mixer.Sound('Sounds\\ohmygod.ogg') #A rage sound that plays when an enemy is killed.

#Extras.
endSound = pygame.mixer.Sound('Sounds\\end.ogg') #The end sound when an enemy approaches you.
gunshot = pygame.mixer.Sound('Sounds\\50Cal.wav') #The sound the plays when you click the mouse(shoot a gun).
weed = pygame.mixer.Sound("Sounds\\weed.ogg") #Extra sound that plays when kill.
tripleKill = pygame.mixer.Sound("Sounds\\triplekill.ogg")  #Extra sound that plays when kill.
toasty = pygame.mixer.Sound("Sounds\\toasty.ogg") #Extra sound that plays when kill.
print("Finished loading the sounds...")

#We now have some fonts to prepare.
print("Loading fonts...")
RegFont = pygame.font.SysFont("Arial", 40, False, False) #This loads Arial at size 40, without bold, or italics.
print("Finished loading fonts...")

#We now have to set up statistics for the character, such as the position.
print("Setting up parameters for the main character...")
#Parameters for the main character.
characterX = 320 #This is the X(horizontal) position. We use this to move.
characterY = 300 #This is the Y(vertical) position. We generally don't need this to move. This is just the Y position.
print("Finished with that...")

#We now have to make a window where we put all the things we render.
print("Setting up the window...")
#Sets up the main window.
MAINWINDOW = pygame.display.set_mode((640,480)) #This makes a window that is 640 pixels by 480 pixels, basically 480p/i. 4:3 ratio.
print("Set up the window!")

#We now have to make a caption for the window. (The title basically)
print("Setting up a caption...")
pygame.display.set_caption("RandomGame 1.0 - Main Window") #This is the title of the window we use.
print("Set up the caption!")

#We now have to make colors with variables. Typing BLACK or WHITE is easier and simpler than typing (0, 0, 0) or (255, 255, 255).
print("Setting up the colors...")
#Sets up basic colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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
characterXRight = False #This is the variable that represents the state of when the character is going right.
hitCreeper = False #This is the variable that represents the state of when the Creeper is shot.
hitCreeperTime = 480 #This is the variable that represents the time of when the particle appears. 1 equals one tick. The game refreshes 60 times a second, so 60 ticks should be equal to 1 second.
hitSniper = False #This is the variable that represents the state of when the Sniper is shot.
hitSniperTime = 120 #This is the variable that represents the time of when the particle appears. 1 equals one tick. The game refreshes 60 times a second, so 60 ticks should be equal to 1 second.
score = 0 #This is the variable that holds the score.
globalDirection = 90 #This is the variable that holds the direction of the particles.
otherKilled = False #Unknown purpose.
onePlay = False #This represents the state of the sound that gets played when the Creeper is hit. When the Creeper gets hit, this is set to true, so the sound will play. This variable is set to False after a sound plays to make sure that it plays once.
twoPlay = False #This represents the state of the sound that gets played when the enemy Sniper is hit. When the enemy Sniper gets hit, this is set to true, so the sound will play. This variable is set to False after a sound plays to make sure that it plays once.
rekt = False #This represents the state of when the enemy approaches the character.
endPlayOne = True #This represents the state of when the end sound plays. If rekt = True, then the sounds will play and rekt will be set to False just to make sure the end sound plays one time.
waitTillEnd = 480 #This is how much time the game has until exiting if the enemy approaches the main character. This variable lowers itself every refresh. The game refreshes 60 times a second, so 480 ticks = 4 seconds.

#This initially draws the enemies.
if directionToGoFirst == 1:
    MAINWINDOW.blit(otherSniper, (-200, 300)) #This draws the enemy sniper on the left side of the screen.
    MAINWINDOW.blit(creeper, (640, 300)) #This draws the enemy creeper on the right side of the screen.
    otherX2 = 640 #This is the X position of the creeper.
    otherX1 = -200 #This is the X position of the enemy sniper.
saveFile.close() #Closes the save file.
#The game loop.
whiles = True
while whiles:
    saveFile = open(saveFileName, "w")
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
                print("Character now at " + str(characterX) + ", " + str(characterY))
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #Checks when someone is pressing the D/right key.
                characterXRight = True #This variable is set to True, so the main character can move to the right.
                print("Character now at " + str(characterX) + ", " + str(characterY))
        
        if event.type == pygame.KEYUP: #Checks when someone stopped pressing the A/left key.
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: #Checks when someone stopped pressing the A/left key.
                characterXLeft = False #This variable gets set to false, so the character stops moving to the left/can move to the right.
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #Checks when someone stopped pressing the D/right key.
                characterXRight = False #This variable gets set to false, so the character stops moving to the right/can move to the left.
    
    #We have to update the character parameters to move the thing at all properly.
    if directionToGoFirst == 1: #Mostly useless.
        if hitSniper == False: #This checks if the enemy Sniper isn't hit.
            otherX1 += 2.5 #The enemy sniper goes to the left by adding 2.5 to its X position. Only happens when not hit.
        
        if hitCreeper == False: #This checks if the Creeper isn't hit.
            otherX2 -= 2.5 #The Creeper goes to the right by removing 2.5 from its X position. Only happens when not hit.
    
    if characterXLeft == characterXRight: #If the player isn't pressing the left(or A), or right(or D) keys, or pressing both at the same time.
        filler = 0 #Nothing really happens. Just a filler variable set to make sure nothing wrong happens.
    
    elif characterXLeft == True: #If the character is moving left,
        characterX -= 2.5 #2.5 is removed from its X position to move left.
        if characterX > 440: #Makes sure sniper doesn't get out of the window.
            characterX = 440 #Sets the character X position to 440 if the X position is too much, to make sure the character doesn't get out of the window.
        
        elif characterX < 0: #Makes sure sniper doesn't get out of the window.
            characterX = 0 #Sets the character X position to 0 if the X position is too little, to make sure the character doesn't get out of the window.
    
    elif characterXRight == True: #If the character is moving right,
        characterX += 2.5 #2.5 is added to its X position to move right.
        
        if characterX > 440: #Makes sure sniper doesn't get out of the window.
            characterX = 440 #Sets the character X position to 440 if the X position is too much, to make sure the character doesn't get out of the window.
        
        elif characterX < 0: #Makes sure sniper doesn't get out of the window.
            characterX = 0 #Sets the character X position to 0 if the X position is too little, to make sure the character doesn't get out of the window.
    
    doneforever = 1 #This variable is used to make sure the mouse X and mouse Y get captured properly.
    for x in pygame.mouse.get_pos(): #pygame.mouse.get_pos() returns a tuple with the X and Y position, so we have to get each individual part properly.
        if doneforever == 1: #If the doneforever variable is 1,
            mouseX = int(x) #Store the X position in a variable.
            doneforever = 2 #And set the doneforever variable to 2, so the program knows to store the Y position in another variable.
        
        elif doneforever == 2: #If the doneforever variable is 2,
            mouseY = int(x) #store the Y position in a variable.
    saveFile.write("Mouse Position: " + str(mouseX) + ", " + str(mouseY) + "\n")
    globalDirection += 5 #This sets the direction of the particles.
    saveFile.write("Particle Direction: " + str(globalDirection) + "\n")
    rmlg = pygame.transform.rotate(mlg, globalDirection) #The rotated version of this particle is stored in another "variable".
    rmachinima = pygame.transform.rotate(machinima, globalDirection) #The rotated version of this particle is stored in another "variable".
    rhacker1 = pygame.transform.rotate(hacker1, globalDirection) #The rotated version of this particle is stored in another "variable".
    rhacker2 = pygame.transform.rotate(hacker2, globalDirection) #The rotated version of this particle is stored in another "variable".
    
    saveFile.write("Mouse Click Areas: " + str(pygame.mouse.get_pressed()) + "\n")
    
    if pygame.mouse.get_pressed() == (False, False, True): #If the right mouse button is clicked, and the others aren't,
        gunshot.play() #Play a laser gun sound.
        if directionToGoFirst == 1 and otherX2 < 540: #If the Creeper is in the right position,
            onePlay = True #Set the onePlay variable to True, to make the sound play.
            hitCreeper = True #Set the hitCreeper variable to true.
            hitCreeperX = otherX2 #Set the hitCreeperX variable to the current X position, so the particles know where to render.
            otherX2 = 640 #Move back to the right. Out of the window.
            score += 1 #Score gets higher.
    
    elif pygame.mouse.get_pressed() == (True, False, False): #If the left mouse button is clicked, and the others aren't,
        gunshot.play() #Play a laser gun sound.
        if directionToGoFirst == 1 and otherX1 > -100: #If the enemy sniper is in the right position,
            twoPlay = True #Set the twoPlay variable to True, to have the sound play.
            hitSniper = True #Set the hitSniper variable to true.
            hitSniperX = otherX1 #Set the hitSniperX variable to the current X position, so the particles know where to render.
            otherX1 = -200 #Go back to the left. Out of the window.
            score += 1 #Score gets higher.
    
    if hitCreeper == True: #If the creeper gets hit,
        hitCreeperTime -= 1 #Makes game remove ticks until goes to 0.
        if hitCreeperTime == 0: #If we ran out of time,
            hitCreeper = False #Set it to False for other things, such as to move.
            hitCreeperTime = 120 #Time gets reset to 60 ticks/1 second.
    
    else:
        if otherKilled == False: #If otherKilled(unknown purpose) is False, set hitCreeperTime to 60.
            hitCreeperTime = 120
        particle = random.randint(1,4) #Sets what particle to use/render.
    
    saveFile.write("Creeper State: " + str(hitCreeper) + "\n")
    
    if hitSniper == True: #If the sniper got hit,
        hitSniperTime -= 1 #Remove 1 tick from this variable until time runs out. Time is used to render particles.
        if hitSniperTime == 0: #If time runs out(at 0),
            hitSniper = False #Set hitSniper to False, to let the enemy sniper move, and to stop rendering the particle.
            hitSniperTime = 120 #Reset the time for later.
            otherKilled = False #Unknown purpose.
    else:
        hitSniperTime = 120 #Reset the time to 60 ticks/1 second to make sure time goes correctly.
        otherKilled = False #Unknown purpose.
    
    saveFile.write("Sniper State: " + str(hitSniper) + "\n")
    
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
    if characterX > otherX2: #If the Creeper approaches the character,
        rekt = True #set rekt to true, to make the game know that it has to do things.
    elif characterX < otherX1: #If the enemy Sniper approaches the character,
        rekt = True #set rekt to true, to make the game know that it has to do things.
    #Due to issues with the sniper, we have to redraw the thing every refresh.
    #The background
    MAINWINDOW.fill(DARKISHBLUE) #We fill the window with this color.
    
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
            saveFile.write("Creeper Particles: MLG Logo\n")
        elif particle == 2: #If the random number was 2,
            MAINWINDOW.blit(rmachinima, (hitCreeperX, 350)) #We draw the Machinima logo.
            saveFile.write("Creeper Particles: Machinima Logo\n")
        elif particle == 3: #If the random number was 3,
            MAINWINDOW.blit(rhacker1, (hitCreeperX, 350)) #We draw a version of the text, "U HACKER".
            saveFile.write("Creeper Particles: \"U HACKER\"(Black)\n")
        elif particle == 4: #If the random number was 4, 
            MAINWINDOW.blit(rhacker2, (hitCreeperX, 350)) #We draw another version of the text, "U HACKER".
            saveFile.write("Creeper Particles: \"U HACKER\"(Colored)\n")
    
    if hitSniper == True: #If the enemy sniper got hit,
        if particle == 1: #If the random number was 1, 
            MAINWINDOW.blit(rmlg, (hitSniperX, 300)) #We draw the MLG logo.
            saveFile.write("Sniper Particles: MLG Logo\n")
        elif particle == 2: #If the random number was 2, 
            MAINWINDOW.blit(rmachinima, (hitSniperX, 300)) #We draw the Macinima logo.
            saveFile.write("Sniper Particles: Machinima Logo\n")
        elif particle == 3:#If the random number was 3, 
            MAINWINDOW.blit(rhacker1, (hitSniperX, 300)) #We draw a version of the text, "U HACKER".
            saveFile.write("Sniper Particles: \"U HACKER\"(Black)\n")
        elif particle == 4: #If the random number was 4, 
            MAINWINDOW.blit(rhacker2, (hitSniperX, 300)) #We draw another version of the text, "U HACKER".
            saveFile.write("Sniper Particles: \"U HACKER\"(Colored)\n")
    
    #Cursor/Scores/similar
    MAINWINDOW.blit(logo, (540, 380)) #Draw the logo of the main developer.
    MAINWINDOW.blit(cursorImage, (mouseX, mouseY)) #Draw the "cursor" at the mouse position.
    
    scoretext = "Score: " + str(score) #Define what the text for the score is.
    saveFile.write(scoretext + "\n")
    textscore = RegFont.render(scoretext, 1, ORANGE) #Define the actual text to draw.
    MAINWINDOW.blit(textscore, (0, 0)) #Draw the text on the screen.
    
    if rekt == True: #If an enemy approached the character,
        saveFile.write("GAME OVER")
        if endPlayOne == True: #If we haven't play the sound yet.
            endSound.play() #Play the end sound.
            endPlayOne = False #Set the variable to false to make sure the sound doesn't play multiple times/sound peculiar.
        endRekt = RegFont.render("#REKT", 1, ORANGE) #Define the text, "#REKT".
        MAINWINDOW.blit(endRekt, (280, 240)) #Render the text.
        waitTillEnd -= 1 #Remove 1 tick from the variable until we run out. This is useful for the sound and other things.
        if waitTillEnd == 0: #If we run out,
            #We have to print some copyright stuff. Again.
            print("RandomGame Copyright (C) 2014 Nathan Guerrero/PoniesFiM") #First line
            print("This program comes with ABSOLUTELY NO WARRANTY; for details go to GPL.txt or README.txt") #Second line
            print("This is free software, and you are welcome to redistribute it") #Third line
            print("under certain conditions.") #Fourth line.
            print("\n")
            print("GitHub at https://github.com/OfficialPoniesFiM/RealRandomGame") #Refers people to the GitHub link.
            whiles = False
    
    #The game updates.
    pygame.display.update()
    
    #The save file closes to update.
    saveFile.close()
    
    #We wait.
    fpsClock.tick(FPS)
pygame.quit() #Pygame quits.
sys.exit() #Sys exits.
