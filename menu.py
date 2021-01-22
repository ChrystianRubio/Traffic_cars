import pygame, sys


def menu():
    pygame.init()
    janela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Menu')

    flag = True
    pos0 = pos1 = 0
    
    while flag:
        janela.fill((10, 10, 43))

        font_msg = pygame.font.Font('freesansbold.ttf', 50)
        msg_iniciar = font_msg.render('Iniciar', True, (0, 50, 11))

        msg_sobre0 = font_msg.render('Sobre', True, (0, 50, 11))

        msg_sobre1 = font_msg.render('Criado por: Chrystian Rubio', True, (0, 50, 11))
        msg_sobre2 = font_msg.render('Desenhos: www.flaticon.com', True, (0, 50, 11))
    
        botao_iniciar = pygame.draw.rect(janela, (0, 0, 11), (100, 100, 200, 200))
        janela.blit(msg_iniciar, (120, 170))
    
        botao_sobre = pygame.draw.rect(janela, (0, 0, 11), (500, 100, 200, 200)) 
        janela.blit(msg_sobre0, (530, 170))
    
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos0 = pygame.mouse.get_pos()[0]
                pos1 = pygame.mouse.get_pos()[1]

        mouse = pygame.draw.rect(janela, (0, 0, 11), (pos0, pos1, 10, 10))

        if pygame.Rect.colliderect(mouse, botao_iniciar):
            flag = False

        if pygame.Rect.colliderect(mouse, botao_sobre):
            janela.blit(msg_sobre1, (10, 370))
            janela.blit(msg_sobre2, (10, 470))

        pygame.display.update()

