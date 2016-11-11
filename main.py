import pygame, sys
from pygame.locals import *
import objects


pygame.init()
white = (255,255,255)
black = (0,0,0)
winSize =(900,600)

window    = objects.Background(winSize,white,"./img/bg.png")
node      = objects.Node(winSize,"./img/ball.png")
paddle    = objects.Paddle(winSize,(20,110),0)
comPaddle = objects.Paddle(winSize,(20,110),1)
score     = objects.Score()


clock = pygame.time.Clock()
done = True


while done:
    window.drawBgImg()

    for event in pygame.event.get():
        if event.type == QUIT:
            done = False
        paddle.getEvent(event)

    node.collision(comPaddle.targetCollision(node) or paddle.targetCollision(node), winSize[0], winSize[1])

    if(paddle.targetCollision(node)):
        score.plusOne()
    if(node.x == 0):
        score.reset()
        
    comPaddle.tracking(node)
    node.moveOn()
    paddle.moveOn(winSize)
    comPaddle.moveOn(winSize)

    score.draw(window.screen)
    node.drawNodeImg(window.screen)
    paddle.drawPaddleRect(window.screen)
    comPaddle.drawPaddleRect(window.screen)

    pygame.display.update()
    clock.tick(150)

pygame.quit()
sys.exit()
