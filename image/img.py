import pygame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import cv2
import matplotlib.backends.backend_agg as agg
import pylab
import matplotlib
matplotlib.use("Agg")
from pygame.locals import *
pygame.init()




fig = pylab.figure(figsize=[5, 5], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()


	

#add

#window = pygame.display.set_mode((600, 400), DOUBLEBUF)






screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Kmeans")
running=True
clock=pygame.time.Clock() # create frame per second
#COLOR
background=(214,214,214)  #RGB
black=(0,0,0)
red=(255,0,0)
background_panel=(249,255,230)
white=(255,255,255)
lime=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
cyan=(0,255,255)
magenta=(255,0,255)
green=(0,128,0)
salmon=(250,128,114)
COLORS=[black,lime,blue,salmon,cyan,magenta,red]


screen1 = pygame.display.get_surface()

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen1.blit(surf, (10,10))





#Font,text
font=pygame.font.SysFont('sanst',20)
font_small=pygame.font.SysFont('sanst',15)
text_plus=font.render('+',True,white)
text_minus=font.render('-',True,white)
text_run=font.render("UPLOAD",True,black)
text_random=font.render('RAMDOM',True,white)
text_alogrithm=font.render('ALOGRITHM',True,white)
text_reset=font.render('RESET',True,yellow)
K=0

while running:
	clock.tick(60)  #60 frames on every second
	screen.fill(background)
	mouse_x, mouse_y=pygame.mouse.get_pos()
	# Draw interface
	# Draw panel before
	pygame.draw.rect(screen,black,(10,10,500,500))
	pygame.draw.rect(screen,background_panel,(15,15,490,490))
	# Draw panel after
	pygame.draw.rect(screen,black,(550,10,500,500))
	pygame.draw.rect(screen,background_panel,(555,15,490,490))
	# Draw K button (+)
	pygame.draw.rect(screen,black,(1060,50,30,30))
	screen.blit(text_plus,(1065,55))
	#daw K buton (-)
	pygame.draw.rect(screen,black,(1100,50,30,30))
	screen.blit(text_minus,(1120,55))
	#daw K value
	text_K=font.render("K="+str(K),True,black)	
	screen.blit(text_K,(1150,55))
	# draw RUN
	pygame.draw.rect(screen,blue,(1060,100,80,30))
	screen.blit(text_run,(1060,105))
	# draw RANDOM
	pygame.draw.rect(screen,black,(1060,150,100,30))
	screen.blit(text_random,(1060,155))
	#draw ALOGRITHM
	pygame.draw.rect(screen,black,(1060,200,100,30))
	screen.blit(text_alogrithm,(1060,205))
	
	# Draw RESET
	pygame.draw.rect(screen,black,(1060,300,100,30))
	screen.blit(text_reset,(1060,305))
	# Draw mouse possion
	if(50<mouse_x<550 and 50<mouse_y<400):
		text_mouse=font_small.render("("+str(mouse_x-50)+","+str(mouse_y-50)+")",True,red)
		screen.blit(text_mouse,(mouse_x+15,mouse_y))
	# End draw interface

	


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			#click K button(+)
			if 1060<mouse_x<1110 and 50<mouse_y<80:
				if(K<7):
					K=K+1
					print("K+") # testing click K+
			#click K button (-)
			if 1110<mouse_x<1150 and 50<mouse_y<80:
				if(K>0):
					K=K-1
					print("K-") # testing click K-
			#click RUN running alorithm without library
			if 1060<mouse_x<1140 and 100<mouse_y<130:
				
				
				print("RUN") #test click in Button RUN
			#click RANDOM
			if 600<mouse_x<700 and 150<mouse_y<180:
				
				print("RANDOM") # check click in RANDOm button
			#click ALOGRITHM
			

				print("ALOGRITHM") # check click in ALO button
			#click RESET
			if 600<mouse_x<700 and 300<mouse_y<330:
				
				print("RESET")	
			
	
	
	
	
	pygame.display.flip()			
			
pygame.quit()
