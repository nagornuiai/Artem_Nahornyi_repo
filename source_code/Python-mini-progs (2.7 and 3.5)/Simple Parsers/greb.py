import re
working_file = open("short-mbox.txt")
comm = raw_input("Enter your commands:\n>>>") 
com = raw_input("Enter your commands:\n>>>") 
count = 0 
for line in working_file:
    print line
    if re.search(comm, line):
        print re.search(comm, line)
        print "[*] OK"
        try:
            tmp = re.findall(com, line)
            print tmp
        except:
            continue
try:
    print tmp
except:
    quit()

