# Write a Python script to print indices of all occurrences of a given element in a given list.
li,i,l=[],0,["Python","Django","Reactjs","HTML","Python","CSS","Javascript","Python"]
while(i<len(l)):
    if l[i]=="Python":
        li.append(i)
        i=i+1
    else:
        i=i+1
        continue
print("Indices of Python : ",li)