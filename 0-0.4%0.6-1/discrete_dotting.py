from decimal import *
import random
wl = 16  #word length is 16 bit

###   Part 1: Read sensitivity map from s_map.txt  ###
# One thing to be noticed here. The precision of decimal number is 28 digits by default. Please do not worry about the precision problem.
s_map = open('s_map.txt','r')
s_value = []
for i in s_map:
    s_value.append(Decimal(i))
s_map.close()
#print s_value


###   Part 2: Analyse data; Prepare for dotting
# Read from txt. Analyse data.
coe_txt = open('coeff.txt','r')
coeff = list()
for line in open('coeff.txt'):
    line = coe_txt.readline()
    line = line.strip("\n")
    coeff.append(line)
coe_txt.close()

count = 0
digits = 4 

coeff_status = 0
search_list = []

i = 3

# get search list for further use
while i <64:       #the number can be changed, depends on how many common blocks you want to search, in current situation, all common blocks within 6 digits will be searched.
    binary = "{0:b}".format(i)
    search_list.append(binary)
    i +=1

#  Before random dotting, check inital coeff complexity for reference.
coe_str = ''
for coe in coeff:
    coe_str = coe_str + coe + ' '
coe_len = len(coeff[0])
evaluate = 0
testing = coe_str

for block in search_list:
    block_len = len(block)
    tar = 'x'*block_len
    zeros = block.count('0')
    block_c = (wl-1)*len(block)-zeros*wl       #block complexity
    block_num = 0
    
    testing = testing.replace(block,tar)
    current = testing.split()
    for i in current:
        appearance = 0    #for common blocks in one coeff
        if i.count(tar) > 0:
            appearance += 1
            block_num+=1
        if i.count(tar) > block_len:
            previous = (wl-1)*len(i)-i.count('0')*wl-block.count('0')*i.count(tar)/block_len*wl
            now = block_c + (i.count(tar)/block_len+i.count('1')-1)*15-i.count('0')*16
            evaluate = previous-now
    if block_num > 0:
        evaluate += max(block_c*(block_num-1)-(len(block)+wl-1)*(block_num-1),0)
    testing = testing.replace('x','a')    
    block_num = 0
best = evaluate
print best
"""
Current Method
Evaluate complexity via FA/FF method (Can be proved, which I've done once. It would be too long to write everything here)
Basic rules: When common blocks appear in two different coeffs but only appear for one time, there is a low chance to get efficiency increase (depends on how many 1 appears)
Any common blocks appear in one coeff increase the efficiency. (more 1, more efficient)
In the following code, evaluate will give how many FA/FF cost can be saved (briefly). 
"""
###   Part 3: Random dotting
while (coeff_status <= 1000):
    coe_str = ''
    exp_coe = list()
    binary = ''
    while count < len(s_value):
    #To be notice, here the method can be improved
        if s_value[count]>=0:  #Random dotting to increase the value of this number
            coe = coeff[count]

            last = coe[-digits:]
            last = int(last,2)
            ceil = 2**digits-1-last
            ceil = max(2,ceil)
            last = last + random.randint(1,ceil)
            last = "{0:b}".format(last)
            while len(last)<digits:
                last = '0'+last #make sure that all binary numbers have same digits
            coe = coe[:-digits] + last
        else:
            coe = coeff[count]
            last = coe[-digits:]
            last = int(last,2)
            last = random.randint(0,last)
            last = "{0:b}".format(last)
            while len(last)<digits:
                last = '0'+last
            coe = coe[:-digits] + last
        count +=1
        exp_coe.append(coe)        # this would be the coeff that are needed to be tested in the next step
    ### Then check complexity
    count = 0
    evaluate = 0
    # Step 0-1, copy elements into a string, as well as result list
    for coe in exp_coe:
        coe_str = coe_str + coe + ' '
    coe_len = len(exp_coe[0])
    # Step 1, evaluate which common block should be replaced in the first place.
    testing = coe_str
    for block in reversed(search_list):
           #Generally, searching longer blocks in the first place will bring a better result, as shorter blocks may cut the longer blocks
        block_len = len(block)
        tar = 'x'*block_len
        zeros = block.count('0')
        block_c = (wl-1)*len(block)-zeros*wl       #block complexity
        testing = testing.replace(block,tar)
        current = testing.split()
        block_num = 0         #for common blocks in different coeffs
        for i in current:
            appearance = 0    #for common blocks in one coeff
            if i.count(tar) > 0:
                appearance += 1
                block_num+=1
            if i.count(tar) > block_len:
                previous = (wl-1)*len(i)-i.count('0')*wl-block.count('0')*i.count(tar)/block_len*wl
                now = block_c + (i.count(tar)/block_len+i.count('1')-1)*(wl-1)-i.count('0')*wl
                evaluate = previous-now
        if block_num > 0:
            evaluate += max(block_c*(block_num-1)-(len(block)+wl-1)*(block_num-1),0)
        block_num = 0
        
        testing = testing.replace('x','a')
    coeff_status+=1
    if evaluate > best:
        print "better"
        best = evaluate
        coeff_best = list(exp_coe)
        coeff_status = 0
        
print "finished"
print coeff_best
print best

