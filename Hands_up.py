def get_positions(n):
    human1=0 #0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2      [0]
    human2=0 #0 0 0 1 1 1 2 2 2 0 0 0 1 1 1 2 2 2 0 0 0 1 1 1 2 2 2      [1]
    human3=0 #0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 0-26 [2] 
    arg=n//27
    tmp=n-(27*arg)
    a=[0,0,0]
    i=0
    while(tmp>0):
        a[i]=(tmp%3)
        tmp=tmp//3
        i+=1
    return (a[0],a[1],a[2])


print(get_positions(4))
