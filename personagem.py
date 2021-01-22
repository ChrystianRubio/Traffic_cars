import pygame


class Personagem:
    def __init__(self):
        self.coordenada_x = 120
        self.coordenada_y = 450
        self.corpo = pygame.image.load('Imagens/car.png')
        self.gasolina = 3
        self.estado_esquerda = self.estado_direita = False
        self.dinheiro = 0
        self.velocidade = 2
        self.pegando_gasolina = pygame.mixer.Sound('Som/dinheiro.wav')
        
