```python
import os
import csv
import math as mt
```


```python
pwd
```




    'C:\\Users\\Bill\\Desktop\\GT Data Bootcamp\\Git Hub Submission\\Python-Challenge\\PyRoll'




```python
inpath = os.path.join("..","PyRoll","Resources","election_data.csv")
inpath
```




    '..\\PyRoll\\Resources\\election_data.csv'




```python

```


```python
with open(inpath,  mode='r', encoding='ISO 8859-1') as csvfile:
    votereader= csv.reader(csvfile, delimiter=',')

    voteheader= next(votereader)
    each_vote = []
    third_col = []
    vote_ls=[]
    candidate = []
    name_count = 0
    linecount = 0 
    percent_l=[]
    
    nX =0
    nY =0
    y=0
    per_cand=0
    z=0
    w=0
   
  
    
    for line in votereader:
        linecount = linecount + 1  
        third_col.append(line[2])
        if line[2] not in candidate:
            candidate.append(line[2])
            name_count =name_count +1
            #x is a placeholder a string
            if x == candidate[y]:
                #a failed experiment that gave a successful result of other many many many previous failed experiments 
                nX= nX
                #each_vote= sum(nx)
                #another test hope for this result vote_ls=[nX, nX, nX] 
                
                #vote_ls.append(sum(each_vote))
                each_vote.append(nX)
                percent_l.append(nX)
            else:
                y= y+1
                if y == name_count :
                    break
  
    for string in third_col:
        for nY in range(0, name_count):
            
            if string == candidate[nY]:
                per_cand = per_cand+1
                each_vote[nY] += per_cand 
            else:
                nY= nY +1
                per_cand = 0 
                if nY == name_count:
                    break
                    
                    
# for reason unknown to me three elements of the each_vote is correct except the first one
each_vote[0]= linecount- (each_vote[1] + each_vote[2] + each_vote[3])


#Time for MATHHHHH, Yeah, finally a simple action

#percen
len(third_col)

#header
print("Election Results")
print("---------------------------------------------------")
#Total Vote
print(f'Total Votes: {linecount} ')
print("---------------------------------------------------")

#Canditate

for z in range(0,name_count):
    print(f'{candidate[z]}: { "{:.3%}".format(each_vote[z]/linecount)} ({each_vote[z]})')
print("---------------------------------------------------")
if each_vote[w] is max(each_vote):  
    print(f"Winner: {candidate[w]}")
print("---------------------------------------------------")
#name_count  
#each_vote[0]
###################################
#print(f'Total candidate {len(candidate)}')
#print(f'{candidate[0]}: ({each_vote[0]})')
#print(f'{candidate[1]}: ({each_vote[1]})')
#print(f'{candidate[2]}: ({each_vote[2]})')
#print(f'{candidate[3]}: ({each_vote[3]})')

#################################


#print(f'{candidate[0]} received {votes} ')
#percent_l
#each_vote
#per_cand
#y
#vote_first
#vote_ls
#candidate

#vote_dict
#print(candidate[0] =)
##print(candidate[0] =)
##print(candidate[0] =)
##print(candidate[0] =)
```

    Election Results
    ---------------------------------------------------
    Total Votes: 3521001 
    ---------------------------------------------------
    Khan: 63.000% (2218231)
    ---------------------------------------------------
    Correy: 20.000% (704200)
    ---------------------------------------------------
    Li: 14.000% (492940)
    ---------------------------------------------------
    O'Tooley: 3.000% (105630)
    ---------------------------------------------------
    Winner: Khan
    


```python
#####/ lessions for today: BBBRRREAK. When "index is out of range": REMEMBER BREAK BREAK BREAK. Forgot about manupilating. Set a limit then BREEAK.
#####/ ATTRIBUTESSSSS. APPEND add aother element to [(),(),(),(),)_(,,,,,,[ITS END]]
######/ += addddded an number to to vbox[#]
```


```python
####/ I spent a combined more than 13 hours on this homework, more than seven is sitting in front of trying to get the list each vote to show up. 
#So blooody me, for not not remembering thought process 
```


```python
#linecount is total vote
# use a code from the net ".add"/#use another method that is similar
#line[2] is coloumn three, we need to know how many of this equal
#using count? using what I do in bank?
#i use several variable to keep track of it num_candiate to count the candidate[], votes to count the vote each, lets tried the next method
#after many speelingg errors I have got an unhasable type for some reason.
#so I change the list to a tuple but then it se
#Test 5 : lets try zip

```


```python
#the first war for row in third_col:
        #if row == candidate[0]:
            #vote_per_candidate = vote_per_candidate + 1
#####/ Long way to create a list with the same amount as the number of the name. Smell of an amateur
        
```
