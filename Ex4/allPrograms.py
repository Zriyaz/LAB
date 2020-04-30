'''1. Create a two instance that belongs to the same class and create a one instance method
which is accessed by the both instance of the class'''

class Student:
  Stream="MCA" #class variable 

  def __init__(self,name,roll): #constructor
    #instance variables
    self.name=name
    self.roll=roll
  def details(self):#method
    print("Name :",self.name)
    print("Roll No. :",self.roll)
    print("Branch : ",self.Stream)

  
object1=Student("Riyaz","18mcr014")
object2=Student("Ritesh","18mcr013")
object1.details()
print("============================")
object2.details()

'''2. Write a python program to find the longest words in the text file.'''

with open('text.txt') as file:
  data=file.read().split()
  max=len(max(data,key=len))
  print("Number of Characters : ",max)
  res=[word for word in data if len(word)==max]
  print(res)

'''3. Write a Python program to count the frequency of words in a file.'''
from collections import Counter
def word_count(fname):
  with open(fname) as f:
    return Counter(f.read().split())
print("Number of words in the file :",word_count("text.txt"))

''' 4. program to find the number of rows and columns of a given matrix.'''

import numpy as np
m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the matrix:")
print(m.shape)

'''5. Compare two text files and get the matched strings available in both text file.'''

with open("file1.txt") as f1,open("file2.txt") as f2:
  words=set(line.strip() for line in f1)  
  for line in f2:
    word,freq=line.split() 
    if(word in words):     
      print(word)