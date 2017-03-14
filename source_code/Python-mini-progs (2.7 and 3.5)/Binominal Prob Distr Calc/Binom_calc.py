print('Binominal Distribution Caltulator Welcomes You!')

import numpy as np
import matplotlib.pyplot as plt
import math 
def p_calc(mode):
    while True:
        try:
            inp = input('Set p, x, n.\n>>>')
            np_lst = np.array(inp.split(','), dtype='f')
            break
        except:
            print('[*] Wrong input')
            continue
        
    print('input',inp.split(','), type(inp.split(',')))
    print('[*] Input is valid')
    print('Array:')
    print(np_lst)
    p = np_lst[0]
    x = np_lst[1]
    n = np_lst[2]
    if mode == 's':
        p_x_equal_inp = (math.factorial(n) / (math.factorial(x) * math.factorial(n-x)) * p**x * (1-p)**(n-x))
        print(p_x_equal_inp) 
    else:
        check = -1
        mutual_p = 0
        while check != n - x:
            p_x_equal_inp = (math.factorial(n) / (math.factorial(x) * math.factorial(n-x)) * p**x * (1-p)**(n-x))
            mutual_p += p_x_equal_inp
            x += 1
        print(mutual_p) 
    p_hist(p,n)
    
def p_hist(p,n):
    # Setting x-axis
    n = int(n)
    p = float(p)
    x_axis = list(range(n+1))
    print(x_axis)
    # Generating probability distribution
    y_axis = list()
    for x in x_axis:
        print('input for calculation:', p, x , n)
        y_axis.append((math.factorial(n) / (math.factorial(x) * math.factorial(n-x)) * p**x * (1-p)**(n-x)))
        print('Calculation output fo iteration:', round((math.factorial(n) / (math.factorial(x) * math.factorial(n-x)) * p**x * (1-p)**(n-x)),5))
    data_frame = np.vstack((x_axis,y_axis)).T
#    data_frame = np.array(y_axis).T
    print(data_frame[:,1])
    plt.hist(data_frame[:,1], bins=n+1)
    plt.show()
        
while True:
    inp = input("simple or complex? [S\C] q - for quit\n>>>")
    if inp.lower() == 's': 
        arg = 's'
        break
    elif inp.lower() == 'c': 
        arg = 'c'
        break
    elif inp.lower() == 'q' : quit()
    else: continue
p_calc(arg)
