#!/home/amv/env/bin/python3
#coding=utf-8

import pygame

class CHello:

	class __CHelloStr:

		def __init__(self, rsl, str, font_size,
				font_name = "monotype", font_color = (255,255,255), pos = None, only = False):
			self.__rsl = rsl
			self.str = str
			self.len = len(str)

			self.fsize = font_size

			font = pygame.font.Font(pygame.font.match_font(font_name),self.fsize)

			if only == True:
				self.surf = font.render(self.str,True,font_color)
				self.height = self.surf.get_rect().height
				self.width = self.surf.get_rect().width
			else:
				self.surf = []
				for x in range(0, self.len):
					self.surf.append(font.render(self.str[x],True,font_color))
				self.height = self.surf[0].get_rect().height
				self.width = self.surf[0].get_rect().width * self.len

			if pos == None:
				pos = ((self.__rsl[0] - self.width) / 2, (self.__rsl[1] - self.height) / 2)

			self.set_pos(pos)

		def set_pos(self, pos):
			self.pos = pos
			self.rect = pygame.Rect(self.pos,(self.width, self.height))

		def symbol_pos_x(self, x):
				return (self.pos[0] + x * self.fsize / 2, self.pos[1])

	class __CHelloMatrix(pygame.sprite.Sprite):

		def __init__(self, rsl, num):
			pygame.sprite.Sprite.__init__(self)

			self.__rsl = rsl
			self.__num = num

			self.__surf = []
			for x in range(0, self.__num):
				self.__surf.append(pygame.image.load("image/matrix/m" + str(x) + ".png"))

			self.__clear_surf = self.__surf[0].copy()
			self.__clear_surf.fill((0,0,0))
			
			self.rect = self.__surf[0].get_rect()
			self.pos = (
					(self.__rsl[0] - self.__surf[0].get_width()) / 2,
					(self.__rsl[1] - self.__surf[0].get_height()) / 2)
			self.rect = pygame.Rect(self.pos, (self.rect.width, self.rect.height))

			self.image = self.__surf[0]

			self.__cur_shot = 0

		def update(self, *args):
			if args[0] == 0:
				self.__cur_shot = self.__cur_shot + 1
				self.image = self.__surf[self.__cur_shot]
			else:
				self.image = self.__clear_surf

	def __init__(self, rsl):

		self.__shot = 0
		self.__rsl = rsl

		self.__name = self.__CHelloStr(self.__rsl, "Verzhak",36)
		self.__pres = self.__CHelloStr(self.__rsl, "presented:",14)
		self.__pres.set_pos((self.__pres.pos[0], self.__pres.pos[1] + self.__name.height / 2))
		self.__date = self.__CHelloStr(self.__rsl, "(02.08.2009)",14,only = True) # TODO - исправить
		self.__date.set_pos((self.__rsl[0] - self.__date.width, self.__rsl[1] - self.__date.fsize - 3))
		self.__matrix_num = 8
		self.__matrix = pygame.sprite.Group([self.__CHelloMatrix(rsl, self.__matrix_num)])

	def __do_shot(self, main_surf):

		if 0 < self.__shot < (self.__name.len + 1):
			main_surf.fill(main_surf.get_at((0,0)), rect = self.__name.rect)
			for x in range(0,self.__shot):
				main_surf.blit(self.__name.surf[x], self.__name.symbol_pos_x(x))

		elif self.__shot < (self.__name.len + self.__pres.len + 1):
			main_surf.fill(main_surf.get_at((0,0)), rect = self.__pres.rect)

			for x in range(0,self.__shot - self.__name.len):
				main_surf.blit(self.__pres.surf[x],self.__pres.symbol_pos_x(x))

		elif self.__shot < (self.__name.len + self.__pres.len +15):
			main_surf.blit(main_surf,(0, - self.__rsl[1] / 30))

		elif (self.__name.len + self.__pres.len + 15) == self.__shot:
			main_surf.blit(self.__date.surf, self.__date.pos)
			self.__matrix.draw(main_surf)

		elif self.__shot < (self.__name.len + self.__pres.len + 15 + 11):
			pass

		elif self.__shot == (self.__name.len + self.__pres.len + 15 + 11):
			main_surf.fill((0,0,0))
			self.__matrix.draw(main_surf)

		elif self.__shot < (self.__name.len + self.__pres.len + 15 + self.__matrix_num + 11):
			self.__matrix.update(1)
			self.__matrix.draw(main_surf)
			self.__matrix.update(0)
			self.__matrix.draw(main_surf)

		else:
			return None

		self.__shot = self.__shot + 1

		return main_surf

	def main_loop(self, main_surf):

		event_type = pygame.USEREVENT + 1
		pygame.time.set_timer(event_type,100)

		run = 1
		while run == 1:
			event = pygame.event.poll()
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_ESCAPE:
					run = 0
			elif event.type == event_type:
				temp_surf = self.__do_shot(main_surf.copy())
				if temp_surf == None:
					run = 0
					main_surf.fill((0,0,0))
				else:
					main_surf.blit(temp_surf, (0,0))
				pygame.display.flip()

