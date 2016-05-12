#Valentin Vallejo
#CIS AM
#3/7/16
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (242, 131, 181)

size = (1500, 1000)
screen = pygame.display.set_mode(size)


PI = 3.141592653
screen.fill(WHITE)
done = False
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
rect_x += 5
rect_y += 3
rect_change_x = 5
rect_change_y = 3
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

    for y_offset in range(0, 100, 10):
        #pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

          
        #pygame.draw.circle(screen, WHITE, [750, 500], 200, 10)
        #pygame.draw.line(screen, WHITE, [750, 0], [750, 1000], 10)
        #pygame.draw.line(screen, WHITE, [0, 300 ], [0, 300 ], 10)
      
        pygame.draw.rect(screen, PINK, [rect_x, rect_y, 10, 10])
        rect_x += rect_change_x
        rect_y += rect_change_y
        if rect_x > 1449 or rect_x < 0:
            rect_change_x *= -1
        if rect_y > 949 or rect_y < 0:
            rect_change_y*= -1
             
        font = pygame.font.SysFont('Calibri', 75, True, False)
         
        text = font.render("1-800-SUH-DUDE", True,WHITE)  
        screen.blit(text, [300, 50])      
        screen.blit(text, [300, 100])       
        screen.blit(text, [300, 150])
        screen.blit(text, [300, 200])
        screen.blit(text, [300, 250])
        screen.blit(text, [300, 300])       
        screen.blit(text, [300, 350])               
        screen.blit(text, [300, 400])       
        screen.blit(text, [300, 450])
        screen.blit(text, [300, 500])       
        screen.blit(text, [300, 550])      
        screen.blit(text, [300, 600])
        screen.blit(text, [300, 650])
        screen.blit(text, [300, 700])
        screen.blit(text, [300, 750])
        screen.blit(text, [300, 800])
        screen.blit(text, [300, 850])
        screen.blit(text, [300, 900])
         
        pygame.display.flip()
          
        clock.tick(1000)
                     
pygame.quit()
