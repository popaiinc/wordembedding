#Wordembedding (BOW) implementation in Python
#rossikamal@gmail.com

import nltk
sent="make america great again"
sent=sent.lower()

from nltk.tokenize import
word_tokenize
result=word_tokenize(sent)
print(result)

count=0
dict={}
for i in range(0,len(result)):
    for j in range(0,len(result)):
          if(result[i]==result[j]):
             count=count+1
          if(count==2)
             dict[result[]]=count
             count=0
          else
             count=0

print(dict)

flag=0
final=[]
for i in range(0,len(result)):
    flag=0
    for j in dict:
          if(result[i]==j):
 		final.append(i)
                flag=1
                break 
          else
                continue
          if(flag==0)
                final.append(0)
print(final)         