import math
def is_legal_region(kmap_function, term):
    l=[]
    n=len(kmap_function)
    my=len(kmap_function[0])
    k1=int(math.log(n)/math.log(2))
    k2=int(math.log(my)/math.log(2))
    #no. of variables=k1+k2
    if k1==1:
        var1=["0","1"]
        if k2==1:
            var2=["0","1"]
        elif k2==2:
            var2=["00","01","11","10"]
    elif k2==2 and k1==2:
        var1=["00","01","11","10"]
        var2=["00","01","11","10"]
    m=[]
    w=[]
    for i in range(len(var1)):
        for j in range(len(var2)):
            w.append(var2[j]+var1[i])     
        m.append(w)
        w=[]
    #print(m)
    s=""
    for t in term:
        if t==None:
            s+=("N")
        else:
            s+=(str(t))
    #print(s)
    op=[]
    opq=[]
    for q in range(len(m)):
        for y in range(len(m[q])):
            saesha= True
            for j in range(len(s)):
                if s[j]!="N":
                    if s[j]!=(m[q][y])[j]:
                        saesha=False
                        break
            if saesha==True:
                op.append((q,y))
                opq.append(kmap_function[q][y])
    #print(op)
    #print(opq)
    leftcoordinate=0
    rightcoordinate=0
    for i in range(len(op)):
        leftx=0
        lefty=0
        j=0
        while (j<len(op) and (leftx<1 or lefty<1)):
            if (i!=j and ((op[i])[0]+1)%n==(op[j])[0]):
                leftx=1
            if (i!=j and (((op[i])[1]+1)%my==(op[j])[1])):
                lefty=1
            j+=1
        if (leftx==1 and lefty==1):
            leftcoordinate=op[i]
            break
    for i in range(len(op)-1,-1,-1):
        rightx=0
        righty=0
        j=0
        while (j<len(op) and (rightx<1 or righty<1)):
            if (i!=j and ((op[i])[0]-1)%n==(op[j])[0]):
                rightx=1
            if (i!=j and ((op[i])[1]-1)%my==(op[j])[1]):
                righty=1
                
            j+=1
        if (rightx==1 and righty==1):
            rightcoordinate=op[i]
            break
    Legalvalue=True
    for i in opq:
        if i==0:
            Legalvalue=False
            break
    return(leftcoordinate,rightcoordinate,Legalvalue)
#print(is_legal_region([[0,1],[1,1]],[0,None]))

print(is_legal_region([[0,1,1,0],["x",1,"x",0]],[None,0,None]))
#fault when one row selected