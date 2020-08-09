'''This verson uses the input of a csv file , template from text and output as text'''
from sys import argv
import csv
import re

indata = open(argv[1])
custdata = csv.reader(indata)
temp = open(argv[2])
text = temp.read()

result = re.findall('{(.*?)}', text)
tags = {}

for word in result:
    tags[word] = 1

for data in custdata:
    if data[0] in tags:
        tags[data[0]] = data[1]

out = open('output.txt', 'w+')

for ele in tags:
    text = text.replace('{' + ele + '}', tags[ele])
############################################################
options = re.findall('<<(.*?)>>',text)
condition = re.search('_.*?_',options[0])
print(options[0])
condit = condition[0]
condit = condit.replace('_','')
list = re.split("\s", condit)
print(list)
for i in list:
    for word in tags:
        if word == i:
            print('working')
            condit1 = condit.replace(word, tags[word])
            if exec(condit1):
                print('working')
                repl = options[0].replace(condit,'')
                text = text.replace(options[0],repl)

############################################################
out.write(text)

out.close()
temp.close()
indata.close()
