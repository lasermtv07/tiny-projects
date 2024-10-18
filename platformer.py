#!/data/data/com.termux/files/usr/bin/python
import pygame as pg

pg.init()
screen=pg.display.set_mode((832,579))

field=[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0]

    ]
can_jump=True
jmp_timer=0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j]==2:
            px=j*64
            py=i*64
            field[i][j]=0
while True:
    screen.fill((0,0,0))
    for e in pg.event.get():
        if e.type==pg.QUIT: exit()

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]==1:
                pg.draw.rect(screen,(50,50,50),pg.Rect(64*j,64*i,64,64))
    pg.draw.rect(screen,(0,0,255),pg.Rect(px,py,64,64))
    bx=int(((px)/64)-((px%64)/64))
    bxa=int(((px+64)/64)-(((px+64)%64)/64))
    by=int((py/64)-((py%64)/64))
    print((px,py))
    if (field[by+1][bx]==0 and field[by+1][bxa]==0) or py%64>4:
        py+=5
        can_jump=False
    else:
        can_jump=True
    if pg.key.get_pressed()[pg.K_RIGHT]:
        px+=5
    if pg.key.get_pressed()[pg.K_LEFT]:
        px-=5
    if pg.key.get_pressed()[pg.K_UP] and can_jump:
        can_jump=False
        jmp_timer=30
    if jmp_timer>0:
        py-=11
        jmp_timer-=1

    pg.display.flip()
    pg.time.Clock().tick(60)
