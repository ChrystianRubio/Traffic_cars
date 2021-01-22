import pygame, sys, random

from definicoes_de_tela import Tela
from personagem import Personagem
from inimigo import Inimigo
from menu import menu
from horario import horario 


def principal():
    tela = Tela()
    personagem = Personagem()

    inimigo_azul_marinho = Inimigo()

    inimigo_azul = Inimigo()
    inimigo_azul.corpo = pygame.image.load('Imagens/inimigo_cor_azul.png')
    inimigo_azul.corpo = pygame.transform.scale(inimigo_azul.corpo,(145, 120))


    inimigo_preto = Inimigo()
    inimigo_preto.corpo = pygame.image.load('Imagens/inimigo_cor_preto.png')
    inimigo_preto.corpo = pygame.transform.scale(inimigo_preto.corpo,(145, 120))


    inimigo_verde = Inimigo()
    inimigo_verde.corpo = pygame.image.load('Imagens/inimigo_cor_verde.png')
    inimigo_verde.corpo = pygame.transform.scale(inimigo_verde.corpo,(145, 120))

    inimigo_coringa = Inimigo()
    inimigo_coringa.corpo = pygame.image.load('Imagens/inimigo_cor_azul.png')
    inimigo_coringa.corpo = pygame.transform.scale(inimigo_coringa.corpo,(145, 120))
    inimigo_coringa.rua_aleatoria = [-5, 560, 220, 343]
    escolhendo_para_coringa = random.randint(0, len(inimigo_coringa.rua_aleatoria) - 1)


    gasolina = Inimigo()
    gasolina.corpo = pygame.image.load('Imagens/dollar.png')
    gasolina.corpo = pygame.transform.scale(gasolina.corpo,(50, 50))
    gasolina.rua_aleatoria = [-5, 130, 100, 220, 343, 435, 560]
    escolhendo_para_gasolina = random.randint(0, len(gasolina.rua_aleatoria) - 1)


    lista_de_carros_inimigos = [inimigo_azul_marinho,
                                inimigo_preto,
                                inimigo_verde,
                                ]
    flag = True
    
    pygame.mixer.music.play(-1)

    while flag:
        
        #Rect do Azul Marinho
        rect_azul_marinho = pygame.draw.rect(tela.janela, 
                            (0, 0, 0), 
                            (inimigo_azul_marinho.coordenada_x + 170, inimigo_azul_marinho.coordenada_y - 95 , 65, 110))

        #Rect do Preto
        rect_preto = pygame.draw.rect(tela.janela, 
                                     (0, 0, 0), 
                                     (inimigo_preto.coordenada_x - 60, inimigo_preto.coordenada_y - 155 , 65, 110))

        #Rect do Verde
        rect_verde = pygame.draw.rect(tela.janela, 
                                     (0, 0, 0), 
                                     (inimigo_verde.coordenada_x + 475, inimigo_verde.coordenada_y - 115 , 65, 110))

        #Rect do coringa
        rect_coringa = pygame.draw.rect(tela.janela, 
                                       (0, 0, 0), 
                        (inimigo_coringa.coordenada_x + inimigo_coringa.rua_aleatoria[escolhendo_para_coringa] + 41, 
                        inimigo_coringa.coordenada_y - 115 , 65, 110))

        #Rect Gasolina
        rect_gasolina = pygame.draw.rect(tela.janela, 
                                        (0, 0, 0), 
                        (gasolina.coordenada_x + gasolina.rua_aleatoria[escolhendo_para_gasolina] + 10, 
                        gasolina.coordenada_y - 110 , 35, 40))

        
        
        #tela.janela.blit(personagem.corpo,(personagem.coordenada_x, personagem.coordenada_y))
        rect_personagem = pygame.draw.rect(tela.janela, 
                                          (0, 0, 0), 
                                          (personagem.coordenada_x + 33, personagem.coordenada_y, 60, 130))

        tela.janela.blit(tela.back_rua,(0,0))

        #Personagem
        tela.janela.blit(personagem.corpo,(personagem.coordenada_x, personagem.coordenada_y))
        
        #Azul Marinho
        tela.janela.blit(inimigo_azul_marinho.corpo,
                        (inimigo_azul_marinho.coordenada_x + 130,
                        inimigo_azul_marinho.coordenada_y - 100))


        #Preto
        tela.janela.blit(inimigo_preto.corpo,(inimigo_preto.coordenada_x - 100,inimigo_preto.coordenada_y - 160))
    

        #Verde
        tela.janela.blit(inimigo_verde.corpo,(inimigo_verde.coordenada_x + 435,inimigo_verde.coordenada_y - 120))
   

        #Rua aleatoria para o coringa
        if inimigo_coringa.coordenada_y <= 800:
            inimigo_coringa.coordenada_y += inimigo_coringa.velocidade
        else:
            inimigo_coringa.coordenada_y = -10
            inimigo_coringa.velocidade = float(random.randint(2, 5) + 0.3)
    
            escolhendo_para_coringa = random.randint(0, len(inimigo_coringa.rua_aleatoria) - 1)


        #Verde Escuro/Coringa
        tela.janela.blit(inimigo_coringa.corpo,
                        (inimigo_coringa.coordenada_x + inimigo_coringa.rua_aleatoria[escolhendo_para_coringa],
                        inimigo_coringa.coordenada_y - 120 )) 


        #Rua aleatoria para o coringa
        if gasolina.coordenada_y <= 3000: 
            gasolina.coordenada_y += gasolina.velocidade
        else:
            gasolina.coordenada_y = -10
            gasolina.velocidade = float(random.randint(1, 2))
    
            escolhendo_para_gasolina = random.randint(0, len(gasolina.rua_aleatoria) - 1)


        #Gasolina/Coringa
        tela.janela.blit(gasolina.corpo,
                        (gasolina.coordenada_x + gasolina.rua_aleatoria[escolhendo_para_gasolina],
                        gasolina.coordenada_y - 120))


        #Movimentacao dos carros
        for carro in lista_de_carros_inimigos:
            if carro.coordenada_y <= 800:
                carro.coordenada_y += carro.velocidade
            else:
                carro.coordenada_y = -10
                carro.velocidade = float(random.randint(1, 4) + 0.2)
    
    

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    personagem.estado_esquerda = True
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    personagem.estado_direita = True
                if evento.key == pygame.K_SPACE:
                    personagem.velocidade = 6 
            if evento.type == pygame.KEYUP:
                personagem.estado_esquerda = personagem.estado_direita = False;
                personagem.velocidade = 2
        

        #Movimentacao do personagem

        if personagem.estado_esquerda and personagem.coordenada_x > 0:
            personagem.coordenada_x -= personagem.velocidade
        if personagem.estado_direita and personagem.coordenada_x < 700:
            personagem.coordenada_x += personagem.velocidade


        #Colisao

        lista_de_rect = [rect_azul_marinho,
                        rect_preto,
                        rect_verde,
                        rect_coringa,
                        ]


        for rect in lista_de_rect:
            if pygame.Rect.colliderect(rect_personagem, rect):
                for carro in lista_de_carros_inimigos:
                    flag = False
                tempo_atual = horario()
                with open('Cadastro_de_pontos.dat', 'a') as objeto:
                    objeto.write('Time: ' + str(tempo_atual) + '|' + ' Pontos: ' + str(personagem.dinheiro) + '\n')

        # Colisao com o dinheiro

        if pygame.Rect.colliderect(rect_personagem,rect_gasolina):
            personagem.dinheiro += 120
            personagem.pegando_gasolina.play()
            gasolina.coordenada_y = 700
        
        #Aparecendo dinheiro na tela

        tela.aparecendo_dinheiro_na_tela(personagem.dinheiro)

        tela.atualizando_tela()
        

while True:
    menu()     
    principal()

