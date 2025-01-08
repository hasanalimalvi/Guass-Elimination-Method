"""
                    *******GUASS ELIMINATION*******
"""
print("             *************GUASS ELIMINATION*************     ")
print("             ******METHOD TO SOLVE LINEAR EQUATIONS*****     ")
print("             *********BUILT BY:HASANALI A. MALVI********     ")
print("             *************ROLL NO.:2103309**************     ")
print("\n")
print("\n")
print("\n")
print("**GIVE INPUT IN THE GIVEN BELOW FORMAT**")
print("\n")
print("a11 a12 a13 ... a1n|b1")
print("a21 a22 a23 ... a2n|b2")
print("a31 a32 a33 ... a3n|b3")
print("...         ...    |..")
print("...         ... ann|bn")
print("\n\n\n")

         

import numpy as np #Using library to find determinant

n=int(input("Enter order of square matrix:"))#Taking value of n from user

B=[] #input of constants of equation

L=[]#Empty list to add rows

for i in range(n):#loop for each row

    R=[]#Empty list to add element in row

    for j in range(n):#loop for each element in row

        print("Enter a"+str(i+1)+str(j+1)+" element:")

        R.append(float(input()))#Taking input of each element and added to Row

    L.append(R)#Adding row to matrix

for b in range(n):#Taking input of constants

    print("Enter b"+str(b+1)+" :")

    B.append(float(input()))#Adding constant to a list



for k in range(n-1): #Main Loop

    Max=abs(L[k][k])#Assuming to be max

    for m in range(k,n-1):#Iterate through each column

        if abs(L[m+1][k])>Max:#Checking Condition

            Max=L[m+1][k]#Changing Max value

            l=L[k]#Storing list to swap

            b=B[k]#Storing constants to swap

            B[k]=B[m+1]#Exhchanging corresponding constant

            B[m+1]=b #Exhchanging corresponding constant

            L[k]=L[m+1]#Exchanging rows

            L[m+1]=l#Exchanging rows
    

    if L[k][k]==0:#Checking condition

        continue #Going to next small matrix

    else:#If condition not fulfilled

        for t in range(k+1,n):#Loop to do elimination

            if L[t][k]==0:#Checking condition

                continue #No need of operation

            else:#Condition not fulfilled

                mult=(L[t][k])/(L[k][k])#Multiplier

                L[t]=[round((L[t][j]-L[k][j]*(mult)),2) for j in range(n)] #Subtraction

                B[t]=round(B[t]-B[k]*mult,2) #Operation on constant



    

X=[] #List for solutions    

a = np.array(L)

d = np.linalg.det(a)#Calculation of Determinant

if d==0:#Checking condition

    print("The solution does not exist.")

else:#If condition is not fulfilled

    for i in range(n): #Loop for iterating through each row

        S=0#Initializing sum for each row

        for j in range(n-1,n-i-2,-1):#Iterating through non zero values of each row

          if j==n-1-i:#Checking condition 

              X.append(round(((B[n-1-i]-S)/L[n-1-i][j]),2))#Adding Solution

          else:#Condition not satisfied

              S=(S+L[n-1-i][j]*X[n-1-j])#Adding Terms in each row other than the variable

if d!=0:#Checking condition of determinant

    print("**COMPARE OUTPUT TO THE GIVEN BELOW FORMAT**")
    print("a11 a12 a13 ... a1n|x1   b1")
    print("a21 a22 a23 ... a2n|x2   b2")
    print("a31 a32 a33 ... a3n|x3 = b3")
    print("...         ...    |..   ..")
    print("...         ... ann|xn   bn")
    print("\n\n")

    for x in range(n):#Iterating through each value of x

        print("x"+str(x+1)+" = ",end="")

        if X[n-x-1]==-0.0:#While sometimes it prints -0.0 so to avoid this

            print(int(X[n-x-1]))

        else:#Else its okay if no problem with it

            print(X[n-x-1])

    print("**ABOVE SOLUTION IS APPROXIMATELY CALCULATED**")


"""
                                                   BUILT BY:HASANALI A. MALVI
                                                   ROLL NO.:2103309
"""


        
          

    






            

            

            

            

            
        
    

        



    
        

    



        
    

        



    
        

    



        
