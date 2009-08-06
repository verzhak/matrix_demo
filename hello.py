import pygame

from base import CBase, CStr, rsl

class CHello(CBase):

	class __CHelloMatrix(pygame.sprite.Sprite):

		def __init__(self, num):

			pygame.sprite.Sprite.__init__(self)

			self.__num = num

			self.__surf = []
			for x in range(0, self.__num):
				self.__surf.append(pygame.image.load("image/matrix/m" + str(x) + ".png"))

			self.__clear_surf = self.__surf[0].copy()
			self.__clear_surf.fill((0,0,0))
			
			self.rect = self.__surf[0].get_rect()
			self.pos = (
					(rsl[0] - self.__surf[0].get_width()) / 2,
					(rsl[1] - self.__surf[0].get_height()) / 2)
			self.rect = pygame.Rect(self.pos, (self.rect.width, self.rect.height))

			self.__next_surf = 0
			self.image = self.__surf[self.__next_surf]

		def update(self, *args):

			if args[0] == 0:
				self.__next_surf = self.__next_surf + 1
				self.image = self.__surf[self.__next_surf]
			else:
				self.image = self.__clear_surf

	def __init__(self):

		CBase.__init__(self)

		self.__shot = 0

		self.__name = CStr("Verzhak",36)
		self.__pres = CStr("presented:",14)
		self.__pres.set_pos((self.__pres.pos[0], self.__pres.pos[1] + self.__name.height / 2))
		self.__date = CStr("(06.08.2009)",14,only = True)
		self.__date.set_pos((rsl[0] - self.__date.width, rsl[1] - self.__date.fsize - 3))
		self.__matrix_num = 8
		self.__matrix = pygame.sprite.Group([self.__CHelloMatrix(self.__matrix_num)])

	def do_shot(self, main_surf):

		if self.__shot == 0:

			pass
		
		elif self.__shot < (self.__name.len + 1):
			
			self.__name.draw(main_surf, self.__shot - 1)

		elif self.__shot < (self.__name.len + self.__pres.len + 1):

			self.__pres.draw(main_surf, self.__shot - self.__name.len - 1)

		elif self.__shot < (self.__name.len + self.__pres.len +15):

			main_surf.blit(main_surf,(0, - rsl[1] / 30))

		elif (self.__name.len + self.__pres.len + 15) == self.__shot:

			self.__date.draw(main_surf)
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

			return False

		self.__shot = self.__shot + 1

		return True

