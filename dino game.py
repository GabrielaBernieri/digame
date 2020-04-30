import pygame
import random
from pygame import *
import sys


class dinossauro(object):
    AZUL = (108,166,205)

    def __init__(self, pos_x, pos_y):
        self.pos_x = 66
        self.pos_y = 107
        self.pulo = False
        self.puloconta = 14

    def draw(self, fundo):
        self.rect = pygame.draw.rect(fundo, dinossauro.AZUL, [self.pos_x, self.pos_y, 20, -20])

    def pular(self):
        if self.pulo:
            if self.puloconta >= -14:
                neg = -1 if self.puloconta < 0 else 1
                self.pos_y -= (self.puloconta ** 2) * 0.1 * neg
                self.puloconta -= 1
            else:
                self.pulo = False
                self.puloconta = 14

    def colidiu(self, rect):
        return self.rect.colliderect(rect)


class cactu(object):
    LILAS = (209,95,238)

    def __init__(self, pos_c, pos_z, altura):
        self.pos_c = pos_c
        self.pos_z = pos_z
        self.altura = altura

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, cactu.LILAS, [self.pos_c, self.pos_z, 20, -self.altura], )

    def anda(self, score):
        if self.pos_c > -20:
            self.pos_c -= 3
        if score >= 20:
            self.pos_c -= 5
        if score >= 50:
            self.pos_c -= 8
        if score >= 90:
            self.pos_c -= 10
        if score >= 120:
            self.pos_c -= 12

    def colidiu(self, rect):
        return self.rect.colliderect(rect)

class passaro(object):
    ROXO = (155,48,255)
    def __init__(self, pos_p, pos_w, altura):
        self.pos_p = pos_p
        self.pos_w = pos_w
    def draw (self, screen):
        self.rect = pygame.draw.rect(screen, passaro.ROXO, [self.pos_p, self.pos_w, 20, -10], )
    def anda(self, score):
        if self.pos_p > -20:
            if score >= 4:
                self.pos_p -= 3
    def colidiu(self, rect):
        return self.rect.colliderect(rect)
def wait(key):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
                else:
                    return False


def jogo(dino, cacts, passro, screen, score):
    fundo = pygame.Surface((largura, altura))
    fundo.fill(ROSA)
    screen.blit(fundo, (0, 0))
    tempo = pygame.time.Clock()
    while True:
        tempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.pulo = True
                score+=1

        screen.blit(fundo, (0, 0))
        pygame.draw.line(screen, BRANCO, [0, 109], [600, 109], 7)
        dino.pular()
        dino.draw(screen)
        cacts_copy = []
        passro_copy = []
        for cact in cacts:
            if cact.pos_c <= -20: cact = cactu(random.randrange(600, 700), 107, random.randrange(10, 30))
            cacts_copy.append(cact)
            cact.draw(screen)
            cact.anda(score)
        cacts = cacts_copy
        for pas in passro:
            if pas.pos_p <= -20: pas = passro(random.randrange(600, 700), 40, (20, -10))
            passro_copy.append(pas)
            pas.draw(screen)
            pas.anda(score)
        passro = passro_copy

        pygame.display.update()

        for cact in cacts:
            if dino.colidiu(cact.rect):
                print('colidiu.....')
                return True
        for pas in passro:
            if dino.colidiu(pas.rect):
                print('colidiu.....')
                return True


def main():
    preto = (0, 0, 0)
    fonte_jn = pygame.font.SysFont(pygame.font.get_default_font(), 25)
    fundo = pygame.Surface((largura, altura))
    fundo.fill(ROSA)
    screen.blit(fundo, (0, 0))
    msg3 = 'Precione SPAÇO para começar'
    texto3 = fonte_jn.render(msg3,True,preto)
    screen.blit(texto3,(200, 30))
    pygame.draw.line(screen, BRANCO, [0, 109], [600, 109], 7)
    dino = dinossauro(66, 107)
    cacts = [cactu(random.randrange(600, 700), 107, random.randrange(10, 30)),
             cactu(random.randrange(800, 900), 107, random.randrange(10, 30)),
             cactu(random.randrange(1000, 1100), 107, random.randrange(10, 30))]
    passro = [ passaro(random.randrange(600, 700), 40, (20, -10)),
            passaro(random.randrange(800, 900), 40, (20, -10)),
            passaro(random.randrange(1000, 1100), 40, (20, -10))]
    dino.draw(screen)
    for cact in cacts:
        cact.draw(screen)
    for pas in passro:
        pas.draw(screen)
    pygame.display.update()
    if not wait(pygame.K_SPACE): return

    while jogo(dino, cacts, passro, screen, score):
        fundo.fill(ROSA)
        msg = 'Precione S para jogar novamente'
        msg2 = 'Precione N para sair do jogo'
        texto = fonte_jn.render(msg, True, preto)
        texto2 = fonte_jn.render(msg2, True, preto)
        screen.blit(texto, (200, 30))
        screen.blit(texto2, (200, 55))
        pygame.display.update()
        if not wait(pygame.K_s): return
        dino = dinossauro(66, 107)
        cacts = [cactu(random.randrange(600, 700), 107, random.randrange(10, 30)),
                 cactu(random.randrange(800, 900), 107, random.randrange(10, 30)),
                 cactu(random.randrange(1000, 1100), 107, random.randrange(10, 30))]
        passro = [ passaro(random.randrange(600, 700), 40, (20, -10)),
                passaro(random.randrange(800, 900), 40, (20, -10)),
                passaro(random.randrange(1000, 1100), 40, (20, -10))]

ROSA = (255,181,197)
BRANCO = (255, 255, 255)
largura = 600
altura = 150
score = 0
screen = pygame.display.set_mode((largura, altura))
pygame.init()
pygame.font.init()
pygame.display.set_caption('block run')

main()
pygame.quit()
sys.exit(0)




