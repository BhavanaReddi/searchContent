from turtle import*
import turtle
bgcolor("white")
C,A=Turtle(),Turtle()
C.speed(0),A.speed(0),C.ht()


#$$$$$$$$$$$$$$$-------GOOGLE--------$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
go=Turtle()
go.speed(0),go.up(),go.color("blue"),go.goto(63,130),go.write("mini",True,font=("Serif",15)),go.goto(100,70),go.ht()
list=['blue','red','orange','blue','green','red']
google="Google"
for i in range(6):
	go.color(list[i])
	go.write(google[i],True,font=("Times new roman",60))
go.goto(270,55),go.color("grey"),go.write("RGUKT",True,font=("Times new roman",15,"bold")),go.goto(480,-280),go.color("black"),go.write("by",True,font=("Times new roman",15)),go.goto(500,-300),go.write("P.Jagadish..",True,font=("Times new roman",20)),go.color("brown"),go.goto(-670,280),go.pd(),go.pensize(6),go.fd(590),go.pensize(1.5),go.bk(30),go.rt(90),go.fd(500),go.rt(70),go.fd(300),go.rt(40),go.fd(270),go.rt(70),go.fd(510)	
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#+++++++++++++++++++this is main program++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def keys(n):
	w=n.split()
	k,g,c,we,qw,ty,e,d,kl,ij,fd,df="","",0,[],[],[],0,{},[],{},[],[]
	gj=len(w)
	for j in w:
		we.append(j)
	def rgukt2(gh):
		g=""
		for m in gh:
			g=g+" "+m
		qw.append(g)
	def rgukt(v):
		k=""
		if v==0:
			return 0
		for j in range(v):
			k=k+" "+w[j]
		qw.append(k)
		return rgukt(v-1)
	rgukt(len(w))
	def rgukt1(l):
		i=0
		while len(w)>i:
			del w[0]
			i=i+1
			rgukt2(w)
	rgukt1(gj)
	for i in qw:
		hj=i.strip(" ")
		we.append(hj)
	for j in we:
		if j not in ty:
			ty.append(j)
	aa=sorted(ty)
	#================================combinations================================
	o=open("list.txt","r")
	p=o.readlines()       		      
	o.close()
	hj={}            
	for i in range(len(p)):           
		w=p[i].strip("\n") 
		ab,abc,h,c=[],[],[],0        
		v=open(w,"r")          
		r=v.readlines()
		v.close()                            
		for j in r:            
			o=j.split()    
			for j in o:
				h.append(j)
		for b in aa:
			z=0
			for x in h:
				if b==x:
					z=z+1
			abc.append(b)
			ab.append(z)
			d[w]=ab
		hj[w]=abc
	#================================================================================
	for u in hj:
			g=u
			uv=hj[u]
			vu=d[u]
			u={}
			for k in range(len(uv)):
				f=uv[k].count(" ")+1
				if f not in kl:
					kl.append(f)
	#========================================================================
	for i in kl:
		uk={}
		for u in hj:
			gl=u
			viu,uvj=d[u],hj[u]
			for k in range(len(uvj)):
				xi=uvj[k].count(" ")+1
				if i==xi:
					if gl not in uk:
						uk[gl]=viu[k]
					else:
						fg=uk[gl]
						hl=fg+viu[k]
						uk[gl]=hl
		ij[i]=uk
	#================================================================
	p=sorted(kl)
	p.reverse()
	c=0
	for i in p:
		o=ij[i]
		g,t=0,[]
		for j in o:
			gh=o[j]
			t.append(gh)
		ti=sorted(t)
		ti.reverse()
		ju=ij[i]
		for l in ju:
			for l in ju:
				rt=ju[l]
				if rt==ti[g] and ti[g]>0 and c<10:
					fd.append(l)
					c=c+1
			g=g+1
	for i in fd:
		if i not in df:
			df.append(i)
#====================================this below about the writing letters in turtle================================	
	C.ht()	
	C.color("blue"),C.pu(),C.goto(-630,240)
	A.ht(),A.speed(0),A.color("purple"),A.pu(),A.goto(-650,300)
	v,ci=50,0
	A.write("Showing results for",True,font=("Times new roman",22,"italic")),A.fd(30),A.write(n,True,font=('Arial',22,"bold"))
	for i in df:
			C.ht(),C.speed(0),C.write(i[29:],True,font=("Comic Sans MS",15)),C.goto(-630,240-v)
			v=v+50
a=Turtle()
a.ht(),a.goto(-5,0),a.pensize(2),a.fd(500),a.lt(90),a.fd(30),a.pensize(1),a.lt(90),a.fd(500),a.lt(90),a.fd(30),a.lt(90)
n,T="",0
#====================this writing of elements in the box======================
ht()
def main(k):
	global n,T
	if k!='Tab' and k!="BackSpace":
		n=n+k
		write(k,True,font=("Arial",15))
	if k=="BackSpace":
		n=n.strip(n[-1])
		undo()			
	if k=='Tab':
		T=T+1
		for j in range(30):
			if T>1:
				A.undo()
				C.undo()
		keys(n)
		for i in range(len(n)):
			undo()
			n=""
def turn():
	main('a')
onkey(turn,"a")
def turn():
	main('b')
onkey(turn,"b")
def turn():
	main('c')
onkey(turn,"c")
def turn():
	main('d')
onkey(turn,"d")
def turn():
	main('e')
onkey(turn,"e")
def turn():
	main('f')
onkey(turn,"f")
def turn():
	main('g')
onkey(turn,"g")
def turn():
	main('h')
onkey(turn,"h")
def turn():
	main('i')
onkey(turn,"i")
def turn():
	main('j')
onkey(turn,"j")
def turn():
	main('k')
onkey(turn,"k")
def turn():
	main('l')
onkey(turn,"l")
def turn():
	main('m')
onkey(turn,"m")
def turn():
	main('n')
onkey(turn,"n")
def turn():
	main('o')
onkey(turn,"o")
def turn():
	main('p')
onkey(turn,"p")
def turn():
	main('q')
onkey(turn,"q")
def turn():
	main('r')
onkey(turn,"r")
def turn():
	main('s')
onkey(turn,"s")
def turn():
	main('t')
onkey(turn,"t")
def turn():
	main('u')
onkey(turn,"u")
def turn():
	main('v')
onkey(turn,"v")
def turn():
	main('w')
onkey(turn,"w")
def turn():
	main('x')
onkey(turn,"x")
def turn():
	main('y')
onkey(turn,"y")
def turn():
	main('z')
onkey(turn,"z")
def turn():
	main(' ')
onkey(turn,"space")
#-------------------------------------------
def turn():
	main('A')
onkey(turn,"A")
def turn():
	main('B')
onkey(turn,"B")
def turn():
	main('C')
onkey(turn,"C")
def turn():
	main('D')
onkey(turn,"D")
def turn():
	main('E')
onkey(turn,"E")
def turn():
	main('F')
onkey(turn,"F")
def turn():
	main('G')
onkey(turn,"G")
def turn():
	main('H')
onkey(turn,"H")
def turn():
	main('I')
onkey(turn,"I")
def turn():
	main('J')
onkey(turn,"J")
def turn():
	main('K')
onkey(turn,"K")
def turn():
	main('L')
onkey(turn,"L")
def turn():
	main('M')
onkey(turn,"M")
def turn():
	main('N')
onkey(turn,"N")
def turn():
	main('O')
onkey(turn,"O")
def turn():
	main('P')
onkey(turn,"P")
def turn():
	main('Q')
onkey(turn,"Q")
def turn():
	main('R')
onkey(turn,"R")
def turn():
	main('S')
onkey(turn,"S")
def turn():
	main('T')
onkey(turn,"T")
def turn():
	main('U')
onkey(turn,"U")
def turn():
	main('V')
onkey(turn,"V")
def turn():
	main('W')
onkey(turn,"W")
def turn():
	main('X')
def turn():
	main('Y')
onkey(turn,"Y")
def turn():
	main('Z')
onkey(turn,"Z")
def turn():
	main('.')
onkey(turn,"period")
def turn():
	main('Tab')
onkey(turn,"Tab")
def turn():
	main('BackSpace')
onkey(turn,"BackSpace")

listen(),done()
