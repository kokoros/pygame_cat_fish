#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import pygame,sys,time
from pygame.locals import *

class Screen:
	def __init__(self,size=(800,800)):
		'''设置窗口大小和标题'''
		pygame.init()
		self.size = size
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption('为了守护主子的笑容--智障自动叉鱼!可以把键盘丢掉~')
		self.myfont = pygame.font.Font('华文行楷.ttf',30)

	def img_1(self):
		first_image = 'IMG_1.jpg'
		background = pygame.image.load(first_image)
		first_image_last = pygame.transform.smoothscale(background,self.size)	
		self.screen.blit(first_image_last,(0,0))
		pygame.display.update()

	def img_2(self):
		'''在屁股上放画面'''
		second_image = 'IMG_2.png'
		img2 = pygame.image.load(second_image)
		self.screen.blit(img2,(400,200))

	def start_background(self):
		'''放游戏背景图'''
		background_image = 'img_3.png'
		img3 = pygame.image.load(background_image)
		self.screen.blit(img3,(0,0))
		# pygame.display.update()

	def mouse_start(self):
		'''判断鼠标在不在屁股上'''
		global flag1,flag2
		mouse_pos = pygame.mouse.get_pos()
		mouse_button = pygame.mouse.get_pressed()
		if flag1:
			if 400 < mouse_pos[0] < 600 and 300 < mouse_pos[1] < 400 :
				self.img_2()
				txt1 = self.myfont.render('来都来了,点一下屁股试试=w=',True,(255,160,122))
				self.screen.blit(txt1,(200,400))
				pygame.display.update()
				if mouse_button[0]:
					flag1 = False
					self.start_background()
					self.tip()
					flag2 = True

	def tip(self):
		'''提示'''
		txt0 = self.myfont.render('鼠标操纵方向',True,(255,160,122))
		self.screen.blit(txt0,(300,300))
		pygame.display.update()
		time.sleep(2)
		self.start_background()
		txt1 = self.myfont.render('为了主子,努力叉鱼',True,(255,160,122))
		self.screen.blit(txt1,(250,300))
		pygame.display.update()
		time.sleep(3)
		self.start_background()
		txt2 = self.myfont.render('3',True,(255,160,122))
		self.screen.blit(txt2,(400,300))
		pygame.display.update()
		time.sleep(1)
		self.start_background()
		txt3 = self.myfont.render('2',True,(255,160,122))
		self.screen.blit(txt3,(400,300))
		pygame.display.update()
		time.sleep(1)
		self.start_background()
		txt4 = self.myfont.render('1',True,(255,160,122))
		self.screen.blit(txt4,(400,300))
		pygame.display.update()
		time.sleep(1)
		self.start_background()
		txt5 = self.myfont.render('游戏开始',True,(255,160,122))
		self.screen.blit(txt5,(350,300))
		pygame.display.update()	
		time.sleep(1)
		self.start_background()

	def arrow(self):
		'''放箭'''	
		# clock.tick(500)
		
		global y,score
		mouse_pos = pygame.mouse.get_pos()
		import random
		a = random.randint(100,450)
		b = random.randint(0,400)
		fish = pygame.image.load('img_4.png')
		fish_rect = pygame.Rect(a,b,300,100)
		arrow = pygame.image.load('arrow.png')
		arrow_rect = pygame.Rect(mouse_pos[0], y, 50, 200)	
		y -= 30
		if y < 0:
			y = 600
		x = mouse_pos[0]
		self.start_background()
		self.screen.blit(fish,fish_rect)
		self.screen.blit(arrow,arrow_rect)
		pygame.display.update()
		time.sleep(0.05)
		if arrow_rect.colliderect(fish_rect):
			txt7 = self.myfont.render('叉到鱼了～喜+1',True,(255,160,122))
			y = 0
			score += 1
			score_txt = self.myfont.render('已叉鱼数:%d' % score,True,(255,160,122),(255,240,255))
			self.screen.blit(score_txt,(0,0))
			self.screen.blit(txt7,(250,300))
			pygame.display.update()
			time.sleep(2)
			if score == 5:
				self.score('主子表示还要吃~','cat_1.jpg',(600,800),(100,0))
			elif score == 10:
				self.score('主子表示很满意~','cat_2.jpg',(600,800),(100,0))
			elif score == 15:
				self.score('主子吃饱了~','cat_3.jpg',(800,800),(0,0))

				
	def score(self,txt,image,size,bilt_):
		score_1 = self.myfont.render(txt,True,(255,160,122))
		cat_1 = pygame.image.load(image)
		image_last = pygame.transform.smoothscale(cat_1,size)
		self.screen.blit(image_last, bilt_)
		self.screen.blit(score_1, (250,50))
		pygame.display.update()
		time.sleep(3)

# clock = pygame.time.Clock()
flag1 = True
flag2 = False
y = 600
score = 0

def main():	
	'''运行的主程序'''
	flag = True
	
	screen = Screen()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if flag:
				screen.img_1()
				flag = False
			if flag1:
				screen.mouse_start()

		if flag2:
			screen.arrow()

			
			





		# screen.arrow()
		
		
		
		# if flag:
		# 	screen.img_1()
			
		# 	flag = False
		# else:
		# 	screen.mouse_start()
		
			
			
		# screen.cat()
		# screen.move_fish()
			# screen.start_background()



		# screen.start_background()
		# pygame.display.update()

main()








