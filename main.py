import pygame
import os
import math
import random


# setup display
pygame.init()                                                                                                                                                                                                                                                                                                                                                                             
width,height = 800,500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bunnie's Hangman")

# BUTTONS
radius = 20
gap = 15
letters = []
startx = round((width - ( radius * 2 + gap) * 13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
letter_font = pygame.font.SysFont('comicsans',40)
word_font = pygame.font.SysFont('comicsans',60)
title_font = pygame.font.SysFont('comicsans', 70)

# load images
images = []
for i in range(7):
    image = pygame.image.load(r"C:\Users\asus\Documents\project\hangman\hangman" + str(i) + ".png")
    images.append(image)

# game variables   
hangman_status = 0
file = open(r"C:\Users\asus\Documents\project\hangman\words.txt","r")
words = file.readline().split()
WORD = random.choice(words)
WORD = WORD.upper()
guessed = []


# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# setup game loop

def draw():
    win.fill(WHITE)
    # draw title
    text = title_font.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (width/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in WORD:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    


# draw buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),radius,3)
            text = letter_font.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()



FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS) 

    
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters: 
                x,y,ltr,visible = letter
                if visible:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < radius:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in WORD:
                            hangman_status +=1
    
    won = True
    for letter in WORD:
        if letter not in guessed:
            won = False
            break

    if won:
        win.fill(WHITE)
        text = word_font.render("You Won!",1,BLACK)
        win.blit(text,(width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
        break
    if hangman_status == 7:
        win.fill(WHITE)
        text = word_font.render("You Lost :(",1,BLACK)
        text2 = word_font.render("The word was : "+WORD,1,BLACK)
        win.blit(text,(width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        win.blit(text2,(150,300))
        pygame.display.update()
        pygame.time.delay(4000)
        break


pygame.quit()
