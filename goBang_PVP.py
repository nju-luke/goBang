# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:54:45 2016

@author: nju-hyhb
"""

from graphics import *

def chessboard(win_width,win_height,step):
    win = GraphWin("goBang",win_width,win_height)  
    win.setBackground('#8ee6d2')
    size=win_width
    for x in range(0,size,step):
       lin_x=Line(Point(x+1,0),Point(x+1,size))
       lin_y=Line(Point(0,x+1),Point(size,x+1))
       lin_x.draw(win)
       lin_y.draw(win)
       lin_x.setWidth(1.5)
    for i in range(1,4):
        cirmid=Circle(Point(x*i/4,x*i/4),3)
        cirmid.setFill('black')
        cirmid.draw(win)
        cirmid=Circle(Point(x*i/4,x*(4-i)/4),3)
        cirmid.setFill('black')
        cirmid.draw(win)
    return win   

def chessman(Arr1,Arr2,indx,indy,win,step,colors):
    p1x=indx*step
    p1y=indy*step
    cir1=Circle(Point(p1x,p1y),step*0.45)
    if colors==1:
        Arr1[indx,indy]=1
        cir1.setFill('white')
        cir1.draw(win)
        colors*=-1
    else:
        Arr2[indx,indy]=1
        cir1.setFill('black')
        cir1.draw(win)
        colors*=-1
    return colors
    
def checkWin(Arr1,Arr2,line_num,colors):
    P=Arr1    
    if colors==1:
        P=Arr2
    for i in range(line_num):
        for j in range(line_num):            
            px,py=i,j
            valx=zeros(4)
            for k in range(5):
                if (px+k)<(line_num-1):
                    valx[0]+=P[px+k,py]                
                if py+k<line_num-1:
                    valx[1]+=P[px,py+k]
                if (px+k<line_num-1)&(py+k<line_num-1):
                    valx[2]+=P[px+k,py+k]
                if (px+k<line_num-1)&(py-k>0):
                    valx[3]+=P[px+k,py-k] 
            if max(valx)>4:
                return 1
    return 0
    
def winNotice(win,colors):
    winSide='White'
    if colors==1:
        winSide='Black'
    notic=Text(Point(200,200),winSide+'  Win!\n Press anykey to exit!')
    notic.draw(win)
    notic.setSize(30)

def main():
    
    win_width=800
    win_height=800
    line_num=25
    step=win_width/line_num
    win=chessboard(win_width,win_height,step)
    
    Arr1=[[i for i in range(line_num)] for k in range(line_num)]
    Arr1=dot(Arr1,0)
    Arr2=copy(Arr1)
    Arrt=copy(Arr1)
    
    win_state=0
    colors=1
    while not win_state:
        p1=win.getMouse()
        indx=round(p1.getX()/step)
        indy=round(p1.getY()/step)
        indx=int(indx)
        indy=int(indy)
        if not Arrt[indx,indy]:
            colors=chessman(Arr1,Arr2,indx,indy,win,step,colors)
            Arrt[indx,indy]=1
        win_state=checkWin(Arr1,Arr2,line_num,colors)
        if win_state:
            winNotice(win,colors)
            break
    win.getMouse()
    win.close()
    
main()


    
    
        
    

    
