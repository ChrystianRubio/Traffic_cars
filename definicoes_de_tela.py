import pygame


class Tela:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Cars')
        self.controlador_frames = pygame.time.Clock()
        self.back_rua = pygame.image.load('Imagens/rua_pequena.png')
        self.back_rua = pygame.transform.scale(self.back_rua,(800,600))
        pygame.mixer.music.load('Som/som_urbano.wav')

    def aparecendo_dinheiro_na_tela(self, dinheiro_personagem):
        msg_fonte = pygame.font.Font('freesansbold.ttf', 25)
        msg_aparecendo = msg_fonte.render('Dinheiro: ' + str(dinheiro_personagem), True, (100, 200, 100))
        self.janela.blit(msg_aparecendo, (0, 10)) 

    def atualizando_tela(self):
        pygame.display.update() 
        self.controlador_frames.tick(350)

