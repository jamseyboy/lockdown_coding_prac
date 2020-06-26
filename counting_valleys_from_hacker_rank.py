#input is n,s
#the string of steps s and number of steps taken n 
step=0
mylist=[]
valley=0
for x in s:
    if x=='U':
        step=step+1
    if x=='D':
        step=step-1
    mylist.append(step)
for x in range(len(mylist)):
    if mylist[x]==0:
        if mylist[x-1]<0:
            valley=valley+1
return valley

