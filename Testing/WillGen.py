from mako.template import Template #templating software
from mako import lexer, codegen
from mako.lookup import TemplateLookup
from sys import argv, exit # input arguments
import csv
import re #regular expression

def willGen():
    indata = open(argv[1]) #collecting the argument data
    custdata = csv.reader(indata) #converting csv data into matrix
    temp = open(argv[2]) #opening template
    text = temp.read() #reading template

    symbols = {
        '&nbsp;' : ' ',
        '&lt;' : '<',
        '&gt;' : '>',
        '&amp;' : '&',
        '&quot;' : '"',
        '&apos;' : '\'',
        f'</span><span>&rdquo;</span><span class="c3">'  : '"',
        f'&rdquo;' : '"',
        f'&ldquo;' : '"',
        f'</span><span>&ldquo;</span><span class="c3">' : '"'}

    for sym, ch in symbols.items():
        text = text.replace(sym, ch)
    #print(text)

    #creating the dictionary that contains the replacement to the template fields
    tags = {}
    for data in custdata:
        type = data[0].lower()
        if type == 'string':
            tags[data[1]] = data[2]
        elif type[0:3] == 'int':
            tags[data[1]] = int(data[2])
        elif type == 'list':
            tags[data[1]] = []
            for i in range(2,len(data)):
                tags[data[1]].append(data[i])
        elif type == 'float':
            tags[data[1]] = float(data[2])
        elif type == 'table':
            dictName = data[1]
            tags[dictName] = {}
            tags[dictName][data[2]] = []
            for i in range(3,len(data)):
                tags[dictName][data[2]].append(data[i])
        elif type == 'row':
            tags[dictName][data[2]] = []
            for i in range(3,len(data)):
                tags[dictName][data[2]].append(data[i])
        else:
            print('First column in csv is invalid. Type must be [int, float, list, string, table, row].')
            exit()
    # print(tags)

    #rendering the template using Mako
    Lookuploc = TemplateLookup(directories=[''])
    mytemplate = Template(filename=argv[2],strict_undefined=True,lookup=Lookuploc)



    if argv[3] == "Debug":
        print(mytemplate.render(**tags))
    else:
        output = open("output" + "." + argv[2].split('.')[1],"w") #opening a file of the same format the tempalate file
        output.write(mytemplate.render(**tags))
    return 0
