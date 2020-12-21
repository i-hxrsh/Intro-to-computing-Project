#first imported necessary modules
import pygame
import os
import sys
import random
import math
# I need to initialize the pygame module so:
pygame.init()
#I fix the screen size using pyygame
width=800
height=600
screen=pygame.display.set_mode((width,height))
#I'll set the window name
pygame.display.set_caption('Musical Hangman Game')
# I need some colours. Each colour has a set of values that gives it a specific colour. Values are known as RGB values.

white=(255,255,255)
black=(0,0,0)
#I want to set a background image
def backgroundimage():
    
    backgroundimage=pygame.image.load('background.jpg')
    screen.blit(backgroundimage,[0,0])
#pygame.display.update()
#Loadinng the engame message, that is after winning or losing:
win_image=pygame.image.load('if_you_win.jpg')
loss_image=pygame.image.load('if_you_lose.jpg')



#We'll now add background music to the intro using pygame
pygame.mixer.music.load('mystery them music.mp3')
pygame.mixer.music.play(-1,0.0)    #-1 makes it run forever and 0.0 decides the exact time from when it will start
pygame.mixer.music.fadeout(5000)  ##This is just the intro music so this code stops it after 5 seconds


#Adding Intro Theme
font=pygame.font.SysFont('Arial.tff',32)
backgroundimage() 
introtext=font.render("WELCOME TO MUSICAL HANGMAN",True,black)
textrect=introtext.get_rect()
textrect.center=((400,300))




#I'll also need to add fps later to the game loop. So defining fps here:
fps=60
clock=pygame.time.Clock()



#Here I'm calling the Intro theme
start_time = pygame.time.get_ticks() #time.get_ticks() function returns the time passed in miliseconds.
while pygame.time.get_ticks() < start_time+5000:      ##This code is controlling the time for intro theme.
    screen.blit(introtext,textrect)
    pygame.display.update()


#LIST OF THE IMAGES OF THE HANGING MAN AT DIFFERENT STAGES OF GAMEPLAY INVOLVED IN THE GAME:
image1=pygame.image.load('Image1.jpg')
image2=pygame.image.load('Image2.jpg')
image3=pygame.image.load('Image3.jpg')
image4=pygame.image.load('Image4.jpg')
image5=pygame.image.load('Image5.jpg')
image6=pygame.image.load('Image6.jpg')
image7=pygame.image.load('Image7.jpg')
images=[image1,image2,image3,image4,image5,image6,image7]


#LIST OF ALPHABETS FOR MAKING THE ALPHABET BUTTONS:
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alphabets=[]
for letter in alphabets:
    Alphabets.append(letter.upper())



#Defining positions of alphabets:
positions_of_alphabets=[]
starting_x=60
ending_x=720
gap_between_postions=((ending_x-starting_x)//12)
print(starting_x,ending_x,gap_between_postions)
for i in range(13):
    x=starting_x+i*gap_between_postions
    y=400
    positions_of_alphabets.append([x,y])
for i in range(13):
    x=starting_x+i*gap_between_postions
    y=500
    positions_of_alphabets.append([x,y])



main_button_controller=[] #THIS LIST CONTAINS ALPHABETS,THEIR POSITIONS, AND CONTROLS WHETHER A BUTTON IS VISIBLE OR NOT
for i in range(26):
    main_button_controller.append([positions_of_alphabets[i][0],positions_of_alphabets[i][1],Alphabets[i],True])


###########################################################
#Structure of alphabet buttons:
Radius=20
def buttons():
    for elements in main_button_controller:
        x,y,ltr,value=elements
        if value==True:                                            #I wasn't able to execute this part of the buttons
                                                                   #so had to look up for it in the internet.
            pygame.draw.circle(screen,black,(x,y),20,2)
            FONT=pygame.font.SysFont('Bradley Hand ITC.tff',40)
            buttonletters=FONT.render(ltr,True,black)
            screen.blit(buttonletters,[x-9,y-12])
###############################################################            




# LIST OF MUSIC THAT WILL PLAY IN THE GAME:
Songs=['Bekhayali.mp3','Bulleya.mp3','Dilbar.mp3','Galliyan.mp3','Garmi.mp3','Hasi.mp3','Hosanna.mp3','Khwahishein.mp3','Machayenge.mp3','Makhna.mp3','Malang.mp3','matargashti.mp3','Muqabla.mp3','Pachtaoge.mp3','Raabta.mp3','duniyaa.mp3','filhaal.mp3','jeet.mp3','vaaste.mp3']
Songnames=['BEKHAYALI','BULLEYA',"DILBAR",'GALLIYAN','GARMI','HASI','HOSANNA','KHWAHISHEIN','MACHAYENGE','MAKHNA','MALANG','MATARGASHTI','MUQABLA','PACHTAOGE','RAABTA','DUNIYAA','FILHAAL',"JEET",'VAASTE']
    
 

#I am trying to define the gameplay here
randomsong=random.choice(Songs)                  #CHOOSING RANDOM SONG FROM THE SONG LIST
pygame.mixer.music.load(randomsong)              
pygame.mixer.music.play(-1,0.0)                  #LOADING AND PLAYING THE SONG FOR INIFINITE TIME USING -1 AS PARAMETER
index_of_song= Songs.index(randomsong)
randomword=Songnames[index_of_song]              #THIS WORD IS USED FOR THE HANGMAN GAME
#print(randomword)                                
letter_of_randomword=[]                          #
display_of_letters=[]                            # I created these lists to control the game play and to decide
correctly_guessed_letters=[]                     # what to show on screen as a display of underscores and letters.
for i in range(len(randomword)):                 # 
        display_of_letters.append('_')           #
for event in pygame.event.get():               
    if event.type==pygame.QUIT:
        quit()



#GUESSED LETTERS LIST:
Guessed_letters=[]                               #This list will store the guessed letters through mouse button input.

#Status of no of correctly and incorrectly guessed letter   
no_of_correct_guesses=0                          #These varibales will control the number of turns the user gets
no_of_incorrect_guesses=0                        #and whether all the letters are guessed or not


#Main game running loop starts from here
run=True
while run:
    
    for letters in randomword:
        letter_of_randomword.append(letters)                 #This appends the letters of name of song
                                                             #to the list we used before the game loop
    
    sorted_letter_of_randomword=sorted(list(set(letter_of_randomword)))  # We will use this list to determine
                                                                         # whether all correct letters have been
                                                                         # guessed or not
   
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        if event.type==pygame.MOUSEBUTTONDOWN:

            ################################################################################
            a,b=pygame.mouse.get_pos() #a,b are the coordinates of the mouse pointer
            #print(a,b)
            for elements in main_button_controller:
                x_coordinate,y_coordinate,charcter,value=elements
                dis=math.sqrt((x_coordinate-a)**2+(y_coordinate-b)**2)
                if dis<Radius:
                    elements[3]=False
                    Guessed_letters.append(elements[2])
                    for guesses in Guessed_letters:
                        if guesses in sorted_letter_of_randomword:
                            correctly_guessed_letters.append(guesses)
            
                    
                    if elements[2] in letter_of_randomword:
                        no_of_correct_guesses+=1
                    elif elements[2] not in letter_of_randomword:
                        no_of_incorrect_guesses+=1
                    
    # The if statement below decides whether we need anymore input from the user and also decides what 
    # would combination of letters and underscores will be displayed to he user.
    
    if no_of_incorrect_guesses+1<7 and sorted(list(set(correctly_guessed_letters)))!=sorted_letter_of_randomword:
                        
        string=''
        for chars in display_of_letters:
            string=string+' '+chars
        #print(string)
        for numbers in range(len(randomword)):
            if letter_of_randomword[numbers] in correctly_guessed_letters:
                display_of_letters[numbers]=letter_of_randomword[numbers]


    #Defininng the FPS of the game:
    clock.tick(fps)
    
    
    #This if statements defines what will be shown to the user at the start of the game
    if len(Guessed_letters)==0:
        
        backgroundimage()
        screen.blit(images[no_of_incorrect_guesses],[75,100])
        font_of_display=pygame.font.Font(None,30)
    
        text_display=font_of_display.render('_ '*len(randomword),True,black)
        text_display_rect=text_display.get_rect()
        text_display_rect.center=[400,200]
        screen.blit(text_display,text_display_rect)
        buttons()
        pygame.display.update()
    
    #This if statement defines what will be shown to the user as the game proceeds
    elif len(Guessed_letters)>0:
        
        backgroundimage()
        screen.blit(images[no_of_incorrect_guesses],[75,100])
        font_of_display=pygame.font.Font(None,30)
    
        text_display=font_of_display.render(string,True,black)
        text_display_rect=text_display.get_rect()
        text_display_rect.center=[400,200]
        screen.blit(text_display,text_display_rect)
        buttons()
        pygame.display.update()
    
    #This is used to end the game once either the user guesses all the letters or exhausts his number of guesses
    if sorted(list(set(correctly_guessed_letters)))==sorted_letter_of_randomword:
        
        run=False
    elif no_of_incorrect_guesses>=6:
        pygame.time.wait(1000)
        run=False


#NOW I'm defining the ending screen i.e.,what happens once the game gets over:
ending=True
while ending:
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    if no_of_incorrect_guesses==6:
        screen.blit(loss_image,[0,0])
        pygame.display.flip()
        pygame.time.wait(2000)
        ending=False
    elif sorted(list(set(correctly_guessed_letters)))==sorted_letter_of_randomword:
        screen.blit(win_image,[0,0])
        pygame.display.flip()
        pygame.time.wait(2000)
        ending=False

    

                    

                




   
    
      
