P = int(input("Please enter the total principal amount:"))
r = float(input("Please enter the interest rate (0.00 format):"))
t = int(input("Please enter the term of the loan in years:"))
n = int(input("Please enter the number of interest payments per year:"))

total_paid = P*(1+(r/n))**(n*t)
interest_paid = total_paid - P

print("Principal: " + str(P))
print("Rate: " + str(r))
print("Term: " + str(t))
print("Compound: " + str(n))
print("Total paid after " + str(t) + " years: " + str(total_paid))
print("Interest paid after " + str(t) + " years: " + str(interest_paid))
