
failed = True
i = 1

while failed:
    if i%2!=0:
        i=i+1
        continue
    print(f"attempt{i}")
    i=i+1
    if i>100:
        break


    #4th example
i=0
while i<=10:
    print(i)
    i+=1    #i = i+1


    #5th example

failed=True
i=0
while i<=10:
    x=0
    while x<i:
        print("vinod" , end = "-")
        x+=1
    print("")
    i+=1      
