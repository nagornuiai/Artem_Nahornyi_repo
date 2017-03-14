def pickup_operator(funcs, operators, error_msgs):
    print "Choose desired operation:\n1. int()\n2. str()\nq -quit()\nm - main menu\n"      
    operator_choosen = raw_input(">>>")
    if operator_choosen == "q":
        quit()
    elif operator_choosen in operators:
        operator_choosen = operators[operator_choosen]
        prompting(funcs, operator_choosen, error_msgs)
    else:
        print "Error #####"
        pickup_operator(funcs, operators, error_msgs)
def prompting(funcs, operator_choosen, error_msgs):
    operation_inp = raw_input("Enter operands:\n>>>")
    if operation_inp == "q":
        quit()
    elif operation_inp == "m": pickup_operator(funcs, operators, error_msgs)
    output = error_catch(funcs, operator_choosen, operation_inp, error_msgs)

def error_catch(funcs, operator_choosen, operation_inp, error_msgs):
    print "[*] error_catch check"
    try:
        print "[*] try:"
        return funcs[operator_choosen](operation_inp)
    except:
        print "[*] except"
        print "Error:", error_msgs[operator_choosen]
        prompting(funcs, operator_choosen, error_msgs)

def intg(var):
    print "[*] intg func accessed"
    var = int(var)
    print "[*] inted"
    print var

def strg(var):
    print "[*] strg func accessed"
    var = str(var)
    print "[*] stringed"
    print var
    
funcs = {"int":intg,"str":strg}
operators = {"1":"int","2":"str"}
error_msgs = {"int": "#001 - Wrong input. int(string) is not allowed.\nUse int(num)",
"str":"#002- Unexpected error. Non-char object can't be str()"}

pickup_operator(funcs, operators, error_msgs)