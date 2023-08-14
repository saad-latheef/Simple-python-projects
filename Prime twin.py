s=4
q=0
l=[]
n=int(input('Enter last limit:--->'))
while s<n:
    for i in range(2,s-1):
        if s%i==0:
            q+=1
    if q==0:
        l.append(s)
    else:
        q=0
    s+=1
print([5,3])
for i in range(len(l)):
    if l[i]-2==l[i-1]:
        p=[l[i],l[i-1]]
        print(p)
