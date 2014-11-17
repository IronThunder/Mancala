import pygame
from pygame.locals import *
import sys

pygame.init()
text_font = pygame.font.SysFont('monospace', 20)
pit_font = pygame.font.SysFont('monospace', 30)
end_font = pygame.font.SysFont('monospace', 30)

class Pit(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.count = 3
        self.position = position
        self.rect = pygame.Rect(position, (80, 80))
        self.khalana = False
        self.number = 0

    def chosen(self):
        self.count += 1

    def update(self, background):
        label = pit_font.render(str(self.count), 1, (0, 0, 0))
        label_position_x, label_position_y = self.position
        label_position_x += 20
        label_position_y += 20
        pygame.draw.circle(background, (128, 50, 0), (label_position_x, label_position_y), 40)
        if self.count <= 10:
            background.blit(label, (label_position_x-5, label_position_y-10))
        else:
            background.blit(label, (label_position_x-10, label_position_y-10))


class GraphicUI:
    def __init__(self):
        self.background = None
        self.screen = None
        self.pit_sprites = None
        self.clock = pygame.time.Clock()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Click the Pits')
        pygame.mouse.set_visible(1)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        self.pit_sprites = []
        for i in range(14):
            if i < 6:
                pit = Pit((250 + 100*(i+1), 100))
            if 6 < i < 13:
                pit = Pit((950 - 100*(i-6), 300))
            if i == 6:
                pit = Pit((950, 200))
                pit.khalana = True
            if i == 13:
                pit = Pit((250, 200))
                pit.khalana = True
            pit.number = i
            self.pit_sprites.append(pit)

    def move(self, extra_turn, invalid, number, board):
        self.screen = pygame.display.set_mode((1200, 800))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        pits = board.pits
        for i in range(len(self.pit_sprites)):
                self.pit_sprites[i].count = pits[i]
        if not extra_turn and not invalid:
            text = 'Player %d, enter the pit you would like to move from.' % number
        elif extra_turn and not invalid:
            text = 'You ended in your Khalana. Take an extra turn. Enter another pit'
        elif invalid:
            text = 'Invalid move. Please enter the number of a pit that stones in it that is on your side.'
        else:
            raise Exception('next_turn method failure')
        message = text_font.render(text, 1, (0, 0, 0))
        self.background.blit(message, (0, 700))
        pygame.mouse.set_visible(1)
        clock = pygame.time.Clock()
        pit_input = None
        while pit_input is None:
            clock.tick(60)
            for each in pygame.event.get():
                if each.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif each.type == KEYDOWN and each.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif each.type == MOUSEBUTTONDOWN:
                    for i in self.pit_sprites:
                        if i.rect.collidepoint(pygame.mouse.get_pos()):
                            pit_input = i.number
            for m in self.pit_sprites:
                m.update(self.background)
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
        return str(pit_input)

    def display_winner(self, victor, score):
        if victor == 0:
            text = 'The game ends in a tie. Congratulations./nThe odds of this happening are very slim.'
        elif victor == 1:
            text = 'The game ends with a victory for player 1!/nThe final score was %d to %d.' % (score, 36-score)
        elif victor == 2:
            text = 'The game ends with a victory for player 2!/nThe final score was %d to %d.' % (score, 36-score)
        else:
            raise Exception('rogue_AI_player_wins')
        message = end_font.render(text, 1, (0, 0, 0))
        self.background.blit(message, (0, 600))
        for m in self.pit_sprites:
            m.update(self.background)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()