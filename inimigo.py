import pygame

from personagem import Personagem


class Inimigo(Personagem):
    def __init__(self):
        super().__init__()
        self.corpo = pygame.image.load('Imagens/inimigo_cor_azul_marinho.png')
        self.corpo = pygame.transform.scale(self.corpo,(145, 120))
        self.velocidade = float(1.5)
        
