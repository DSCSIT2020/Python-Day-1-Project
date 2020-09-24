''' Fizz Buzz Game
the number is divisible by 3 and 5 is Fizz Buzz and fizz for 3 and Buzz for 5'''

print("Lets start the Fizz Buzz Game",end='\n\n')
t=int(input("Please enter the end range of the game:"))
p=t+1
p=int(p)
for i in range(1,p):
        if(i%3==0 and i%5==0):
                print(i,"= Fizz Buzz")
        else:
                if(i%3==0):
                        print(i,"= Fizz")
                elif(i%5==0):
                        print(i,"= Buzz")
                else:
                        print(i)
