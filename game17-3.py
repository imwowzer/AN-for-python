import pygame,sys
from random import *

#-----ball subclass definition------------------------
class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, location, speed):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed
	
	def move(self):
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]
			
		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = -self.speed[1]


def animate(group):
	screen.fill([255, 255, 255])
#	for ball in group:
#		ball.move()
	for ball in group:
#下蛋start
            group_egg = pygame.sprite.Group()
            location_egg = [ball.rect.left, ball.rect.top]
            speed_egg = [0,0]
            egg = MyBallClass(img_file_egg1,location_egg,speed_egg)
            group_egg.add(egg)
            screen.blit(egg.image, egg.rect)
            pygame.display.flip()
#下蛋end
            group.remove(ball)
            if pygame.sprite.spritecollide(ball, group, False):
                ball.speed[0] = -ball.speed[0]
                ball.speed[1] = -ball.speed[1]
            ball.move()
            group.add(ball)
            screen.blit(ball.image, ball.rect)
                
	pygame.display.flip()
	pygame.time.delay(20)
	
#------Main Program-------------------------------------
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
#img_file = "beach_ball.png"

#选择鸡和出生点
img_file_chick = "chick1.png"
img_file_egg1 = "egg3.png"
#balls = []
group = pygame.sprite.Group()
location = [300,250]
speed = [choice([-2,2]), choice([-2,2])]
ball = MyBallClass(img_file_chick,location,speed)
group.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#	pygame.time.delay(20)
        animate(group)
    """
    screen.fill([255, 255, 255])
    for ball in balls:
    	ball.move()
	screen.blit(ball.image, ball.rect)
	pygame.display.flip()
    """
