P = int(input("Please enter the total principal amount:"))
A = float(input("Please enter the total amount paid (result from interest.py):"))
t = int(input("Please enter the term of the loan in years:"))
n = int(input("Please enter the number of interest payments per year:"))

r = ((A/P)**(1/(n*t))-1)*n

print("Principal: " + str(P))
print("Total: " + str(A))
print("Term: " + str(t))
print("Compound: " + str(n))
print("The interest rate on a loan for " + str(P) + " that cost " + str(A) + 
      " over " + str(t) + " years is: "+ str(r))
