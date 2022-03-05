import pygame
import random
pygame.init()
widthscreen=800
heightscreen=600
Keep_going = True
Screen  = pygame.display.set_mode([widthscreen,heightscreen])
point1player1=[100,50]
point2player1=[200,50]
point3player1=[300,50]
point1player2=[500,50]
point2player2=[600,50]
point3player2=[700,50]
White=(255,255,255)
Black=(0,0,0)

ball = {
    'Width':10,
    'speedy':0.3,
    'speedx':0.6,
    'positionx':400,
    'positiony':300,
    'radius':50,




}
player1 = {
    'positionx':1,
    'positiony': 100,
    'racket': '',
    'width':10,
    'height':200,
    'score':0
}

player2 = {
    'positionx':790,
    'positiony': 100,
    'racket': '',
    'width':10,
    'height':200,
    'score':0
}

#
def reachend(player):
    if player['positiony'] <= -1:
        return True
    if player['positiony'] + player['height'] >= 601:
        return True
    return False

def updateracket(player):
    player['racket'] = pygame.Rect(player['positionx'],player['positiony'], player['width'], player['height'])

def moveball(ball):
    ball['positionx']+=ball['speedx']
    ball['positiony']+=ball['speedy']

def crash(player,ball):
    if ball['positionx'] > player['positionx'] and ball['positionx']<player['positionx']+player['width'] and  ball['positiony'] > player['positiony'] and ball['positiony']<player['positiony']+player['height']:
        return True  
    else:      
        return False

def randfloat(lower,upper):
    r = random.randrange(int(lower*100), int(upper*100))
    return r/100

def ballbounce(ball):
    if ball['positiony'] >= heightscreen:
        return True
    if ball['positiony'] <= 0:
        return True
    return False

def outside1(ball):    
    if ball['positionx'] < -10:
            return True
def outside2(ball):
    if ball['positionx'] > 810:
        return True

    

while Keep_going == True:
    for event in pygame.event.get():
        
        if event.type==pygame.TEXTINPUT:
            if event.text == 'p':
                pass
            if event.text == 'q':
                Keep_going = False
            if event.text == 'w':
                player1['positiony']-=10
                if reachend(player1):
                    player1['positiony']+=10
            elif event.text == 's':
                player1['positiony']+=10
                if reachend(player1):
                    player1['positiony']-=10

   
    
    
        

                
    if ball['positiony']<player2['positiony']:
        player2['positiony']-=20
        print('alto')
    elif ball['positiony']>player2['positiony']:
        player2['positiony']+=20  
        print('bajo')         
    Screen.fill(Black)
    updateracket(player1)
    updateracket(player2)

    if crash(player2,ball):
        
        ball['speedx']*=-1
        ball['speedy']*=-1
        ball['speedy']*=randfloat(0.5,1.5)
        ball['speedx']*=randfloat(0.3,1.7)
        
    if crash(player1,ball):
        ball['speedx']*=-1
        ball['speedy']*=-1
        ball['speedy']*=randfloat(0.5,1.5)
        ball['speedx']*=randfloat(0.3,1.7)

        
        
    
    moveball(ball)
    
    if ballbounce(ball):
        ball['speedy']*=-1

    if outside1(ball):
        player2['score']+=1
        ball['positionx']=300
        ball['positiony']=400
    if outside2(ball):
        print('un punto')
        player1['score']+=1
        ball['positionx']=400
        ball['positiony']=300
    


    
    pygame.draw.rect(Screen,White,player1['racket'])
    pygame.draw.rect(Screen,White,player2['racket'])
    pygame.draw.circle(Screen,White,(ball['positionx'],ball['positiony']),ball['radius'])
    if player1['score'] >= 1:
        pygame.draw.circle(Screen,White,(point1player1),50)
    if player1['score']>=2:
        pygame.draw.circle(Screen,White,(point2player1),50)
    if player1['score']>=3:
        pygame.draw.circle(Screen,White,(point3player1),50)
        
    
    
    pygame.display.update()

    #pygame.draw.rect(screen,Green,(30,30,30,30))

pygame.quit()

