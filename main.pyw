# Imports
from buttonClass import *
import pygame
import random
from pygame import mixer

pygame.init()

##########################

# The screen

screen = pygame.display.set_mode((670, 540))

##########################

# Objects

# Answer Text
answerInt = 0
text = ""
font2 = pygame.font.Font('freesansbold.ttf', 50)

# Defining the text
def show_answer(x, y):
    # Rendering the text
    answerText = font2.render(str(text) + str(answerInt), True, (0, 0, 0))
    # Drawing the text
    screen.blit(answerText, (x, y))

# Score
streak = 0
font = pygame.font.Font('freesansbold.ttf', 27)

# Defining the text
def show_score(x, y):
    # Rendering the text
    scoreText = font.render("Streak: " + str(streak), True, (0, 0, 0))
    # Drawing the text
    screen.blit(scoreText, (x, y))

# Background
bg = pygame.image.load('bg.png')

pos = pygame.mouse.get_pos()
btn1 = button(pygame.image.load('1.png'), 1, 20, 200)
btn2 = button(pygame.image.load('2.png'), 2, 180, 200)
btn3 = button(pygame.image.load('3.png'), 3, 340, 200)
btn4 = button(pygame.image.load('4.png'), 4, 500, 200)
btn5 = button(pygame.image.load('5.png'), 5, 20, 285)
btn6 = button(pygame.image.load('6.png'), 6, 180, 285)
btn7 = button(pygame.image.load('7.png'), 7, 340, 285)
btn8 = button(pygame.image.load('8.png'), 8, 500, 285)
btn9 = button(pygame.image.load('9.png'), 9, 180, 370)
btn0 = button(pygame.image.load('0.png'), 0, 340, 370)
btnClear = button(pygame.image.load('clear.png'), 10, 180, 455)
btnSubmit = button(pygame.image.load('submit.png'), 11, 340, 455)

num1 = random.randint(0, 30)
num2 = random.randint(0, 30)
operations = ["addition", "subtraction"]
solution = 0

bool1 = False
bool2 = False
bool3 = False
bool4 = False
bool5 = False
bool6 = False
bool7 = False
bool8 = False
bool9 = False
bool0 = False
bool10 = False
bool11 = False

# Icon and caption
pygame.display.set_icon(pygame.image.load('icon.png'))
pygame.display.set_caption("Math Game: Easy Edition")

# Sounds
correct = mixer.Sound('correct.mp3')
incorrect = mixer.Sound('yousuck.mp3')
correct.set_volume(0.5)
incorrect.set_volume(0.3)

##########################

# Main game loop

solving = False
clicked = False
running = True
run = True
while run:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            # Click event
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = True
        
        # Generating a bunch of sprites
        screen.blit(bg, (0, 0))
        show_score(10, 10)
        btn1.generate(screen)
        btn2.generate(screen)
        btn3.generate(screen)
        btn4.generate(screen)
        btn5.generate(screen)
        btn6.generate(screen)
        btn7.generate(screen)
        btn8.generate(screen)
        btn9.generate(screen)
        btn0.generate(screen)
        btnClear.generate(screen)
        btnSubmit.generate(screen)
        show_answer(90, 90)

        # Click detection
        if clicked == True:
            bool1 = btn1.isOver(pos)
            bool2 = btn2.isOver(pos)
            bool3 = btn3.isOver(pos)
            bool4 = btn4.isOver(pos)
            bool5 = btn5.isOver(pos)
            bool6 = btn6.isOver(pos)
            bool7 = btn7.isOver(pos)
            bool8 = btn8.isOver(pos)
            bool9 = btn9.isOver(pos)
            bool0 = btn0.isOver(pos)
            bool10 = btnClear.isOver(pos)
            bool11 = btnSubmit.isOver(pos)
            clicked = False
        if len(str(answerInt)) != 8:
            if bool1:
                clicked = False
                bool1 = False
                answerInt *= 10
                answerInt += 1
            if bool2:
                clicked = False
                bool2 = False
                answerInt *= 10
                answerInt += 2
            if bool3:
                clicked = False
                bool3 = False
                answerInt *= 10
                answerInt += 3
            if bool4:
                clicked = False
                bool4 = False
                answerInt *= 10
                answerInt += 4
            if bool5:
                clicked = False
                bool5 = False
                answerInt *= 10
                answerInt += 5
            if bool6:
                clicked = False
                bool6 = False
                answerInt *= 10
                answerInt += 6
            if bool7:
                clicked = False
                bool7 = False
                answerInt *= 10
                answerInt += 7
            if bool8:
                clicked = False
                bool8 = False
                answerInt *= 10
                answerInt += 8
            if bool9:
                clicked = False
                bool9 = False
                answerInt *= 10
                answerInt += 9
            if bool0:
                clicked = False
                bool0 = False
                answerInt *= 10
        if bool10:
            clicked = False
            bool10 = False
            if randomOperation == "addition":
                answer = str(num1) + "+" + str(num2) + " = "
                answerInt = 0
            else:
                answer = str(num1) + "-" + str(num2) + " = "
                answerInt = 0
        if bool11:
            clicked = False
            bool11 = False
            if answerInt == solution:
                correct.play()
                streak += 1
            elif answerInt != solution:
                incorrect.play()
                streak = 0
            answerInt = 0
            solving = False
        
        if solving == False:
            num1 = random.randint(0, 30)
            num2 = random.randint(0, 30)
            randomOperation = operations[random.randint(0, 1)]
            if randomOperation == "addition":
                solution = num1+num2
                text = str(num1) + "+" + str(num2) + " = "
            if randomOperation == "subtraction":
                if num1-num2 > 0:
                    solution = num1-num2
                    text = str(num1) + "-" + str(num2) + " = "
                else:
                    num1 = num2
                    solution = num1-num2
                    text = str(num1) + "-" + str(num2) + " = "
            solving = True


        pos = pygame.mouse.get_pos()
        pygame.time.delay(20)
        pygame.display.update()
