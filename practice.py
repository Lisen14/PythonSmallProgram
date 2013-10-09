from sys import argv
from ConfigParser import ConfigParser
import os,time

x="test %d test %s" % (123,"123")

y="I said %s" % x

end1="l"
end2="i"
end3="s"
end4="e"
end5="n"

months = "\nJAN\nFeb\nMar\n"
days = "Mon Tue Wed Thu Fri Sat Sun"

print "Here are the days: ", days


for i in ["/","-","|","\\","|"]:
    print "%s\r" % i,


txt = open('test.txt',"w")
txt.close()

def function1(*argc):
    arg1,arg2 = argc;
    print "argc1: %s, argc2: %s" % (arg1,arg2)
    
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    
    
print sort_words(["1","3","2","4"])

CONFIG_FILE="/Users/workProgram/pythonPractice/MonitorFile/config.ini"



print os.listdir(".")


print mktime(time)






