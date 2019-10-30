import pygame


class Character():
    def __init__(self, screen):
        '''
        Инициализирует персонажа и задает его начальные позиции.

        '''

        self.screen = screen

        # Загрузка изображения персонажа и получение прямоугольника.
        self.image = pygame.image.load('person.bmp').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый персонаж появляется в середине экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        '''
        Рисует персонажа в текущей позиции.

        '''
        self.screen.blit(self.image, self.rect)
