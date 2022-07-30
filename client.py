import pygame
from game import Player
from game import Ball
from network import Network
pygame.font.init()

BG_COLOR = (0, 0, 0)
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Online Pong')
FONT = pygame.font.SysFont('calibri', 20)
WHITE = (255, 255, 255)

def redraw_window(player1, player2, ball):
    WIN.fill(BG_COLOR)
    player1.draw(WIN)
    player2.draw(WIN)
    ball.draw(WIN)

    p1_score_txt = FONT.render(str(ball.p1_score), 1, WHITE)
    p2_score_txt = FONT.render(str(ball.p2_score), 1, WHITE)
    WIN.blit(p1_score_txt, (WIDTH/4 - p1_score_txt.get_width()/2, 5))
    WIN.blit(p2_score_txt, (WIDTH - WIDTH/4 - p2_score_txt.get_width()/2, 5))

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    data = n.getData()
    p1 = data[0]
    ball = data[1]

    while run:  
        clock.tick(60)
        reply = p1
        both_data = n.send(reply)
        p2 = both_data[0]
        ball = both_data[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        
        p1.move()    
        redraw_window(p1, p2, ball)

if __name__ == '__main__':
    main()