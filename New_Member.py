def openOrSenior(data):
    for i in range(len(data)):
        a=data[i]
        if(a[0]>=55)and(a[1]>7):
            data[i]="Senior"
        else:
            data[i]="Open"
    return data