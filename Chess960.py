def is_valid(positions:str)->bool:
    i=0
    a=list(positions)
    R1_index=0
    R2_index=0
    countR=0
    N1_index=0
    N2_index=0
    countN=0
    B1_index=0
    B2_index=0
    countB=0
    Q_index=0
    K_index=0
    for i in range(len(a)):
        if(a[i]=="R")and(countR==0):
            R1_index=i
            countR+=1
        elif(a[i]=="R"):
            R2_index=i
        elif(a[i]=="N")and(countN==0):
            N1_index=i
            countN+=1
        elif(a[i]=="N"):
            N2_index=i
        elif(a[i]=="B")and(countB==0):
            B1_index=i
            countB+=1
        elif(a[i]=="B"):
            B2_index=i
        elif(a[i]=="K"):
            K_index=i
        else:
            Q_index=i
    print("B2 = ", B2_index, "\nB1 = ", B1_index )
    if((B2_index-B1_index)%2==0):
        return False
    else:
        if(K_index>R1_index)and(K_index<R2_index):
            return True
        else:
            return False






print(is_valid("QNBNBRKR"))