#if-else-elif

x=10
if x==10:
    print("yes x is 10")

#example if-else

y=24
if y%24==0:
    print("y is even")
else:
    print("y is odd")    

#if-else-elif
signal=input("what's the colour of the signal : ")
if signal=="red":
    print("STOP")
elif signal=="yellow":
    print("READY")
else:
    print("GO")    

#attendence

att=75
is_teacher_frnd=True
if att>=75:
    print("EXAM")
elif att<=75 and is_teacher_frnd==True:
    print("EXAM")
else:
    print("NO EXAM")

#bus ticket example

gender=input("gender>> ")
age=int(input("age>> "))
if gender == "female" :
    print("Ticket is free")
else:
    if age < 5:
        print("Ticket is free ")
    elif age <= 12:
        print("You get a child discount ")
    elif age >= 60:
        print("You get a senior citizen discount ")
    else:
        print("You pay the full fare ")