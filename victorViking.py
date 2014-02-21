import sys, pygame
pygame.init()

size = width, height = 1200, 700

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Victor The Viking")

white = 255,255,255
grey = 100,100,100
FPS = pygame.time.Clock()

class Victor(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("newvictor.png")
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.leftmoving = self.rightmoving = self.upmoving = self.downmoving = self.onfloorbool = False

	def checkCollide(self):
		if len(pygame.sprite.groupcollide(hero_sprites,floor_tiles,False,False)) > 0:
			self.onfloorbool = True
			print self.onfloorbool
		else:
			print "False"

	def update(self):

		if self.leftmoving == True:
			self.rect = self.rect.move(-5,0)
		if self.rightmoving == True:
			self.rect = self.rect.move(5,0)
		if self.upmoving == True:
			self.rect = self.rect.move(0,-5)
		if self.downmoving == True:
	 		self.rect = self.rect.move (0,5)


class Floor(pygame.sprite.Sprite):
	
	def __init__(self, fileLoc, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(fileLoc)
		self.rect = self.image.get_rect()
		self.rect.topleft = x, y

class Map():
	def __init__(self, fileLoc):
	
		self.lines = []
		self.Mapfile = open(fileLoc)
		for line in self.Mapfile.readlines():
			string = line.strip()
			self.lines.append(string)

		self.Mapfile.close()

# Class Instances
victor = Victor(width/2,height/2)
map1 = Map("map.txt")

# Sprite Groups
hero_sprites = pygame.sprite.RenderPlain((victor))
floor_tiles = pygame.sprite.Group()

# Creates floor tiles at floor Co-ordinates
for x in range(0,len(map1.lines)):
	for y in range(0,len(map1.lines[x])):
		if map1.lines[x][y] == ".":
			floor = Floor("pattern1.png", y*50, x*50)
			floor_tiles.add(floor)
		elif map1.lines[x][y] =="#":
			plant = Floor("plant.png", y*50, x*50)
			floor_tiles.add(plant)

while True:
	
	screen.fill(white)
	floor_tiles.draw(screen)
	victor.checkCollide()
	hero_sprites.update()
	hero_sprites.draw(screen)
	pygame.display.update()
	FPS.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				victor.leftmoving = True
			if event.key == pygame.K_RIGHT:
				victor.rightmoving = True
			if event.key == pygame.K_UP:
				victor.upmoving = True
			if event.key == pygame.K_DOWN:
			 	victor.downmoving = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				victor.leftmoving = False
			if event.key == pygame.K_RIGHT:
				victor.rightmoving = False
			if event.key == pygame.K_UP:
				victor.upmoving = False
			if event.key == pygame.K_DOWN:
			 	victor.downmoving = False