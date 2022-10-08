# Write a Python script to remove all non int values from a list.
a,l=['Java','Python','iNeuron','Saurabh Shukla MySirG',3.45,8.9,9,1,3],[]
for e in a:
    if type(e)==int:
        l.append(e)
    else:
        continue
print(l)