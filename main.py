import pygame


FPS = 50  # количество кадров в секунду
SIZE = WIDTH, HEIGHT = 800, 400


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [
            [0] * width for _ in range(height)
        ]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self,  screen):
        end_x = self.width * self.cell_size + self.left
        end_y = self.height * self.cell_size + self.top
        for x in range(self.left, end_x, self.cell_size):
            for y in range(self.top, end_y, self.cell_size):
                pygame.draw.rect(
                    screen,
                    'white',
                    (x, y, self.cell_size, self.cell_size),
                    width=1
                )


def main():
    pygame.display.set_caption('Наш проект')
    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()
    running = True

    # поле 5 на 7
    board = Board(4, 3)
    board.set_view(300, 100, 80)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill('black')
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
