import pygame
import time
import math

pygame.init()

# JANELA
janelaWidth = 800
janelaHeight = 600
janela = pygame.display.set_mode((janelaWidth, janelaHeight))
pygame.display.set_caption('Super Head Soccer')

# PARA DEFINIR FPS
clock = pygame.time.Clock()
FPS = 60

# CORES
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 90, 0)
blue = (0, 0, 255)

# Sprites-Balizas
goalRight = pygame.image.load('goal_1.png')
goalLeft = pygame.image.load('goal_2.png')

# Sprites-Relvado
grass = pygame.image.load('grass.png')
# Sprites-Bola
ball = pygame.image.load('ball1.png')

# Sprites-Jogadores
player1 = pygame.image.load('P1.png')
player2 = pygame.image.load('p2.png')



def scoreBoard(goals1,goals2):
     #font
    fonte=pygame.font.SysFont("arial", 30)
    texto1=fonte.render("Player 1: "+ str(goals1),True,(0,0,0))
    texto2=fonte.render("Player 2: "+ str(goals2),True,(0,0,0))
    # Escrever Scores
    janela.blit(texto1, (10, 10))
    janela.blit(texto2, (janelaWidth-130, 10))

def intro():
    start=True
    janela.fill(white)
    while start:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    start=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        
        fonte=pygame.font.SysFont("arial", 30)  
        texto=fonte.render("Para começar a jogar pressione a barra de espaço.",True,(0,0,0))
        janela.blit(texto, (100, 100))
        texto=fonte.render("Pressione Q para sair",True,(0,0,0))
        janela.blit(texto, (100, 140))
        pygame.display.update()
        clock.tick(FPS)
def pause():
    paused=True 
    janela.fill(white)
    while paused:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                   paused=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        
        fonte=pygame.font.SysFont("arial", 30)  
        texto=fonte.render("Para voltar ao jogar pressione a barra de espaço.",True,(0,0,0))
        janela.blit(texto, (100, 100))
        texto=fonte.render("Pressione Q para sair",True,(0,0,0))
        janela.blit(texto, (100, 140))
        pygame.display.update()
        clock.tick(FPS)

def gameOver(player):
    restart=True 
    janela.fill(white)
    while restart:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                   restart=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        
        fonte=pygame.font.SysFont("arial", 30)  
        texto=fonte.render("O jogador "+player+" perdeu",True,(0,0,0))
        janela.blit(texto, (100, 100))
        texto=fonte.render("Se quiseres desforra pressiona a barra de espaço",True,(0,0,0))
        janela.blit(texto, (100, 140))
        texto=fonte.render("Pressione Q para sair",True,(0,0,0))
        janela.blit(texto, (100, 180))
        pygame.display.update()
        clock.tick(FPS)
    if restart==False:
        return True

def gameLoop():
    gameExit = False
    # ALTURA DO CHÃO
    floorHeight = (janelaHeight / 4)*3
    # ALTURA DA TRAVE
    barHeight = janelaHeight-(floorHeight/3)-200
    # LARGURA DA BALIZA
    goalThickness = 82
    # VARIAVEIS DE MOVIMENTO:
    ballRadius = 20
    playerRadius = 30
    playerSpeed = 5
    playerJumpSpeed = 13
    playerGravity = 0.4
    ballGravity = 0.4

    # BALL
    ball_X = janelaWidth/2
    ball_Y = floorHeight - 200

    ball_X_change = 0
    ball_Y_change = 0

    # PLAYER 1
    p1_X = 200
    p1_Y = floorHeight - playerRadius

    p1_X_change = 0
    p1_Y_change = 0

    # PLAYER 2
    p2_X = 600
    p2_Y = floorHeight - playerRadius

    p2_X_change = 0
    p2_Y_change = 0

    #Booleanas orientação dos sprites dos jogadores
    p1FacingRight = True
    p2FacingLeft = True

    # Variavel bool para saber se foi Golo
    gol = False
    # Contar Golos Cada jogador
    gols1 = 0
    gols2 = 0
   
    while not gameExit:

        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pause()
            if event.type == pygame.QUIT:  # FECHAR O JOGO NO "X" DA JANELA
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # PLAYER 2
                if event.key == pygame.K_LEFT:
                    p2_X_change = -playerSpeed
                    p2FacingLeft = True
                if event.key == pygame.K_RIGHT:
                    p2_X_change = playerSpeed
                    p2FacingLeft = False
                if event.key == pygame.K_UP:
                    if p2_Y+playerRadius == floorHeight:
                        p2_Y_change = -playerJumpSpeed
                # PLAYER 1
                if event.key == pygame.K_a:
                    p1_X_change = -playerSpeed
                    p1FacingRight = False
                if event.key == pygame.K_d:
                    p1_X_change = playerSpeed
                    p1FacingRight = True

                if event.key == pygame.K_w:
                    if p1_Y+playerRadius == floorHeight:
                        p1_Y_change = -playerJumpSpeed
            if event.type == pygame.KEYUP:
                # PLAYER 2
                if event.key == pygame.K_LEFT:
                    if p2_X_change == -playerSpeed:
                        p2_X_change = 0
                if event.key == pygame.K_RIGHT:
                    if p2_X_change == playerSpeed:
                        p2_X_change = 0
                if event.key == pygame.K_UP:
                    p2_Y_change = p2_Y_change / 2
                # PLAYER 1
                if event.key == pygame.K_a:
                    if p1_X_change == -playerSpeed:
                        p1_X_change = 0
                if event.key == pygame.K_d:
                    if p1_X_change == playerSpeed:
                        p1_X_change = 0
                if event.key == pygame.K_w:
                    p1_Y_change = p1_Y_change / 2

        # APLICAR GRAVIDADE
        p1_Y_change += playerGravity
        p2_Y_change += playerGravity

        ball_Y_change += ballGravity
        if ball_X_change > 0:
            ball_X_change -= 0.01
        elif ball_X_change < 0:
            ball_X_change += 0.01

        # UPDATE ÁS POSIÇÕES
        # PLAYERS
        p1_X += p1_X_change
        p2_X += p2_X_change

        p1_Y += p1_Y_change
        p2_Y += p2_Y_change
        # BOLA
        ball_X += ball_X_change
        ball_Y += ball_Y_change

        # REAPLICAR BACKGROUND
        janela.fill(white)
        
        # Desenhar Balizas
        janela.blit(goalRight, (janelaWidth-82, barHeight))
        janela.blit(goalLeft, (0, barHeight))
        janela.blit(grass, (0, floorHeight))
        # DESENHAR FLOOR
        pygame.draw.line(janela, black, (0, floorHeight),
                         (janelaWidth, floorHeight), 1)
       
        # DELIMITAR OS JOGADORES À JANELA
        # PLAYER 1
        if p1_X-playerRadius < 0:
            p1_X = 0+playerRadius

        if p1_X+playerRadius > janelaWidth:
            p1_X = janelaWidth-playerRadius

        # PLAYER 2
        if p2_X-playerRadius < 0:
            p2_X = 0+playerRadius

        if p2_X+playerRadius > janelaWidth:
            p2_X = janelaWidth-playerRadius

        # IMPEDIR QUE OS JOGADORES ATRAVESSEM O FLOOR
        # PLAYER 1
        if p1_Y+playerRadius >= floorHeight:
            p1_Y = floorHeight - playerRadius

        # PLAYER 2
        if p2_Y+playerRadius >= floorHeight:
            p2_Y = floorHeight - playerRadius

        # COLISOES BOLA
        # PAREDES
        if ball_X-ballRadius < 0:
            ball_X = 0 + ballRadius
        if ball_X-ballRadius == 0:
            ball_X_change *= -0.6

        if ball_X+ballRadius > janelaWidth:
            ball_X = janelaWidth - ballRadius
        if ball_X+ballRadius == janelaWidth:
            ball_X_change *= -0.6
        # FLOOR
        if ball_Y+ballRadius > floorHeight:
            ball_Y = floorHeight - ballRadius
        if ball_Y+ballRadius == floorHeight:
            ball_Y_change = -ball_Y_change*0.75
            if math.fabs(ball_Y_change) <= 2:
                ball_Y_change = 0
                ball_X_change = 0
        # TRAVE DIREITA
        #COLISÃO FRENTE DA TRAVE
        if ball_X+ballRadius >= janelaWidth-82 and ball_Y+ballRadius >= barHeight and ball_Y-ballRadius <= barHeight-14 and ball_X <= janelaWidth-82:
            ball_X =janelaWidth-82-ballRadius
            ball_X_change *= -1
        #COLISÃO TOPO DA TRAVE
        elif ball_X+ballRadius >= janelaWidth-82 and ball_Y+ballRadius >= barHeight and ball_Y-ballRadius <= barHeight-14:
            ball_Y = barHeight - ballRadius
            ball_Y_change *= -1


        # TRAVE  ESQUERDA
        #82 igual largura de baliza, 14 largura da barra
        if ball_X-ballRadius <= 82  and ball_Y+ballRadius >= barHeight and ball_Y-ballRadius <= barHeight-14 and ball_X >= 82:
            ball_X =82+ ballRadius
            ball_X_change *= -1
        #COLISÃO TOPO DA TRAVE
        elif ball_X-ballRadius <= 82  and ball_Y+ballRadius >= barHeight and ball_Y-ballRadius <= barHeight-14:
            ball_Y = barHeight - ballRadius
            ball_Y_change *= -1

        # Golo na baliza do lado direito
        if ball_X+ballRadius >= janelaWidth-82:
            if ball_Y-ballRadius > barHeight+14:
                #print("Golo")
                gol = True
                gols1 += 1
                
                

        # Golo na baliza do lado esquerdo
        if ball_X-ballRadius <= 82:
            if ball_Y-ballRadius > barHeight+14:
                #print("Golo")
                gol = True
                gols2 += 1
              
                

        # Resetar posição da bola
        if gol == True:
            ball_X = janelaWidth/2
            ball_Y = floorHeight - 200
            ball_X_change=0
             # PLAYER 1
            p1_X = 200
            p1_Y = floorHeight - playerRadius

            p1_X_change = 0
            p1_Y_change = 0

            # PLAYER 2
            p2_X = 600
            p2_Y = floorHeight - playerRadius

            p2_X_change = 0
            p2_Y_change = 0
            gol=False
        
        # PLAYER1
        if math.hypot(ball_X - p1_X, ball_Y - p1_Y) < (playerRadius+ballRadius):
            hypot = math.hypot(ball_X - p1_X, ball_Y - p1_Y)
            overlap = (playerRadius+ballRadius) - hypot
            teta = math.atan2(ball_Y - p1_Y, ball_X - p1_X)
            #print(teta)
            vetor = pygame.math.Vector2(math.cos(teta), math.sin(teta))
            ball_X += vetor.x*overlap
            ball_Y += vetor.y*overlap
            ball_X_change += 4 * vetor.x
            if p1_Y + playerRadius == floorHeight:
                ball_Y_change += -5 + 2*vetor.y
            else:
                ball_Y_change += -1 + 2*vetor.y

        # PLAYER2
        if math.hypot(ball_X - p2_X, ball_Y - p2_Y) < (playerRadius+ballRadius):
            hypot = math.hypot(ball_X - p2_X, ball_Y - p2_Y)
            overlap = (playerRadius+ballRadius) - hypot
            teta = math.atan2(ball_Y - p2_Y, ball_X - p2_X)
            #print(teta)
            vetor = pygame.math.Vector2(math.cos(teta), math.sin(teta))
            ball_X += vetor.x*overlap
            ball_Y += vetor.y*overlap
            ball_X_change += 4 * vetor.x
            if p2_Y + playerRadius == floorHeight:
                ball_Y_change += -5 + 2 * vetor.y
            else:
                ball_Y_change += -2 + 2 * vetor.y

        # DESENHAR OBJETOS NAS NOVAS POSIÇÕES
        
        #P1
        if p1FacingRight == False:
            janela.blit(pygame.transform.flip(player1,True,False), (int(round(p1_X)-playerRadius),
                              int(round(p1_Y)-playerRadius)))
        else:    
            janela.blit(player1, (int(round(p1_X)-playerRadius),
                                  int(round(p1_Y)-playerRadius)))
        #P2
        if p2FacingLeft == False:
            janela.blit(pygame.transform.flip(player2,True,False), (int(round(p2_X)-playerRadius),
                              int(round(p2_Y)-playerRadius)))
        else:    
            janela.blit(player2, (int(round(p2_X)-playerRadius),
                                  int(round(p2_Y)-playerRadius)))
        # BOLA
        janela.blit(ball, (int(round(ball_X)-ballRadius),
                           int(round(ball_Y)-ballRadius)))
        scoreBoard(gols1,gols2)
        #Acabar jogo
        if gols1 >=5 :
           restart = gameOver("player2")
           if restart:
               gols1=0
               gols2=0
        if gols2 >=5 :
           restart = gameOver("player1")
           if restart:
               gols1=0
               gols2=0
        # UPFATE
        pygame.display.update()

        # APLICAR FPS
        clock.tick(FPS)

    # FECHAR O JOGO
    pygame.quit()
    quit()

intro()
gameLoop()
