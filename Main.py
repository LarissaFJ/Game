import pygame
pygame.init()
print ("Setup Start")
window = pygame.display.set_mode((800, 600))
print ("Setup Finish")
print("Loop")
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #close pigame
