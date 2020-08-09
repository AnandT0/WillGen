from mako.template import Template #templating software
from mako import lexer, codegen
from mako.lookup import TemplateLookup
from sys import argv # input arguments
import csv
import re #regular expression
'''I made this as a funtion so that i can try to import the code into a different file, but this method is really crude
and will need to be worked on. The function currently takes the template file and outputs the filled in template to the
console'''
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
    print(text)

#This is copied code from the internet to capture the names of the fields in the template
    lex1 = lexer.Lexer(text)
    node = lex1.parse()

    compiler = lambda: None
    compiler.reserved_names = set()

    identifiers = codegen._Identifiers(compiler, node)
    tagstemp = identifiers.undeclared
#End of the copied code
    #creating the dictionary that contains the replacement to the template fields
    tags = {}

    for data in custdata:
        if data[0] in tagstemp:
            tags[data[0]] = data[1]
    #print(tagstemp)
    #print(tags)

    #rendering the template using Mako
    Lookuploc = TemplateLookup(directories=[''])
    mytemplate = Template(filename=argv[2],strict_undefined=True,lookup=Lookuploc)



    if argv[3] == "Debug":
        print(mytemplate.render(**tags))
    else:
        output = open("output2" + "." + argv[2].split('.')[1],"w") #opening a file of the same format the tempalate file
        output.write(mytemplate.render(**tags))
    return 0

#calling the above written funtion
#
