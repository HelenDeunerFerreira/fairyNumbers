import pygame
import random
import time

pygame.init()
#icone = pygame.image.load("assets/ironIcon.png")
# pygame.display.set_icon(icone)
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

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))

fps = pygame.time.Clock()
fundo = pygame.image.load("assets/jardim.png")
iron = pygame.image.load("assets/fada.png")
#missel = pygame.image.load("assets/missile.png")

preto = (0, 0, 0)
branco = (255, 255, 255)


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


def dead(desvios):
    message_display("Você Morreu com "+str(desvios)+" desvios")


def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))


def jogo():
    ironPosicaoX = largura * 0.45
    ironPosicaoY = altura * 0.8
    ironLargura = 120
    movimentoX = 0
    missilPosicaoX = largura * 0.45
    missilPosicaoY = -220
    missilLargura = 50
    missilAltura = 250
    missilVelocidade = 5

    desvios = 0

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
        ironPosicaoX = ironPosicaoX + movimentoX

        if ironPosicaoX < 0:
            ironPosicaoX = 0
        elif ironPosicaoX > 680:
            ironPosicaoX = 680

        display.blit(iron, (ironPosicaoX, ironPosicaoY))
        display.blit(missel, (missilPosicaoX, missilPosicaoY))
        missilPosicaoY = missilPosicaoY + missilVelocidade

        if missilPosicaoY > altura:
            missilPosicaoY = -220
            missilVelocidade += 1
            missilPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1

        escrevendoPlacar(desvios)

        if ironPosicaoY < missilPosicaoY + missilAltura:
            if ironPosicaoX < missilPosicaoX and ironPosicaoX+ironLargura > missilPosicaoX or missilPosicaoX+missilLargura > ironPosicaoX and missilPosicaoX+missilLargura < ironPosicaoX+ironLargura:
                dead(desvios)

        pygame.display.update()
        fps.tick(60)


jogo()
