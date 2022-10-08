# Write a Python script to find the greatest number in a given list of numbers.
l,n=[],int(input("Enter how many numbers you want to stoe in a list : "))
i=1
while(i<=n):
    l.append(int(input("Enter a number : ")))
    i=i+1
print("Maximum number is : ",max(l))