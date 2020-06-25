#c is th input array, an array of 0s and 1s 

n=len(c)
step=0
mylist=[]
while step<n-2:
    if c[step+1]==0:
        if c[step+2]==0:
            step=step+2
        else:
            step=step+1
    else:
        step=step+2
    mylist.append(step)
if step+2==n:
    mylist.append(n)
    return len(mylist)
else:
    return len(mylist)
