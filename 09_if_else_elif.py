    #Let's make a program for grades of students:

x = input ("Enter your marks: ")    #It's upto you wheather you want to decleare variable or you want the user
                                    #to input it...
x= int(x)
# print(type(x))

if   x>= 90:
    print("Congrats! Your Grade is A")
elif x>=80:
    print("Your grade is B")
elif x>=70:
    print("Your grade is C")
elif x>=60:
    print("Your grade is D")    
elif x>=50:
    print("Your grade is E")
else:
    print("You are FAIL!!!!") 


