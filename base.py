import pygame

rsl = (640,480)

class CBase:

	def __init__(self, frame_per_sec = 10):
		
		self.__frame_per_sec = frame_per_sec
		self.cur_shot = 0

	def do_shot(self, main_surf):

		print("[Переопределить метод]")

	def completion(self, main_surf):

		return False # Заглушка, метод переопределяется в дочерних классах там, где нужно

	def main_loop(self, main_surf):
		
		clock = pygame.time.Clock()

		ret = None

		while ret == None:

			clock.tick(self.__frame_per_sec)

			if pygame.K_ESCAPE in map(lambda ev: ev.key, pygame.event.get(pygame.KEYDOWN)):

				ret = False

			elif self.do_shot(main_surf):
				
				pygame.display.flip()

			else:

				ret = True

		while self.completion(main_surf):

			clock.tick(self.__frame_per_sec)
			pygame.display.flip()

		main_surf.fill((0,0,0))

		return ret

class CStr:

		def __init__(self, str, font_size,
				font_name = "monotype", font_color = (255,255,255), pos = None, only = False):

			self.__only = only
			self.str = str
			self.len = len(str)
			self.font_color = font_color

			self.fsize = font_size

			font = pygame.font.Font(pygame.font.match_font(font_name),self.fsize)

			if self.__only == True:
				self.surf = font.render(self.str,True,self.font_color,(0,0,0))
				self.height = self.surf.get_rect().height
				self.width = self.surf.get_rect().width
			else:
				self.surf = []
				for x in range(0, self.len):
					self.surf.append(font.render(self.str[x],True,self.font_color,(0,0,0)))
				self.height = self.surf[0].get_rect().height
				self.width = self.surf[0].get_rect().width * self.len

			if pos == None:
				pos = ((rsl[0] - self.width) / 2, (rsl[1] - self.height) / 2)

			self.set_pos(pos)

		def set_pos(self, pos):

			self.pos = pos
			self.rect = pygame.Rect(self.pos,(self.width, self.height))

		def draw(self, main_surf, x = 0):
			
			if self.__only == True:

				main_surf.blit(self.surf, self.pos)

			else:

				main_surf.blit(self.surf[x],
						(self.pos[0] + sum(map(lambda x: x.get_width(), self.surf[0 : x])),
							self.pos[1]))

