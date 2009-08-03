#!/home/amv/env/bin/python3
#coding=utf-8

import pygame
from base import CBase, CStr

class CConsole(CBase):

	class __CCursor(pygame.sprite.Sprite):

		def __init__(self):

			pygame.sprite.Sprite.__init__(self)

			self.__surf = []
			for x in range(0,3):
				self.__surf.append(pygame.image.load("image/cursor/c" + str(x) + ".png"))
			self.__surf.append(self.__surf[0].copy())
			self.__surf[3].fill((0,0,0))

			self.__surf_loop = 2
			self.image = self.__surf[2]

			self.rect = pygame.Rect((10,10),
					(self.__surf[0].get_width(), self.__surf[0].get_height()))

		def update(self, *args):

			if args[0] == -1:

				self.image = self.__surf[3]

			elif args[0] == 0:

				self.__surf_loop = self.__surf_loop + 1

				if self.__surf_loop < 4:
					
					self.image = self.__surf[self.__surf_loop]

				elif self.__surf_loop > 6:

					self.__surf_loop = 0
					self.image = self.__surf[0]

			elif args[0] == 1:

				self.image = self.__surf[0]

			elif args[0] == 2:

				self.image = self.__surf[0]
				
				#self.rect.x = self.rect.x + self.__step_x
				#self.rect.x = self.rect.x + 12
				self.rect.x = self.rect.x + args[1]

			else:

				self.image = self.__surf[0]

				self.rect.x = 10
				#self.rect.y = self.rect.y + self.__step_y
				self.rect.y = self.rect.y + 22
			
	def __init__(self, rsl):
		
		CBase.__init__(self, 2)

		self.__rsl = rsl

		self.__wakeup = CStr(rsl, "Wake up, Neo!", 22, font_color = (30, 189, 4), pos = (10,10))
		self.__has_you = CStr(rsl, "The Matrix has you...", 14,
				font_color = (30, 189, 4), pos = (10,25))
		self.__rabbit = CStr(rsl, "Follow the white rabbit...", 14,
				font_color = (30, 189, 4), pos = (10,40))
		self.__knock = CStr(rsl, "KNOCK, KNOCK", 32, font_color = (30, 189, 4))

		self.__cursor = pygame.sprite.Group([self.__CCursor()])

		self.__cur_shot = 0

	def do_shot(self, main_surf):

		if self.__cur_shot < 17:
			
			self.__cursor.update(0)
			self.__cursor.draw(main_surf)

		elif self.__cur_shot == 17:

			self.__cursor.update(1)
			self.__cursor.draw(main_surf)

		elif self.__cur_shot < (17 + self.__wakeup.len + 1):

			self.__cursor.update(-1)
			self.__cursor.draw(main_surf)
			self.__wakeup.draw(main_surf, self.__cur_shot - 18)
			self.__cursor.update(2, self.__wakeup.surf[self.__cur_shot - 18].get_width())
			self.__cursor.draw(main_surf)

		# TODO

		self.__cur_shot = self.__cur_shot + 1

		return main_surf

