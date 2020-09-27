#Code to find out sum of degits after decimal point
T = int(input("Enter the no. of testcase: "))
for  t in range(T):
    #N denotes the number of places after which decimal is to be taken
    N = int(input("Enter the digits: "))
    P,Q =map(int,input().split())
    #value will be rounded up upto Nth decimal place
    x = round(P/Q, N)
    y = int(x)
    #substracing is done inorder to remove the number before decimal place
    j = x - y
    #for loop will bring all the decimal points to integer number
    for i in range(N):
        j = j * 10
        continue
    j = int(j)
    def sum_of(j):
        s = 0
        while j > 0:
            r = j % 10
            s = s + r
            j = j // 10
        return s
    s = sum_of(j)
    print(s)
