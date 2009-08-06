import pygame
from random import randint
from base import CBase, rsl

class CEnc(CBase):

	def __init__(self):

		CBase.__init__(self)

		self.__font = pygame.font.Font("fonts/enc.ttf",24)

		self.__sg = [ord("A"), ord("z")] # Symbol (generation) guard
		self.__prob = [-50, 20, -10]
		self.__step = 14

		self.__line = []
		for x in range(0, rsl[0] // self.__step):
			self.__line.append(randint(self.__prob[0], self.__prob[1]))

		self.__num_compl_shots = rsl[1] // 20

	def completion(self, main_surf):

		if self.__num_compl_shots > 0:

			main_surf.blit(main_surf, ((0, 20), (rsl[0], rsl[1] - 20)))
			main_surf.fill((0,0,0), ((0,0), (rsl[0], 20)))

		elif self.__num_compl_shots == 0:

			main_surf.blit(pygame.image.load("image/thats_all_folks.jpg"), (0,0))

		elif self.__num_compl_shots < -20:

			return False

		self.__num_compl_shots = self.__num_compl_shots - 1

		return True

	def do_shot(self, main_surf):

		main_surf.blit(main_surf, ((0, 20), (rsl[0], rsl[1] - 20)))
		main_surf.fill((0,0,0), ((0,0), (rsl[0], 20)))

		for x in range(0, len(self.__line)):
			
			if self.__line[x] > 0:
			
				sym_s = self.__font.render(chr(randint(self.__sg[0], self.__sg[1])),True, (30, 189, 4))
				main_surf.blit(sym_s, ((x * self.__step, 0), (sym_s.get_width(), sym_s.get_height())))

			elif self.__line[x] < self.__prob[2]:

				self.__line[x] = randint(self.__prob[0], self.__prob[1])

			self.__line[x] = self.__line[x] - 1

		return True

