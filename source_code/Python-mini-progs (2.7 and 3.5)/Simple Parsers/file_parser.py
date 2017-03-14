#cheaking for user commands
def inp_commands(user_input):
    if "-sw" in user_input: #starts with
        sw = True
    else:
        sw = False
    if "-hi" in user_input: #have key in line
        hi = True
    else: 
        hi = False
    if "-kd" in user_input: #kills duplicates
        kd = True
    else:
        kd = False
    if "-sm" in user_input: #sends me
        sm = True
    else:
        sm = False
    if "-sf" in user_input: #stores file
        sf = True
    else:
        sf = False
    if "-wia" in user_input: #writes in file after previous content
        wia = True
    else:
        wia = False
    return sw, hi, kd, sm, sf, wia

#cheacking if user is ready to run
   
###################################################################################

#queryit for additional input
def querying_user(sw_r, hi_r, sm_r, sf_r, wia_r):
    file_prompt = raw_input("Enter your file:\n>>>")
    if sw_r: 
        sw_q = raw_input("Enter how does line must start with:\n>>>") 
        swd_q = raw_input("Would you like to drop 'starts-with' keyword? [Y/n]\n>>>") #swd_ -> drop starting keyword
        if swd_q.lower() == "y":
            swd_q = True
            skip_len = len(sw_q)
        elif swd_q.lower() == "n":
            swd_q = False
            skip_len = 0
        else:
            swd_q = None
            skip_len = 0
    else: 
        sw_q = None
        swd_q = None
        skip_len = 0
    if hi_r: 
        hi_q = raw_input("Enter keys that must be in line\n>>>") 
    else: 
        hi_q = None
    if sm_r: 
        sm_q = raw_input("Enter e-mail\n>>>") 
    else: 
        sm_q = None
    if sf_r: 
        sf_q = raw_input("Enter a File Name to store the output [-sf]\n>>>") 
    else: 
        sf_q = None
    if wia_r: 
        wia_q = raw_input("Enter a file name to rewrite existing file [-wia]\n>>>")
    else: 
        wia_q = None
    return file_prompt, sw_q, hi_q, sm_q, sf_q, wia_q, swd_q, skip_len # _q is our questions

##################################################################################
    
def parsing_file(opened_file, sw_a, hi_a, sf_a, wia_a, skip_len):
    if sw_r and hi_r:
        for line in opened_file:
            if line.startswith(sw_a) and hi_a.lower() in line.lower():
                print line[skip_len:].strip()
                if sf_a is not None:

                    new_file.write(line[skip_len:].strip()+"\n")

                if wia_a is not None:

                    having_file.write(line[skip_len:].strip()+"\n")

    elif sw_r:
        for line in opened_file:
            if line.startswith(sw_a):
                print line.strip()
                if sf_a is not None:

                    new_file.write(line.strip()+"\n")

                if wia_a is not None:

                    having_file.write(line.strip()+"\n")
                
    elif hi_r:
        for line in opened_file:
            if hi_a.lower() in line.lower():
                print line.strip()
                if sf_a is not None:

                    new_file.write(line.strip()+"\n")

                if wia_a is not None:

                    having_file.write(line.strip()+"\n")
                
    else:
        print "program is looking for nothig, thus session will be closed automaticly."
        quit()
 
        


import os
import os.path
import time
user_input = raw_input("To see all possible arguments -> type 'help()'\nEnter your commands:\n>>>") #prompting user for commands

sw_r, hi_r, kd_r, sm_r, sf_r, wia_r = inp_commands(user_input) #reading and returning commands -> _r is received Boolean from the function
file_name, sw_a, hi_a, sm_a, sf_a, wia_a, swd_a, skip_len = querying_user(sw_r, hi_r, sm_r, sf_r, wia_r) #asking user for details about relative commands -> _a is answer


opened_file = open(file_name)

##Opening sessions right here to keep them global, as well as, to eliminate inefficiency using it in loop body. 
if sf_a is not None: 
    if os.path.isfile(sf_a) is not True:
        new_file = open(sf_a, 'w')
        print "[*] Creating file [-sf]"
        time.sleep(1.0)
        print "[*] Done"
    if os.path.isfile(sf_a):
        print "[*] Creating file [-sf]"
        time.sleep(1.0)
        prompt_file_exists = raw_input("Such file already exists.\nWould you like to write in it? [Y/n]\n>>>")
        if prompt_file_exists.lower() == "y":
            new_file = open(sf_a, 'w')
            print "[*]Done"
            time.sleep(1.0)
        else:
            sf_a = None
if wia_a is not None:
    if os.path.isfile(wia_a):
        print "[*] Accessing having file [-wia]"
        time.sleep(1.0)
        if sf_a is not None:
            prompt_sf_already_rewrited = raw_input("You already rewrited %s. Do you still want to add DATA into another file? [Y/n]\n>>>" % sf_a)
            if prompt_sf_already_rewrited.lower() == "y":
                having_file = open(wia_a, 'a')
                having_file.write("\n")
                print "[*] Done"
                time.sleep(1.0)
            else:
                wia_a = None
        else:
            having_file = open(wia_a, 'a')
            having_file.write("\n")        
    else:
        print "[*] Accessing having file [-wia]"
        time.sleep(1.0)
        prompt_file_isnt_exists = raw_input("Such file is't exist.\nWould you like to create new one? [Y/n]\n>>>")
        if prompt_file_isnt_exists.lower() == "y":
            having_file = open(wia_a, 'a')
            having_file.write("\n")            
        else:
            wia_a = None

print "[*] All done"
time.sleep(0.5)
parsing_file(opened_file, sw_a, hi_a, sf_a, wia_a, skip_len)
print "[*] Parsed"
time.sleep(1.0)
##Closing sessions if condition is met
if sf_a is not None:
    new_file.close()
if wia_a is not None:
    having_file.close()
print "[*] File sessions closed"
print "Have Fun!"




