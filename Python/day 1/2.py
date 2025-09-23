a={}
b=[]
l=[1,1,2,3,1,1,1,2,2,2,1]
t=len(l)/2
for i in l:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
for i in a:
    b.append(a[i])
if max(b)>t:
    print(max(b))
else:
    print(None)