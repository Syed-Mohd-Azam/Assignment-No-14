# Write a Python script to create a list of first N odd natural numbers.
l,n=[],int(input("Enter the value of n : "))
i=0
while(i<n):
    l.append((2*i+1))
    i=i+1
print(l)