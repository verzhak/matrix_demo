import pygame
from random import randint
from base import CBase, rsl

class CEnc(CBase):

	def __init__(self, main_surf):

		CBase.__init__(self, main_surf)

		self.__font = pygame.font.Font("fonts/enc.ttf",24)

		first_sym = ord("A")
		self.__sg = ord("z") - first_sym # Symbol (generation) guard
		self.__surf = []
		for x in range(0, self.__sg + 1):
			self.__surf.append(self.__font.render(chr(first_sym + x) ,True, (30, 189, 4)))

		self.__prob = [-50, 20, -10]
		self.__step = 14

		self.__line = []
		for x in range(0, rsl[0] // self.__step):
			self.__line.append(randint(self.__prob[0], self.__prob[1]))

		self.__num_compl_shots = rsl[1] // 20

	def completion(self):

		if self.__num_compl_shots > 0:

			self.main_surf.blit(self.main_surf, ((0, 20), (rsl[0], rsl[1] - 20)))
			self.main_surf.fill((0,0,0), ((0,0), (rsl[0], 20)))

		elif self.__num_compl_shots == 0:

			self.main_surf.blit(pygame.image.load("image/thats_all_folks.jpg"), (0,0))

		elif self.__num_compl_shots < -20:

			return False

		self.__num_compl_shots = self.__num_compl_shots - 1

		return True

	def do_shot(self):

		self.main_surf.blit(self.main_surf, ((0, 20), (rsl[0], rsl[1] - 20)))
		self.main_surf.fill((0,0,0), ((0,0), (rsl[0], 20)))

		for num, x in enumerate(self.__line):
			
			if x > 0:

				y = randint(0, self.__sg)
				self.main_surf.blit(self.__surf[y], ((num * self.__step, 0),
									(self.__surf[y].get_width(),self.__surf[y].get_height())))

			elif x < self.__prob[2]:

				self.__line[num] = randint(self.__prob[0], self.__prob[1])

			self.__line[num] = self.__line[num] - 1

		return True

