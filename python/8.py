#while loop

failed = True
i=1
while failed and i<=100:
    print(f"attempt{i}")
    i = i+1
print("i never gave up!")    

#2nd example

failed = True
i = 1
while failed:
    print(f"attempt{i}")
    i = i+1
    if i>100:
        break
print("i gave up!")   

#3rd example

while failed:
    if i%2!=0:
        i=i+1
        continue
    print(f"attempt{i}")
    i=i+1
    if i>100:
        break