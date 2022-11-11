import pygame
import sys
import random
from math import *
import time
pygame.init()
game_window=pygame.display.set_mode((600,600))
pygame.display.set_caption("Bouncing Ball")
board_x,board_y,board_d=300,550,0
ball_x,ball_y,ball_direction=board_x,board_y-15,[0,0]
running=True
clock=pygame.time.Clock()
state="stationary"
no_of_bricks=25
bricks=[]
score=0
ball_speed=3
for i in range(no_of_bricks):
          b_x=random.choice([x for x in range(70,500,80)])
          b_y=random.choice([y for y in range(300,500,30)])
          b_w=random.randint(30,60)
          b_h=random.randint(5,10)
          bricks.append([b_x,b_y,b_w,b_h])
def score_inc():
          global score
          a=pygame.font.Font('freesansbold.ttf',25)
          b=a.render("Score : "+str(score),True,(100,255,0),(0,0,30))
          r=b.get_rect()
          r.center=(400,25)
          game_window.blit(b,r)
def distance(t1,t2):
          return sqrt((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)
def boundary():
          pygame.draw.rect(game_window,(255,255,255),(35,35,530,530),5)
def brick(brick_x,brick_y,brick_w,brick_h):
          pygame.draw.line(game_window,(255,200,0),[brick_x-brick_w/2,brick_y],[brick_x+brick_w/2,brick_y],brick_h)
def ball(x,y):
          pygame.draw.circle(game_window,(255,100,0),(x,y),10)
def game():
          global running,board_x,board_y,board_d,state,ball_x,ball_y,score,ball_speed
          while(running is True):
                    game_window.fill((0,0,30))
                    for event in pygame.event.get():
                              if(event.type==pygame.QUIT):
                                        pygame.quit()
                                        sys.exit()
                                        running=False
                                        quit()
                              if(event.type==pygame.KEYDOWN):
                                        if(event.key==pygame.K_LEFT):
                                                  '''
                                                  if(board_x>=70 and board_x<=545):
                                                            board_x-=10'''
                                                  state="left"
                                        elif(event.key==pygame.K_RIGHT):
                                                  '''
                                                  if(board_x>=60 and board_x<=535):
                                                            board_x+=10'''
                                                  state="right"
                              if(event.type==pygame.KEYUP):
                                        state="stop"
                    for child in bricks:
                              brick(child[0],child[1],child[2],child[3])
                    if(state=="left" or state=="right"):
                              if(ball_direction[1]==0):
                                        ball_direction[1]=-(ball_speed)
                                        ball_direction[0]=ball_speed
                    ball_x+=ball_direction[0]
                    ball_y+=ball_direction[1]
                    for child in bricks:
                              if((child[0]-child[2]/2)<=ball_x<=(child[0]+child[2]/2)):
                                        if((child[1]-child[3]/2)<ball_y<(child[1]+child[3]/2)):
                                                  ball_direction[1]*=-1
                                                  child[0]=child[1]=1000
                                                  bricks.remove(child)
                                                  score+=1
                              if(ball_y==child[1]):
                                        if(ball_x==(child[0]+child[2]/2+10) or ball_x==(child[0]-child[2]/2-10)):
                                                  ball_direction[0]*=-1
                                                  child[0]=child[1]=1000
                                                  bricks.remove(child)
                                                  score+=1
                    if(state=="left"):
                              board_d=-5
                    elif(state=="right"):
                              board_d=5
                    elif(state=="stop"):
                              board_d=0
                    if(board_x>60 and board_x<535):
                              board_x+=board_d
                    if(board_x>=535):
                              board_x-=1
                    if(board_x<=60):
                              board_x+=1
                    if(ball_y<=45):
                              ball_direction[1]*=(-1)
                    if(ball_x<=45 or ball_x>=560):
                              ball_direction[0]*=(-1)
                    if(ball_y>=560):
                              print("Game Over!!")
                              time.sleep(2)
                              pygame.quit()
                              sys.exit()
                              running=False
                              quit()
                    if((board_x-25)<=ball_x<=(board_x+25)):
                              if(ball_y<=board_y+5 and ball_y>=board_y-5):
                                        ball_direction[1]*=-1
                    score_inc()
                    boundary()
                    ball(ball_x,ball_y)
                    pygame.draw.line(game_window,(255,255,255),(board_x-25,board_y),(board_x+25,board_y),10)
                    if(len(bricks)==0):
                              running=False
                              print("Congratulations!! You won")
                    pygame.display.update()
                    clock.tick(60)    
game()
