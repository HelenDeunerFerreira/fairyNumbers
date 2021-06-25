import pygame
import random
import time
from criarLog import criarLog

pygame.init()
icone = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Fairy Numbers")

# números
n1 = pygame.image.load("assets/numbers/1.png")
n2 = pygame.image.load("assets/numbers/2.png")
n3 = pygame.image.load("assets/numbers/3.png")
n4 = pygame.image.load("assets/numbers/4.png")
n5 = pygame.image.load("assets/numbers/5.png")
n6 = pygame.image.load("assets/numbers/6.png")
n7 = pygame.image.load("assets/numbers/7.png")
n8 = pygame.image.load("assets/numbers/8.png")
n9 = pygame.image.load("assets/numbers/9.png")
n10 = pygame.image.load("assets/numbers/10.png")
n11 = pygame.image.load("assets/numbers/11.png")
n12 = pygame.image.load("assets/numbers/12.png")
n13 = pygame.image.load("assets/numbers/13.png")
n14 = pygame.image.load("assets/numbers/14.png")
n15 = pygame.image.load("assets/numbers/15.png")
n16 = pygame.image.load("assets/numbers/16.png")
n17 = pygame.image.load("assets/numbers/17.png")
n18 = pygame.image.load("assets/numbers/18.png")
n19 = pygame.image.load("assets/numbers/19.png")
n20 = pygame.image.load("assets/numbers/20.png")

numeros = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10,
           n11, n12, n13, n14, n15, n16, n17, n18, n19, n20]


largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))

fps = pygame.time.Clock()
fundo = pygame.image.load("assets/jardim.jpg")
fada = pygame.image.load("assets/fada.png")

preto = (0, 0, 0)
branco = (255, 255, 255)


def numbers():
    numero = random.choice(numeros)
    return numero


def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()


def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()


def contagem(acertos):
    message_display("Você acertou "+str(acertos)+" vez(es)!")


acertos = 0
criarLog()
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.play(-1)


def jogo():
    global acertos

    fadaPosicaoX = largura * 0.45
    fadaPosicaoY = altura * 0.6
    fadaLargura = 100
    movimentoX = 0
    numeroUsadoPosicaoX = largura * 0.45
    numeroUsadoPosicaoY = -220
    numeroUsadoLargura = 200
    numeroUsadoAltura = 125
    numeroUsadoVelocidade = 5

    numeroUsado = numbers()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        display.fill(branco)
        display.blit(fundo, (0, 0))
        fadaPosicaoX = fadaPosicaoX + movimentoX

        if fadaPosicaoX < 0:
            fadaPosicaoX = 0
        elif fadaPosicaoX > 680:
            fadaPosicaoX = 680

        display.blit(fada, (fadaPosicaoX, fadaPosicaoY))
        display.blit(numeroUsado, (numeroUsadoPosicaoX, numeroUsadoPosicaoY))

        numeroUsadoPosicaoY = numeroUsadoPosicaoY + numeroUsadoVelocidade

        if numeroUsadoPosicaoY > altura:
            numeroUsadoPosicaoY = -220
            numeroUsadoVelocidade += 0.3
            numeroUsadoPosicaoX = random.randrange(0, largura-50)

        if fadaPosicaoY < numeroUsadoPosicaoY + numeroUsadoAltura:
            if (((fadaPosicaoX > numeroUsadoPosicaoX) and (fadaPosicaoX >= numeroUsadoPosicaoX - fadaLargura))
                    or ((fadaPosicaoX < numeroUsadoPosicaoX) and (fadaPosicaoX <= numeroUsadoPosicaoX + fadaLargura))):
                acertos += 1
                contagem(acertos)

        pygame.display.update()
        fps.tick(60)


jogo()
