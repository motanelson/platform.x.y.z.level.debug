def levels():
    print("0.exit\n1.x+1\n2.x-1\n3.y+1\n4.y-1\n5.z+1\n6.z-1")
    i=int(input("? "))
    return i
x=0
y=0
z=0
files=input("give me the name of map .txt level")
f1=open(files,"r")
level=f1.read()
f1.close()
l=level.split("|")
ttrue=True
xback=x
yback=y
zback=z
ll=[]
lll=[]
zsize=len(l)-1
while ttrue:
    xback=x
    yback=y
    zback=z
    a=levels()
    ll=l[z].split("\n")
    lll=ll[y]
    if a==0:
        ttrue=False
    elif a==1:
        x=x+1
    elif a==2:
        x=x-1
    elif a==3: 
        y=y+1
    elif a==4:
        y=y-1
    elif a==5:
        z=z+1
    elif a==6:
        z=z-1
    try:
        ll=l[z].split("\n")
        lll=ll[y]
        if y<0:
            x=xback
            y=yback
            z=zback
            print("out of board")
    
        elif x<0:
           x=xback
           y=yback
           z=zback
           print("out of board")
        elif z<0:
            x=xback
            y=yback
            z=zback
            print("out of board")
        ll=l[z].split("\n")
        lll=ll[y]

        if z>zsize:
            x=xback
            y=yback
            z=zback
            print("*out of board")
        ll=l[z].split("\n")
        lll=ll[y]
        if y>len(ll)-1:
            x=xback
            y=yback
            z=zback
            print("out of board")
        ll=l[z].split("\n")
        lll=ll[y]
        if x>len(lll)-1:
           x=xback
           y=yback
           z=zback
           print("out of board")
    

        ll=l[z].split("\n")
        lll=ll[y]
    
        
    except:
        x=xback
        y=yback
        z=zback
        print("out of board")
        ll=l[z].split("\n")
        lll=ll[y]

    print("X:"+str(x)+",Y:"+str(y)+"Z:"+str(z)+"\nroom:"+lll[x])