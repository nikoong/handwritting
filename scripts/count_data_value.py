with open('/home/nikoong/Algorithm_test/handwritting/data/txt/finish/wrong.txt','r') as f:
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0
    value6 = 0
    value7 = 0
    value8 = 0
    value9 = 0
    value0 = 0
    value_error = 0
    n = 0
    for line in f: 
        n=n+1
        value = line.split(' ')[1].split('\n')[0]
        if value == '1': value1=value1+1
        elif value == '2': value2=value2+1
        elif value == '3': value3=value3+1
        elif value == '4': value4=value4+1
        elif value == '5': value5=value5+1
        elif value == '6': value6=value6+1
        elif value == '7': value7=value7+1
        elif value == '8': value8=value8+1
        elif value == '9': value9=value9+1
        elif value == '0': value0=value0+1
        else: 
            value_error=value_error+1
            print "value_error = ",value
    all_value = value1+value2+value3+value4+value5+value6+value7+value8+value9+value0

    print "value1 = ",value1,"\n" \
"value2 = ",value2,"\n" \
"value3 = ",value3,"\n" \
"value4 = ",value4,"\n" \
"value5 = ",value5,"\n" \
"value6 = ",value6,"\n" \
"value7 = ",value7,"\n" \
"value8 = ",value8,"\n" \
"value9 = ",value9,"\n" \
"value0 = ",value0,"\n" \
"value_error = ",value_error,"\n" \
"all_value = ",all_value,"\n" \
"n = ",n,"\n" \

        


        
 

        
