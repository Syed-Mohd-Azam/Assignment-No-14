# Write a Python script to create a list of first N even natural numbers.
l,n=[],int(input("Enter the value of n : "))
i=1
while(i<=n):
    l.append((2*i))
    i=i+1
print(l)