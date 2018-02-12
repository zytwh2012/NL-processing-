query = ["$au","aut","uto","tom","omo","mob","obi","bil","ile","le$"]
doc1="$that$angry$mob$is$back$"
doc2="$used$automobiles$for$sale$"
doc3="$meet$at$the$auto$shop$"

d1=[]
d2=[]
d3=[]

i=0
while i+2<len(doc1):
  d1.append(doc1[i]+doc1[i+1]+doc1[i+2])
  i+=1
  
i=0
while i+2<len(doc1):
  d2.append(doc2[i]+doc2[i+1]+doc2[i+2])
  i+=1
  
i=0
while i+2<len(doc3):
  d3.append(doc3[i]+doc3[i+1]+doc3[i+2])
  i+=1

print(d1,"d1\n")
print(d2,"d2\n")
print(d3,"d3\n")

doc1=d1
doc2=d2
doc3=d3

query = set(query)
doc1 = set(doc1)
doc2 = set(doc2)
doc3 = set(doc3)

def find_interesction (doc1,doc2):
  union = len(doc1.union(doc2))
  interect = len(doc1.intersection(doc2))
  print(interect)
  print(union)

  print(interect/union)
find_interesction(query,doc1)
find_interesction(query,doc2)
find_interesction(query,doc3)

#sorted number 2