import operator
def find_interesction (doc1,doc2):
  union = len(doc1.union(doc2))
  interect = len(doc1.intersection(doc2))

  return(interect/union)
  
def result(input_query,query,doc1,doc2,doc3):
  r1=find_interesction(query,doc1)
  r2=find_interesction(query,doc2)
  r3=find_interesction(query,doc3)
  result = [[1,r1],[2,r2],[3,r3]]
  
  result = sorted(result, key=operator.itemgetter(1),reverse=True)
  print("Results for following query:", input_query)
  print("DocID    Similarity")
  
  print(result[0][0],"        ",result[0][1])
  print(result[1][0],"        ",result[1][1])
  print(result[2][0],"        ",result[2][1])
  


doc1 = "my kingdom for a fox".split() 
doc2 = "rose is a rose is a rose".split()
doc3 = "the quick brown fox jumps over the lazy dog".split()
doc1 = set(doc1)
doc2 = set(doc2)
doc3 = set(doc3)

#quey1
input_query = "a"
query = input_query.split()
query = set(query)
result(input_query,query,doc1,doc2,doc3)
#quey2
input_query = "fox"
query = input_query.split()
query = set(query) 
result(input_query,query,doc1,doc2,doc3)
#quey3
input_query = "rose kingdom"
query = input_query.split()
query = set(query) 
result(input_query,query,doc1,doc2,doc3)







