# Write a Python script to find the smallest number in a given list of numbers.
l,n=[],int(input("Enter how many numbers you want to store : "))
i=1
while(i<=n):
    l.append(int(input("Enter a number : ")))
    i=i+1
print("Minimum number is : ",min(l))