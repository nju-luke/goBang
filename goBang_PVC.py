# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:54:45 2016

@author: nju-hyhb
"""
from numpy import *
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
'''
AI 评分
'''       
def assession(Arr1,Arr2,Arrt,lin_num):
    dx=[0, 1, 1, 1, 0, -1, -1, -1]  
    dy=[-1, -1, 0, 1, 1, 1, 0, -1]
    count_A1=zeros((lin_num,lin_num,8))
    Valu_Arr1=zeros((lin_num,lin_num))
    for i in range(lin_num):
        for j in range(lin_num):
            if Arrt[i,j]==0:
                for k in range(8):
                    cnt=0
                    tx,ty=i,j
                    for t in range(5):
                        tx+=dx[k]
                        ty+=dy[k]
                        if (tx>(lin_num-1))|(tx<0)|(ty>(lin_num-1))|(ty<0):
                            break
                        if Arr1[tx,ty]:
                            cnt+=1
                        else:break
                    count_A1[i,j,k]=cnt
    for i in range(lin_num):
        for j in range(lin_num):
            if Arrt[i,j]==0:
                value_1=0
                for k in range(4):
                    if count_A1[i,j,k]+count_A1[i,j,k+4]>=4:
                        value_1+=10000
                    if count_A1[i,j,k]+count_A1[i,j,k+4]==3:
                        value_1+=1000                    
                    if count_A1[i,j,k]+count_A1[i,j,k+4]==2:
                        value_1+=100
                    if count_A1[i,j,k]+count_A1[i,j,k+4]==1:
                        value_1+=10
                Valu_Arr1[i,j]=value_1
        count_A2=zeros((lin_num,lin_num,8))
    Valu_Arr2=zeros((lin_num,lin_num))
    for i in range(lin_num):
        for j in range(lin_num):
            if Arrt[i,j]==0:
                for k in range(8):
                    cnt=0
                    tx,ty=i,j
                    for t in range(5):
                        tx+=dx[k]
                        ty+=dy[k]
                        if (tx>(lin_num-1))|(tx<0)|(ty>(lin_num-1))|(ty<0):
                            break
                        if Arr2[tx,ty]:
                            cnt+=1
                        else:break
                    count_A2[i,j,k]=cnt
    for i in range(lin_num):
        for j in range(lin_num):
            if Arrt[i,j]==0:
                value_1=0
                for k in range(4):
                    if count_A2[i,j,k]+count_A2[i,j,k+4]>=4:
                        value_1+=10000
                    if count_A2[i,j,k]+count_A2[i,j,k+4]==3:
                        value_1+=1000                    
                    if count_A2[i,j,k]+count_A2[i,j,k+4]==2:
                        value_1+=100
                    if count_A2[i,j,k]+count_A2[i,j,k+4]==1:
                        value_1+=10
                Valu_Arr2[i,j]=value_1
    Value=Valu_Arr1+dot(Valu_Arr2,1)
    position_max=argmax(Value)
    indx,indy=divmod(position_max,lin_num)   
    return indx,indy
 
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
    Arr1=zeros((line_num,line_num))
    Arr2=copy(Arr1)
    Arrt=copy(Arr1)
    win_state=0
    colors=1
    while not win_state:
        if colors>0:
            p1=win.getMouse()
            indx=round(p1.getX()/step)
            indy=round(p1.getY()/step)
        else:
            indx,indy=assession(Arr1,Arr2,Arrt,line_num)
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

if __name__=="__main__":
    main()