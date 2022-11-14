def get_winner(ballots):
    mass=[]
    for i in range(len(ballots)):
        if(ballots[i] not in mass):
            mass.append(ballots[i])
    mass_resualt=[]
    for i in range(len(mass)):
        mass_resualt.append(ballots.count(mass[i]))
    max_index=0
    two_max=0
    maximum=0
    for i in range(len(mass)):
        if(mass_resualt[i] > maximum):
            maximum=mass_resualt[i]
            max_index=i
        elif(mass_resualt[i]==maximum):
            two_max=maximum
    if(two_max==maximum):
        return None
    elif(maximum<=len(ballots)/2):
        return None
    else:    
        return mass[max_index]
a=["A", "A", "A", "B", "B", "C"]
print(get_winner(a))