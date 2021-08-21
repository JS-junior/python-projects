import pygame
pygame.init()

running = True

screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Hello world')

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	screen.fill((255,255,255))
	pygame.display.update()