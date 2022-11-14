def pyramid(n):
    if(n==0):
        return []
    elif(n==1):
        return [[1]]
    elif(n>=2):
        a=[[1]*n]
        return pyramid(n-1) + a 
print(pyramid(0))