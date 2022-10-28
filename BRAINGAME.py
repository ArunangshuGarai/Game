import pygame
from pygame.locals import *
import time
import Logic
import Button_making

pygame.init()
Screenheight=640
Screenwidth=480
screen=pygame.display.set_mode((Screenheight,Screenwidth))
clock = pygame.time.Clock()

Button_Rect=pygame.Rect(320-50,240-50,100,100)
start_button=pygame.Rect(320-100,240-50,200,100)
playagain_button= pygame.Rect(640-150,480-150,100,100)

font=pygame.font.SysFont("Cooper Black",72)

fontus=pygame.font.SysFont("Algerian",100)
value_text = fontus. render ("BRAIN GAME", True, "RED")
text_rect = value_text.get_rect(center=(320, 190) )
screen.blit(value_text, text_rect)
pygame.display.flip()

fontus=pygame.font.SysFont("Arial",20)
value_text = fontus. render ("--- Click Anywhere to Continue ---", True, "RED")
text_rect = value_text.get_rect(center=(320, 420) )
screen.blit(value_text, text_rect)
pygame.display.flip()

button1 = pygame.Rect(210, 100, 50, 50)  # create button 1
button5 = pygame.Rect(210, 160, 50, 50)  # create button 2
button9 = pygame.Rect(210, 220, 50, 50)  # create button 3
button13= pygame.Rect(210, 280, 50, 50)  # create button 4

button2 = pygame.Rect(270, 100, 50, 50)  # create button 5
button6 = pygame.Rect(270, 160, 50, 50)  # create button 6
button10 = pygame.Rect(270, 220, 50, 50)  # create button 7
button14 = pygame.Rect(270, 280, 50, 50)  # create button 8

button3 = pygame.Rect(330, 100, 50, 50)  # create button 9
button7 = pygame.Rect(330, 160, 50, 50)  # create button 10
button11= pygame.Rect(330, 220, 50, 50)  # create button 11
button15= pygame.Rect(330, 280, 50, 50)  # create button 12

button4= pygame.Rect(390, 100, 50, 50)  # create button 13
button8= pygame.Rect(390, 160, 50, 50)  # create button 14
button12= pygame.Rect(390, 220, 50, 50)  # create button 15
button16= pygame.Rect(390, 280, 50, 50)  # create button 16

Button1=pygame.Rect(210-4, 100-4, 58, 58)  # create button 1.2
Button5 = pygame.Rect(210-4, 160-4, 58, 58)  # create button 2
Button9 = pygame.Rect(210-4, 220-4, 58, 58)  # create button 3
Button13= pygame.Rect(210-4, 280-4, 58, 58)  # create button 4

Button2 = pygame.Rect(270-4, 100-4, 58, 58)  # create button 5
Button6 = pygame.Rect(270-4, 160-4, 58, 58)  # create button 6
Button10 = pygame.Rect(270-4, 220-4, 58, 58)  # create button 7
Button14 = pygame.Rect(270-4, 280-4, 58, 58)  # create button 8

Button3 = pygame.Rect(330-4, 100-4, 58, 58)  # create button 9
Button7 = pygame.Rect(330-4, 160-4, 58, 58)  # create button 10
Button11= pygame.Rect(330-4, 220-4, 58, 58)  # create button 11
Button15= pygame.Rect(330-4, 280-4, 58, 58)  # create button 12

Button4= pygame.Rect(390-4, 100-4, 58, 58)  # create button 13
Button8= pygame.Rect(390-4, 160-4, 58, 58)  # create button 14
Button12= pygame.Rect(390-4, 220-4, 58, 58)  # create button 15
Button16= pygame.Rect(390-4, 280-4, 58, 58)  # create button 16

user_set=[]
# mouse_pos=[]
def main():
    click=True
    total_time=0
    Box_drawn=False
    x,y=0,0

    font = pygame.font.SysFont('Consolas', 100)

    while True:
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click==True:
                screen.fill((222,142,14))

                for i in range (110):                
                    font = pygame.font.SysFont('Algerian',int(72-i*0.25))
                    title= font. render ("BRAIN GAME", True, ("Black"))
                    title_pos = title.get_rect(center= (320, 180-i))
                    screen.blit(title, title_pos)
                    clock.tick(120)
                    pygame.display.update()
                    
                    screen.fill((222,142,14))
                else:
                    Heading()
                    pygame.display.update()
                    click=False
                    #Start Button
                    Start_button()
                    Playagain_button()
                    total_time=pygame.time.get_ticks()
                    print(total_time)
                    break

            if event.type== MOUSEBUTTONDOWN and event.button==1 and start_button.collidepoint(event.pos) and Box_drawn==False:
                screen.fill((222,142,14))
                Heading()
                fontus=pygame.font.SysFont("Cooper Black",72) #i= 99
                pygame.display.update()

                pygame.time.delay(250)

                value_text = fontus. render ("Get", True, (80, 12, 63))
                text_rect = value_text.get_rect(center=(320, 240) ) #i=99 (100, 5)
                screen.blit(value_text, text_rect)
                
                pygame.display.update()

                pygame.time.delay(1000)

                button1 = pygame.Rect(320-150, 240-30, 300, 60)  # create button 1                
                pygame.draw.rect(screen, (222,142,14), button1)# draw button 1

                pygame.display.update()

                pygame.time.delay(250)

                fontus=pygame.font.SysFont("Cooper Black",72) #i= 99
                value_text = fontus. render ("Set", True, (80, 12, 63))
                text_rect = value_text.get_rect(center=(320, 240) ) #i=99 (100, 5)
                screen.blit(value_text, text_rect)
                pygame.display.update()

                pygame.time.delay(1000)

                button1 = pygame.Rect(320-150, 240-30, 300, 60)  # create button 1                
                pygame.draw.rect(screen, (222,142,14), button1)# draw button 1

                pygame.display.update()

                pygame.time.delay(250)

                fontus=pygame.font.SysFont("Cooper Black",72) #i= 99
                value_text = fontus. render ("Go...", True, (80, 12, 63))
                text_rect = value_text.get_rect(center=(320, 240) ) #i=99 (100, 5)
                screen.blit(value_text, text_rect)
                pygame.display.update()

                pygame.time.delay(1000)

                button1 = pygame.Rect(320-150, 240-30, 300, 60)  # create button 1                
                pygame.draw.rect(screen, (222,142,14), button1)# draw button 1

                pygame.display.update()

                pygame.time.delay(250)
                timer()
                pygame.display.update()

                pygame.draw.rect(screen,(31, 97, 141),Button_Rect,3,5)
                pygame.display.update()  

                screen.fill((237, 228, 224)) 
                DrawButtons()
                # #Numbers on Buttons
                # NumberOnButtons()

                # #WINNER || BETTER LUCK NEXT TIME !
                # Result(user_set.sort())
                
                pygame.display.flip()
                # pygame.display.update()        
                
                Box_drawn=True
                # pygame.display.flip()                
                break
            
            if event.type== MOUSEBUTTONDOWN and event.button==1 and Box_drawn==True and len(user_set)<5:
                mouse_pos = event.pos  # get mouse position
                # check if mouse position is over button
                # print(Logic.win_set)
                # print(Logic.grid)
                # print("mouse_pos :",mouse_pos)
                print(button2.collidepoint(mouse_pos))
                Button_response(mouse_pos)
                print("mouse_pos:",mouse_pos)

                Button_border(mouse_pos)
                
                
                #WINNER || BETTER LUCK NEXT TIME !
                Result(user_set)

                # result(user_set)
                user_set.sort()
                Logic.win_set.sort()
                print("user_choice:",user_set)
                print("Logic.win_set:",Logic.win_set)
                break
                 
            # print(total_time)   
            # pygame.time.delay(total_time)            
            # screen.fill((222,142,14))   
        if Box_drawn==True:
            Heading()
            DrawButtons()

            # update the screen

            font = pygame. font.SysFont('Consolas', 32 )

            #Numbers on Buttons
            NumberOnButtons()
            # #WINNER || BETTER LUCK NEXT TIME !
            # Result(user_set)
            
            # print("user_set:",user_set)
  
        pygame.display.flip()
    
def timer():
    for i in range(5):
        # Using draw.rect module of
        # pygame to draw the solid circle
        pygame.draw.circle(screen,(251, 200, 100),[160,240],50,0) #Inner Number Circle
        pygame.draw.circle(screen,"Black",[160,240],73,6)

        if(i==0): 
            # pygame.draw.arc(screen,"Red",(160-99,240-99,198,198),3.14/2,5*3.14/2,15)
            pygame.draw.arc(screen,"Red",(160-70,240-70,140,140),3.14/2,5*3.14/2,15)
            

            value_text = font. render (str(5), True, "Black")
            text_rect = value_text.get_rect(center= (160,240-10))

            screen.blit(value_text, text_rect)
            pygame.display.update()
            pygame.time.delay(750)

        # pygame.draw.circle(screen, "Gray",
        #                 [160, 240], 100, 15)
        pygame.draw.circle(screen, "Gray",
                        [160, 240], 70, 15)
        # pygame.draw.arc(screen,"Red",(160-100,240-100,200,200),3.14/2,5*3.14/2-2*3.14/5*(i+1),16)
        pygame.draw.arc(screen,"Red",(160-70,240-70,140,140),3.14/2,5*3.14/2-2*3.14/5*(i+1),16)

        pygame.draw.circle(screen,(251, 200, 100),[160,240],50,0)
        pygame.draw.circle(screen,("#A8E890"),[160,240],55,6)

        value_text = font. render (str(5-i-1), True, "Black")
        text_rect = value_text.get_rect(center= (160,240-10))

        screen.blit(value_text, text_rect)
        pygame.display.update()

        # Draws the surface object to the screen.
        pygame.draw.rect(screen,(31, 97, 141),Button_Rect,5,15)
        iButton_Rect=pygame.Rect(320-45,240-45,90,90)
        pygame.draw.rect(screen,(7, 247, 236),iButton_Rect,0,10)

        pygame.display.update()
        pygame.time.delay(100)  

        value_text = font. render (str(Logic.win_set[i]),  True, "Black")
        text_rect = value_text.get_rect(center= (320,240))
        screen.blit(value_text, text_rect)

        pygame.display.update()
        print(pygame.time.delay(900))

def Start_button():
    pygame.draw.ellipse(screen,"Red",start_button)
    pygame.draw.ellipse(screen,"Black",start_button,8)
    fontus=pygame.font.SysFont("Cooper Black",48)
    value_text = fontus. render ("Start", True, "Black")
    text_rect = value_text.get_rect(center= (320,240))
    screen.blit(value_text, text_rect)

def Playagain_button():
    pygame.draw.ellipse(screen,"Red",playagain_button)
    pygame.draw.ellipse(screen,"Black",playagain_button,4)
    fontus=pygame.font.SysFont("Cooper Black",48)
    value_text = fontus. render ("Start", True, "Black")
    text_rect = value_text.get_rect(center= (320,240))
    screen.blit(value_text, text_rect)

def Heading():
    # fonti = pygame.font.SysFont('Algerian',72)
    # title = fonti.render("BRAIN GAME", True, (252,14,14))
    # screen.blit(title, (100, 5))

    heading_font=pygame.font.SysFont("Cooper Black",int(72-99*0.25)+10) #i= 99
    value_text = heading_font. render ("BRAIN GAME", True, (80, 12, 63))
    text_rect = value_text.get_rect(center=(320, 150-99) ) #i=99 (100, 5)
    screen.blit(value_text, text_rect)


def DrawButtons():
    # draw button 1
    pygame.draw.rect(screen, (0, 200, 0), button1)
    # draw button 2
    pygame.draw.rect(screen, (0, 0, 200), button2)
    # draw button 3
    pygame.draw.rect(screen, (0, 120, 200), button3)
    # draw button 4
    pygame.draw.rect(screen, (0, 200, 100), button4)
    # draw button 5
    pygame.draw.rect(screen, (100, 0, 200), button5)
    # draw button 6
    pygame.draw.rect(screen, (100, 100, 200), button6)
    # draw button 7
    pygame.draw.rect(screen, (123, 200, 100), button7)
    # draw button 8
    pygame.draw.rect(screen, (100, 123, 200), button8)
    # draw button 9
    pygame.draw.rect(screen, (100, 233, 200), button9)
    # draw button 10
    pygame.draw.rect(screen, (210, 200, 100), button10)
    # draw button 11
    pygame.draw.rect(screen, (100, 100, 200), button11)
    # draw button 12
    pygame.draw.rect(screen, (100, 200, 200), button12)
    # draw button 13
    pygame.draw.rect(screen, (152, 233, 200), button13)
    # draw button 14
    pygame.draw.rect(screen, (210, 250, 100), button14)
    # draw button 15
    pygame.draw.rect(screen, (100, 110, 200), button15)
    # draw button 16
    pygame.draw.rect(screen, (10, 200, 200), button16)


def NumberOnButtons():
    number_font=pygame. font.SysFont('Consolas', 32 )
    for i in range(4):
        for j in range(4):
            value_text = number_font. render (str(Logic.grid[j][i]), True, "Black")
            text_rect = value_text.get_rect(center= (i*60+210+25, j*60+100+28))
            screen.blit(value_text, text_rect)


def Result(user_choice):
    # print(user_choice)
    # print(len(user_choice))
    if(len(user_choice)==5):
        user_choice.sort()
        
        Logic.win_set.sort()
        # print(Logic.win_set)
        if(user_choice==Logic.win_set):
            # print("Winner !")
            # print("user_choice:",user_choice)
            # print("Logic.win_set:",Logic.win_set)
            fontus=pygame.font.SysFont("Algerian",72)
            value_text = fontus. render ("Winner", True, "RED")
            text_rect = value_text.get_rect(center=(335, 400) )
            screen.blit(value_text, text_rect)
            # return 1           
        else:
            # print("Better Luck Next Time !")
            fontus=pygame.font.SysFont("Algerian",72)
            value_text = fontus. render ("Better Luck", True, "RED")
            text_rect = value_text.get_rect(center=(335, 370) )
            screen.blit(value_text, text_rect)
            value_text = fontus. render ("Next Time !", True, "RED")
            text_rect = value_text.get_rect(center=(335, 440) )
            screen.blit(value_text, text_rect)
            # return 2
        print("Thank You For Playing !")

def Button_response(click_pos):
    if button1.collidepoint(click_pos):
        print('button 1 was pressed',Logic.grid[0][0])  
        user_set.append(Logic.grid[0][0])
        pygame.draw.rect(screen,(202,20,30),button1)

    elif button2.collidepoint(click_pos):
        print('button 2 was pressed',Logic.grid[0][1])
        user_set.append(Logic.grid[0][1])
        pygame.draw.rect(screen,(202,20,30),button2)

    elif button3.collidepoint(click_pos):
        print('button 3 was pressed',Logic.grid[0][2])
        user_set.append(Logic.grid[0][2])
        pygame.draw.rect(screen,(202,20,30),button3)

    elif button4.collidepoint(click_pos):
        print('button 4 was pressed',Logic.grid[0][3])
        user_set.append(Logic.grid[0][3])
        pygame.draw.rect(screen,(202,20,30),button4)

    elif button5.collidepoint(click_pos):
        print('button 5 was pressed',Logic.grid[1][0])
        user_set.append(Logic.grid[1][0])
        pygame.draw.rect(screen,(202,20,30),button5)

    elif button6.collidepoint(click_pos):
        print('button 6 was pressed',Logic.grid[1][1])
        user_set.append(Logic.grid[1][1])
        pygame.draw.rect(screen,(202,20,30),button6)

    elif button7.collidepoint(click_pos):
        print('button 7 was pressed',Logic.grid[1][2])
        user_set.append(Logic.grid[1][2])
        pygame.draw.rect(screen,(202,20,30),button7)

    elif button8.collidepoint(click_pos):
        print('button 8 was pressed',Logic.grid[1][3])
        user_set.append(Logic.grid[1][3])
        pygame.draw.rect(screen,(202,20,30),button8)

    elif button9.collidepoint(click_pos):
        print('button 9 was pressed',Logic.grid[2][0])
        user_set.append(Logic.grid[2][0])
        pygame.draw.rect(screen,(202,20,30),button9)

    elif button10.collidepoint(click_pos):
        print('button 10 was pressed',Logic.grid[2][1])
        user_set.append(Logic.grid[2][1])
        pygame.draw.rect(screen,(202,20,30),button10)

    elif button11.collidepoint(click_pos):
        print('button 11 was pressed',Logic.grid[2][2])
        user_set.append(Logic.grid[2][2])
        pygame.draw.rect(screen,(202,20,30),button11)

    elif button12.collidepoint(click_pos):
        print('button 12 was pressed',Logic.grid[2][3])
        user_set.append(Logic.grid[2][3])
        pygame.draw.rect(screen,(202,20,30),button12)

    elif button13.collidepoint(click_pos):
        print('button 13 was pressed',Logic.grid[3][0])
        user_set.append(Logic.grid[3][0])
        pygame.draw.rect(screen,(202,20,30),button13)

    elif button14.collidepoint(click_pos):
        print('button 14 was pressed',Logic.grid[3][1])
        user_set.append(Logic.grid[3][1])
        pygame.draw.rect(screen,(202,20,30),button14)

    elif button15.collidepoint(click_pos):
        print('button 15 was pressed',Logic.grid[3][2])
        user_set.append(Logic.grid[3][2])
        pygame.draw.rect(screen,(202,20,30),button15)

    elif button16.collidepoint(click_pos):
        print('button 16 was pressed',Logic.grid[3][3])
        user_set.append(Logic.grid[3][3])
        pygame.draw.rect(screen,(202,20,30),button16)

    pygame.display.flip()
    pygame.time.delay(100)
    # print("user_set:",user_set)

def Button_border(click_pos):
    if button1.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button1)                
        pygame.display.update()
    elif button2.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button2)                
        pygame.display.update()
    elif button3.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button3)                
        pygame.display.update()
    elif button4.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button4)                
        pygame.display.update()
    elif button5.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button5)                
        pygame.display.update()
    elif button6.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button6)                
        pygame.display.update()
    elif button7.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button7)                
        pygame.display.update()
    elif button8.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button8)                
        pygame.display.update()
    elif button9.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button9)                
        pygame.display.update()
    elif button10.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button10)                
        pygame.display.update()
    elif button11.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button11)                
        pygame.display.update()
    elif button12.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button12)                
        pygame.display.update()
    elif button13.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button13)                
        pygame.display.update()
    elif button14.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button14)                
        pygame.display.update()
    elif button15.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button15)                
        pygame.display.update()
    elif button16.collidepoint(click_pos):
        
        pygame.draw.rect(screen,(202,20,30),Button16)                
        pygame.display.update()

main()