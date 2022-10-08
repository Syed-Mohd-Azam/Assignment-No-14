# Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
l=["Python","Python","iNeuron","MySirG",5,5,8.90,2+4j,2+4j,3+5j,True,False,True,True,False]
s={e for e in l}
for e in s:
    print(e ," :",l.count(e)," times")
print()