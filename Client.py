# client
import pygame
from network import Network

width = 500
height = 500
Cliennt_Number = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):  # conv str pos to int pos for client
    str = str.split(",")
    return int(str[0]), int(str[1])  # tup


def make_pos(tup):  # conv int pos to str pos for sever
    return str(tup[0]) + "," + str(tup[1])  # tup


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True

    n = Network()  # connecting to the server
    start_pos = read_pos(n.get_pos())
    print(start_pos)

    p = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0)) #you
    p2 = Player(0, 0, 100, 100, (255, 0, 0))#other player
    clock = pygame.time.Clock()

    while run:
        p2.update()
        clock.tick(60)
        p2pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2pos[0]
        p2.y = p2pos[1]

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        print("player 1: ",p.x,p.y)
        print("player 2: ",p2.x, p2.y)
        redraw_window(win, p, p2)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("client")
main()

