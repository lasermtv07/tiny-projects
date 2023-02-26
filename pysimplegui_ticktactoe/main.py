import PySimpleGUI as pg
def main():
    e="-"
    grid=[e]*9
    xt="x's turn"
    ot="o's turn"
    cont=True
    def winProc(w):
        win["i"].update(w +" wins")
    def drawProc():
        win["i"].update("draw")
        
    def chkWin(g):
        for x in range(0,3):
            if g[0+x*3]==g[1+x*3]==g[2+x*3] and g[0+x*3]!=e:
                winProc(g[0+x*3])
            if g[x]==g[x+3]==g[x+6] and g[x]!=e:
                winProc(g[x])
            if g[0]==g[4]==g[8] and g[0]!=e:
                winProc(g[0])
            if g[2]==g[4]==g[6] and g[2]!=e:
                winProc(g[2])
        if not e in g:
            drawProc()

    def mkTurn(g,p,c):
        if g[p]==e:
            g[p]=c
            if c=="x":
                win["i"].update(ot)
                c="o"
            else:
                win["i"].update(xt)
                c="x"
        chkWin(g)
        return [g,c]
    c="x"
    layout=[[pg.Text(xt, key="i")],
            [ pg.Button(e, key="0"), pg.Button(e, key="1"), pg.Button(e, key="2")],
            [ pg.Button(e, key="3"), pg.Button(e, key="4"), pg.Button(e, key="5")],
            [ pg.Button(e, key="6"), pg.Button(e, key="7"), pg.Button(e, key="8")],
            [pg.Button("Restart", key="r")]
    ]
    win=pg.Window("Tic Tac Toe", layout)
    while True:

        event, values= win.read()
        if event=="r":
            c="o"
            grid=[e]*9
            win["i"].update(ot)
        if event==pg.WIN_CLOSED:
            exit()
        if event=="0" or event=="1" or event=="2" or event=="3" or event=="4" or event=="5" or event=="6" or event=="7" or event=="8":
            md=mkTurn(grid,int(event),c)
            grid=md[0]
            c=md[1]
        for x in range(0,9):
            win[str(x)].update(grid[x])


main()
        