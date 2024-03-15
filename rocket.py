import sys

import pygame
from settings import Settings
from get_rocket import GetRocket


class Rocket:
    def __init__(self):
        """Иннициализирую pygame, окно игры, название и т.д"""

        pygame.init()

        """Настройки игры"""
        self.settings = Settings()

        """Игра будет у нас на весь экран"""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # # self.settings.screen_width = self.screen.get_rect().width
        # # self.settings.screen_height = self.screen.get_rect().height

        """Задаем название окна"""
        pygame.display.set_caption(self.settings.name_window)

        """Импортируем ракету"""
        self.get_rocket = GetRocket(self)

    def run(self):
        """Запуск игры"""
        while True:
            self._check_events()
            self.get_rocket.update()
            self._update_screen()

    def _update_screen(self):
        """Обновление экрана"""

        """Цвет экрана"""
        self.screen.fill(self.settings.bg_color)

        """Рисую ракету"""
        self.get_rocket.bltime()
        """Стираю старый экран, рисую новый"""
        pygame.display.flip()

    def _check_events(self):
        """Отслеживаю события с экрана"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.QUIT:
                print("Закрываю игру")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Отслеживаю события нажатия клавиш"""
        if event.key == pygame.K_q:
            print("Закрываю игру")
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.get_rocket.moving_right = True
            print('Нажали правую клавишу')
        elif event.key == pygame.K_LEFT:
            self.get_rocket.moving_left = True
            print('Нажали левую клавишу')
        elif event.key == pygame.K_UP:
            self.get_rocket.moving_up = True
            print('Нажали клавишу вверх')
        elif event.key == pygame.K_DOWN:
            self.get_rocket.moving_down = True
            print('Нажали клавишу вниз')


    def _check_keyup_events(self, event):
        """Отслеживаю события отпускания клавиш"""
        if event.key == pygame.K_RIGHT:
            self.get_rocket.moving_right = False
            print('Отпустиили правую клавишу')
        elif event.key == pygame.K_LEFT:
            self.get_rocket.moving_left = False
            print('Отпустиили левую клавишу')
        elif event.key == pygame.K_UP:
            self.get_rocket.moving_up = False
            print('Отпустиили клавишу вверх')
        elif event.key == pygame.K_DOWN:
            self.get_rocket.moving_down = False
            print('Отпустиили клавишу вниз')



if __name__ == '__main__':
    r = Rocket()
    r.run()
