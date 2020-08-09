'''This verson uses the input of a txt file , template from text and output as text'''
from sys import argv

def readData():
    return input.readline().replace("\n", "")

input = open(argv[1])


name = readData()
age = readData()
title = readData()
address = readData()
phno = readData()

input.close()
temp = open(argv[2])

out = open('output.txt', 'w+')

out.write(temp.read().format(age=age,name=name,title=title,address=address,phno=phno))

out.close()
temp.close()
