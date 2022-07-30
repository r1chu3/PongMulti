import pickle
import socket
import _thread
import pygame
from game import Player
from game import Ball

PLAYER_WIDTH, PLAYER_HEIGHT = 15, 100
WIDTH, HEIGHT = 900, 600 
WHITE = (255, 255, 255)

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(ADDR)
except socket.error as e:
    print(str(e))

server.listen(2)
print(f'[LISTNING] Listning on {ADDR}')

players = [
    Player(10, 300 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT, WHITE), 
    Player(880, 300 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT, WHITE)
    ]

ball = Ball(WIDTH, HEIGHT, 10, WHITE)

def handle_client(conn, current_player):
    print(f'[NEW CONNECTION] {addr} connected')
    conn.send(pickle.dumps([players[current_player], ball])) # 0 is player and 1 is ball
    reply = ''
    ball_data = ball

    while True:
        clock = pygame.time.Clock()
        clock.tick(60)
        if current_player > 0:
            ball_data = ball.move(players[0], players[1])

        try:
            data = pickle.loads(conn.recv(2048))
            players[current_player] = data

            if not data:
                print('DISCONNETED')
                break
            else:
                if current_player == 0:
                    reply = [players[1], ball_data]
                else:
                    reply = [players[0], ball_data]

            conn.sendall(pickle.dumps(reply))
        except:
            remove_player()
            player_reset()
            ball_reset()
            break
        
    print('Lost connection')
    conn.close()

def player_reset():
    if current_player == 0:
        players[0].y = 300 - PLAYER_HEIGHT/2
    else:
        players[1].y = 300 - PLAYER_HEIGHT/2

def ball_reset():
    ball.x = WIDTH/2
    ball.y = HEIGHT/2

def remove_player():
    global current_player
    current_player -= 1


current_player = 0
while True:
    conn, addr = server.accept()
    _thread.start_new_thread(handle_client, (conn, current_player))
    current_player += 1 