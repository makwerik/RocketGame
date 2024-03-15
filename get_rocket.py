import pygame

class GetRocket:
    def __init__(self, ai_game):
        """Задаем начальнуб позицию ракете"""
        self.screen = ai_game.screen

        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Загружаем ракету"""
        self.image = pygame.image.load('img/picture.bmp')
        self.rect = self.image.get_rect()

        """Каждая новая ракета появляется у нижнего края экрана"""
        self.rect.midbottom = self.screen_rect.midbottom


        """Для ограничения ракеты"""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        """Перемещение"""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляем позициб ракеты с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        """Чтобы ракета не стояла на месте"""
        self.rect.x = self.x
        self.rect.y = self.y





    def bltime(self):
        """Рисуем ракету"""
        self.screen.blit(self.image, self.rect)