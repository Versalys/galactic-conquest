from spaceships import *
from space_objects import *
from board import Board

import pygame as pg
import traceback
from time import sleep

def main():
    display = pg.display.set_mode((1500, 1500))
    turn = 'red'
    board = Board(25, 25, display, turn)
    test_ship = Cruiser(10, 10, 'red', 0)
    board.simple_generate_map(excl={(10,10)})
    board.add_obj(test_ship)

    
    screen_dragging = False
    screen_mov_start = (0,0)
    started_moving = False

    while True:
        display.fill((0,0,0))
        # events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN: # keys
                print("Keydown:", event.key)
                if event.key == pg.K_UP:
                    board.move_spaceship(0)
                elif event.key == pg.K_RIGHT:
                    board.move_spaceship(1)
                elif event.key == pg.K_DOWN:
                    board.move_spaceship(2)
                elif event.key == pg.K_LEFT:
                    board.move_spaceship(3)
            elif event.type == pg.MOUSEBUTTONDOWN:
                clicked_obj = board.get_object_at_pixels(pg.mouse.get_pos())
                if isinstance(clicked_obj, SpaceShip):
                    board.select_spaceship(clicked_obj)
                else:
                    board.select_spaceship(None)
                    screen_dragging = True
                    started_moving = False
            elif event.type == pg.MOUSEBUTTONUP:
                screen_dragging = False
                started_moving = False
            elif event.type == pg.MOUSEMOTION and screen_dragging:
                if not started_moving:
                    screen_mov_start = event.pos
                    started_moving = True
                pixels = event.pos[0] - screen_mov_start[0], event.pos[1] - screen_mov_start[1]
                board.update_window_position(pixels)

        # draw board
        board.draw(display)
        pg.display.flip()


if __name__ == "__main__":
    try:
        pg.init()
        main()
    except Exception as e:
        pg.quit()
        print(traceback.format_exc())
        quit()
    

