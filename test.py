import re

from string import maketrans

text=open(r"C:\Users\Yagnik\PycharmProjects\TestProject\test.txt",'r').read()

pattern="\w*Exception"
all= set(re.findall(pattern,text))


for x in all:
    print x

for line in text.split('\n'):
    if re.search("\\w*Exception",line):
        print line
