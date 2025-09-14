l=sorted([2,2,3,3,1])
c=0
for i in range(len(l)):
    print("___________")
    print("i:", l[i])
    print("___________")
    for j in range(i+1,len(l)):
        print("j:",l[j])
        if l[i]==l[j]:
            c=c+1
            d={i:j}


