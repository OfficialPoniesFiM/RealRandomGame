#This is a simple game. 
#Copyright (C) 2014 Nathan Guerrero/PoniesFiM

#We have to print some copyright stuff.
print("RandomGame Copyright (C) 2014 Nathan Guerrero/PoniesFiM") #First line
print("This program comes with ABSOLUTELY NO WARRANTY; for details go to GPL.txt or README.txt") #Second line
print("This is free software, and you are welcome to redistribute it") #Third line
print("under certain conditions.") #Fourth line.
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n") #Separator.

#We need to import some of the things we need.
print("Importing things...")
import pygame, sys
import random
from pygame.locals import *
print("Imported...")

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
mainSniper = pygame.image.load("sniper.png") #Main character(you play this).

#Enemies.
otherSniper = pygame.image.load("sniper.png") #The other sniper.
creeper = pygame.image.load("creeper.png") #The creeper.

#Particles.
mlg = pygame.image.load("mlg.jpg") #A particle.
machinima = pygame.image.load("machinima.png") #A particle.
hacker1 = pygame.image.load("hacker.png") #A particle.
hacker2 = pygame.image.load("hacker2.png") #A particle.

#Other stuff.
cursorImage = pygame.image.load("cursor.png") #We use this as a our "cursor".
print("Finished loading those things!")

#We have some sounds we need to get.
print("Loading the sounds...")
#The sounds
#Rage
kiddingMe = pygame.mixer.Sound('kiddingme.ogg') #A rage sound that plays when an enemy is killed.
comeOn = pygame.mixer.Sound('comeon.ogg') #A rage sound that plays when an enemy is killed.
what = pygame.mixer.Sound('what.ogg') #A rage sound that plays when an enemy is killed.

#Extras.
endSound = pygame.mixer.Sound('end.ogg') #The end sound when an enemy approaches you.
gunshot = pygame.mixer.Sound('lasergun.wav') #The sound the plays when you click the mouse(shoot a gun).
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
hitSniperTime = 60 #This is the variable that represents the time of when the particle appears. 1 equals one tick. The game refreshes 60 times a second, so 60 ticks should be equal to 1 second.
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

#The game loop.
while True:
    pygame.mouse.set_visible(False) #This makes the cursor invisible, so we can use an image as a cursor.
    
    for event in pygame.event.get(): #looks for events.
        if event.type == QUIT: #This is what happens when someone wants to close the program.
            pygame.quit() #First, Pygame has to quit.
            sys.exit() #Since we can't reach the end of the line, we have to exit the program with this method.
        
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
    
    globalDirection += 5 #This sets the direction of the particles.
    rmlg = pygame.transform.rotate(mlg, globalDirection) #The rotated version of this particle is stored in another "variable".
    rmachinima = pygame.transform.rotate(machinima, globalDirection) #The rotated version of this particle is stored in another "variable".
    rhacker1 = pygame.transform.rotate(hacker1, globalDirection) #The rotated version of this particle is stored in another "variable".
    rhacker2 = pygame.transform.rotate(hacker2, globalDirection) #The rotated version of this particle is stored in another "variable".
    
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
            hitCreeperTime = 60 #Time gets reset to 60 ticks/1 second.
    
    else:
        if otherKilled == False: #If otherKilled(unknown purpose) is False, set hitCreeperTime to 60.
            hitCreeperTime = 60
        particle = random.randint(1,4) #Sets what particle to use/render.
    
    if hitSniper == True: #If the sniper got hit,
        hitSniperTime -= 1 #Remove 1 tick from this variable until time runs out. Time is used to render particles.
        if hitSniperTime == 0: #If time runs out(at 0),
            hitSniper = False #Set hitSniper to False, to let the enemy sniper move, and to stop rendering the particle.
            hitSniperTime = 60 #Reset the time for later.
            otherKilled = False #Unknown purpose.
    else:
        hitSniperTime = 60 #Reset the time to 60 ticks/1 second to make sure time goes correctly.
        otherKilled = False #Unknown purpose.
    
    if onePlay == True: #When the game wants to play a sound because of a Creeper being hit,
        current1play = random.randint(1,3) #Get a random number.
        if current1play == 1: #If the number is 1,
            kiddingMe.play() #Play this sound.
        elif current1play == 2: #If the number is 2,
            comeOn.play() #Play this sound.
        elif current1play == 3: #If the number is 3,
            what.play() #Play this sound.
        onePlay = False #Set this variable to false to make sure sounds don't play again until Creeper gets hit again.
    
    if twoPlay == True: #When the game wants to play a sound because of an enemy Sniper being hit,
        current2play = random.randint(1,3) #Get a random number.
        if current2play == 1: #If the number is 1,
            kiddingMe.play() #Play this sound.
        elif current2play == 2: #If the number is 2,
            comeOn.play() #Play this sound.
        elif current2play == 3: #If the number is 3,
            what.play() #Play this sound.
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
    
    #Cursor/Scores/similar
    MAINWINDOW.blit(cursorImage, (mouseX, mouseY)) #Draw the "cursor" at the mouse position.
    
    scoretext = "Score: " + str(score) #Define what the text for the score is.
    textscore = RegFont.render(scoretext, 1, ORANGE) #Define the actual text to draw.
    MAINWINDOW.blit(textscore, (0, 0)) #Draw the text on the screen.
    
    if rekt == True: #If an enemy approached the character,
        if endPlayOne == True: #If we haven't play the sound yet.
            endSound.play() #Play the end sound.
            endPlayOne = False #Set the variable to false to make sure the sound doesn't play multiple times/sound peculiar.
        endRekt = RegFont.render("#REKT", 1, ORANGE) #Define the text, "#REKT".
        MAINWINDOW.blit(endRekt, (280, 240)) #Render the text.
        waitTillEnd -= 1 #Remove 1 tick from the variable until we run out. This is useful for the sound and other things.
        if waitTillEnd == 0: #If we run out,
            pygame.quit() #Quit Pygame.
            sys.exit() #Exit the program.
    
    #The game updates.
    pygame.display.update()
    
    #We wait.
    fpsClock.tick(FPS)
