import pygame
from base import CBase, CStr, rsl

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

				self.__surf_loop = 0
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
				
				self.rect.x = self.rect.x + args[1]

			else:

				self.image = self.__surf[0]

				self.rect.x = 10
				self.rect.y = self.rect.y + args[1]

	class __CKnock(pygame.sprite.Sprite):

		def __init__(self):

			pygame.sprite.Sprite.__init__(self)

			self.__surf = []
			for x in range(1,7):
				self.__surf.append(pygame.image.load("image/knock/k" + str(x) + ".png"))
			self.__clear_surf = self.__surf[0].copy()
			self.__clear_surf.fill((0,0,0))

			self.__surf_loop = 0
			self.image = self.__surf[0]

			self.rect = pygame.Rect((0,0),
					(self.image.get_width(), self.image.get_height()))
			self.__set_rect((-100,-50))

		def __set_rect(self, dis):

			self.rect.x = (rsl[0] - self.rect.width) / 2 + dis[0]
			self.rect.y = (rsl[1] - self.rect.height) / 2 + dis[1]

		def update(self, *args):

			if self.__surf_loop % 2 == 0:

				real_loop = self.__surf_loop // 2

				if args[0] == 0:

					if real_loop < 6:

						self.image = self.__surf[real_loop]

					elif real_loop > 6:

						self.image = self.__surf[real_loop - 6]

					else:

						self.__set_rect((100, 50))
						self.image = self.__surf[0]

				elif (args[0] == -1) and (real_loop != 6):

					self.image = self.__clear_surf

			if args[0] == 0:

				self.__surf_loop = self.__surf_loop + 1

	def __init__(self):
		
		CBase.__init__(self)

		self.__wakeup = CStr("Wake up, Neo!", 22, font_color = (30, 189, 4), pos = (10,10))
		self.__has_you = CStr("The Matrix has you...", 22,
				font_color = (30, 189, 4), pos = (10, self.__wakeup.pos[1] + self.__wakeup.height))
		self.__rabbit = CStr("Follow the white rabbit...", 22,
				font_color = (30, 189, 4), pos = (10,self.__has_you.pos[1] + self.__has_you.height))
		self.__knock_sprite = self.__CKnock()
		self.__knock = pygame.sprite.Group([self.__knock_sprite])

		# 0 - WakeUp+Rabbit+MHY; 1 - Knock,Knock
		self.__cached_region = [(
									range(10, self.__rabbit.rect.width + 40),
									range(10, 10 + self.__wakeup.rect.height +
											self.__has_you.rect.height + self.__rabbit.rect.height)
								),
								(
									range(self.__knock_sprite.rect.x, 570),
									range(self.__knock_sprite.rect.y, 340)
								)]

		self.__cursor = pygame.sprite.Group([self.__CCursor()])

		self.__cur_shot = 0

		self.__cached = [
			(37 + self.__wakeup.len + self.__has_you.len),
			(19 + self.__wakeup.len),
			(18 + self.__wakeup.len),
			(36 + self.__wakeup.len),
			(36 + self.__wakeup.len + self.__has_you.len),
			(74 + self.__wakeup.len + self.__has_you.len + self.__rabbit.len), # 5
			(54 + self.__wakeup.len + self.__has_you.len + self.__rabbit.len),
			(54 + self.__wakeup.len + self.__has_you.len),
			(97 + self.__wakeup.len + self.__has_you.len + self.__rabbit.len), # 8
			(73 + self.__wakeup.len + self.__has_you.len + self.__rabbit.len),
			(101 + self.__wakeup.len + self.__has_you.len + self.__rabbit.len)]

	def __blackout(self, main_surf, reg, step):

		for x in self.__cached_region[reg][0]:

			for y in self.__cached_region[reg][1]:

				tcol = main_surf.get_at((x,y))

				if tcol[1] > step:

					main_surf.set_at((x,y), (tcol[0], tcol[1] - step, tcol[2]))

				elif tcol[1] > 0:

					main_surf.set_at((x,y), (tcol[0], 0, tcol[2]))

	def do_shot(self, main_surf):

		if self.__cur_shot < self.__cached[0]:

			if self.__cur_shot < self.__cached[1]:

				if self.__cur_shot < 18:

					if self.__cur_shot == 17:

						self.__cursor.update(1)

					else:
						
						self.__cursor.update(0)
						
				else:

					self.__cursor.update(-1)
					self.__cursor.draw(main_surf)

					if self.__cur_shot == self.__cached[2]:

						self.__cursor.update(3, self.__wakeup.height)

					else:
						
						self.__wakeup.draw(main_surf, self.__cur_shot - 18)
						self.__cursor.update(2, self.__wakeup.surf[self.__cur_shot - 18].get_width())

			else:
				
				if self.__cur_shot < self.__cached[3]:
			
					self.__cursor.update(0)

				else:

					self.__cursor.update(-1)
					self.__cursor.draw(main_surf)

					if self.__cur_shot == self.__cached[4]:

						self.__cursor.update(3, self.__has_you.height)

					else:

						surf_ind = self.__cur_shot - self.__cached[3]

						self.__has_you.draw(main_surf, surf_ind)
						self.__cursor.update(2, self.__has_you.surf[surf_ind].get_width())

			self.__cursor.draw(main_surf)

		else:
		
			if self.__cur_shot < self.__cached[5]:

				if self.__cur_shot < self.__cached[6]:

					if self.__cur_shot < self.__cached[7]:

						self.__cursor.update(0)

					else:

						surf_ind = self.__cur_shot - self.__cached[7] 

						self.__cursor.update(-1)
						self.__cursor.draw(main_surf)
						self.__rabbit.draw(main_surf,surf_ind)
						self.__cursor.update(2,self.__rabbit.surf[surf_ind].get_width())

					self.__cursor.draw(main_surf)

				else:

					self.__blackout(main_surf, 0, 10)

			else:

				if self.__cur_shot < self.__cached[8]:

					if self.__cur_shot == self.__cached[9]:

						main_surf.fill((0,0,0))

					else:

						self.__knock.update(-1)
						self.__knock.draw(main_surf)
						self.__knock.update(0)
						self.__knock.draw(main_surf)

				else:

					if self.__cur_shot < self.__cached[10]:

						self.__blackout(main_surf, 1, 50)

					else:

						return False

		self.__cur_shot = self.__cur_shot + 1

		return True

