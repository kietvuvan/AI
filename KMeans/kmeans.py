import pygame
from random import*
import math
from sklearn.cluster import*
pygame.init()

# distance of two points
def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

screen=pygame.display.set_mode((800,500))
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

#Font,text
font=pygame.font.SysFont('sanst',20)
font_small=pygame.font.SysFont('sanst',15)
text_plus=font.render('+',True,white)
text_minus=font.render('-',True,white)
text_run=font.render("RUN",True,black)
text_random=font.render('RAMDOM',True,white)
text_alogrithm=font.render('ALOGRITHM',True,white)
text_reset=font.render('RESET',True,yellow)
text_topic=font.render('KMEANS CLUSTERING',True,red)
K=0
loss_function=0
point_of_list=[]
clusters=[]
labels=[]
while running:
	clock.tick(60)  #60 frames on every second
	screen.fill(background)
	mouse_x, mouse_y=pygame.mouse.get_pos()
	# Draw interface
	# Draw panel
	pygame.draw.rect(screen,black,(50,50,500,350))
	pygame.draw.rect(screen,background_panel,(55,55,490,340))
	# Draw K button (+)
	pygame.draw.rect(screen,black,(600,50,30,30))
	screen.blit(text_plus,(605,45))
	#daw K buton (-)
	pygame.draw.rect(screen,black,(650,50,30,30))
	screen.blit(text_minus,(660,45))
	#daw K value
	text_K=font.render("K="+str(K),True,black)	
	screen.blit(text_K,(700,55))
	# draw RUN
	pygame.draw.rect(screen,blue,(600,100,80,30))
	screen.blit(text_run,(600,105))
	# draw RANDOM
	pygame.draw.rect(screen,black,(600,150,100,30))
	screen.blit(text_random,(600,155))
	#draw ALOGRITHM
	pygame.draw.rect(screen,black,(600,200,150,30))
	screen.blit(text_alogrithm,(600,205))
	# Draw TEXT_TOPIC
	pygame.draw.rect(screen,black,(250,420,150,30))
	screen.blit(text_topic,(250,425))
	# Draw RESET
	pygame.draw.rect(screen,black,(600,300,100,30))
	screen.blit(text_reset,(600,305))
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
			if 600<mouse_x<630 and 50<mouse_y<80:
				if(K<7):
					K=K+1
			#click K button (-)
			if 650<mouse_x<680 and 50<mouse_y<80:
				if(K>0):
					K=K-1
					
			#click RUN running alorithm without library
			if 600<mouse_x<680 and 100<mouse_y<130:
				labels=[]
				if clusters==[]:
					break

				# create lables for center points (clusters)
				for p in point_of_list:
					distances=[]
					for c in clusters:
						dis_point_to_center_point=distance(p,c)
						distances.append(dis_point_to_center_point)
					# the min of distance all center points to one  point		
					min_distance=min(distances)
					label=distances.index(min_distance)
					labels.append(label)

				# change center points = computed mean of all point of a label
				#-- clusters_x=()
				for i in range(K):
					sum_x_of_points=0
					sum_y_of_points=0
					count=0;
					for j in range(len(point_of_list)):
						if labels[j]==i:
							sum_x_of_points=sum_x_of_points+point_of_list[j][0]
							sum_y_of_points=sum_y_of_points+point_of_list[j][1]
							count=count+1;
					if count>0:
						new_center_point_x=(sum_x_of_points/count)
						new_center_point_y=(sum_y_of_points/count)
						clusters[i]=[new_center_point_x,new_center_point_y]

				print("RUN") #test click in Button RUN
			#click RANDOM
			if 600<mouse_x<700 and 150<mouse_y<180:
				labels=[]
				clusters=[]
				for i in range(K):
					random_centrer_point=[randint(0,500),randint(0,350)]
					clusters.append(random_centrer_point)
				print("RANDOM") # check click in RANDOm button
			#click ALOGRITHM
			if 600<mouse_x<750 and 200<mouse_y<230:
				if K==0:
					break
				kmeans=KMeans(n_clusters=K).fit(point_of_list)
				clusters=kmeans.cluster_centers_
				labels=kmeans.predict(point_of_list)

				print("ALOGRITHM") # check click in ALO button
			#click RESET
			if 600<mouse_x<700 and 300<mouse_y<330:
				K=0
				loss_function=0
				point_of_list=[]
				clusters=[]
				labels=[]
				print("RESET")	
			# click panel
			if(50<mouse_x<550 and 50<mouse_y<400):
				labels=[]
				point=[mouse_x-50,mouse_y-50]
				point_of_list.append(point)
	
	# Draw points
	if labels==[]:	
		for i in range(len(point_of_list)):
			pygame.draw.circle(screen,black,(point_of_list[i][0]+50,point_of_list[i][1]+50),3)
			pygame.draw.circle(screen,white,(point_of_list[i][0]+50,point_of_list[i][1]+50),2)
	else:
		for i in range(len(point_of_list)):
			pygame.draw.circle(screen,COLORS[labels[i]],(point_of_list[i][0]+50,point_of_list[i][1]+50),3)

	# Draw center point
	for i in range(len(clusters)):
		pygame.draw.circle(screen,COLORS[i],(int(clusters[i][0])+50,int(clusters[i][1])+50),5)

	# Draw Loss Function
	loss_function=0
	if clusters !=[] and labels !=[]:
		for i in range(len(point_of_list)):
			loss_function+=distance(point_of_list[i],clusters[labels[i]])

	#Loss Function TEXT
	text_loss_function=font.render("LossFunc="+str(int(loss_function)),True,red)	
	screen.blit(text_loss_function,(600,250))

	pygame.display.flip()			
			
pygame.quit()