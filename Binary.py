import sys
import fileinput

## DEBUG: 0 normal mode
##        1 debug mode
DEBUG = 1

#input variables
arguments = sys.argv
count = len(sys.argv)
if(DEBUG == 1):
    print ("This is the name of the script: ", arguments[0])
    print ("Number of arguments: ", count)
    print ("The argusments are: " , str(sys.argv))

def t1():
    q = ["I","am","bread"]
    s = ""
    for i in q:
        s+=i
        s+=" "
    print(s)

def dec7(bin_in):
    file_len = len(bin_in)
    characters = int((file_len)//7)
    message = ""
    Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789:"
    temp_A = 0
    for i in range(characters):
        start = int(7*i)
        end = int(7*i+7)
        curr_b = "0b"+bin_in[start:end]
        curr_d = int(curr_b,2)
        if(DEBUG == 1):
            print (curr_b)
            print ("decimal: {}".format(curr_d))
        #parse
        if(curr_d == 32):
            message += " "
        elif(curr_d == 33):
            message += "!"
        elif(48 <= curr_d and curr_d <= 58):
            temp_A = curr_d-48
            message += number[temp_A]
        elif(65 <= curr_d and curr_d <= 90):
            temp_A = curr_d-65
            message += Alpha[temp_A]
        elif(97 <= curr_d and curr_d <= 122):
            temp_A = curr_d-97
            message += alpha[temp_A]
        elif(curr_d == 8):
            m_len = len(message)
            message = message[0:m_len-1]
        else:
            message += "?"
    return message


def dec8(bin_in):
    file_len = len(bin_in)
    characters = int((file_len)//8)
    message = ""
    Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789:"
    print(len(Alpha))
    print(len(alpha))
    print(len(number))
    temp_A = 0
    for i in range(characters):
        start = int(8*i)
        end = int(8*i+8)
        curr_b = "0b"+bin_in[start:end]
        curr_d = int(curr_b,2)
        if(DEBUG == 1):
            print (curr_b)
            print ("decimal: {}".format(curr_d))
        #parse
        if(curr_d == 32):
            message += " "
        elif(curr_d == 33):
            message += "!"
        elif(48 <= curr_d and curr_d <= 58):
            temp_A = curr_d-48
            message += number[temp_A]
        elif(65 <= curr_d and curr_d <= 90):
            temp_A = curr_d-65
            message += Alpha[temp_A]
        elif(97 <= curr_d and curr_d <= 122):
            temp_A = curr_d-97
            message += alpha[temp_A]
        elif(curr_d == 8):
            m_len = len(message)
            message = message[0:m_len-1]
        else:
            message += "?"
    return message


##START##
if(DEBUG == 1):
    print ("start")
file = sys.stdin
bin_in = file.read()
file_len = len(bin_in)
text = "Filler text"
if(DEBUG == 1):
    print ("Raw text: ")
    print (bin_in)
    print ("Number of bits: {}".format(file_len))
    print ("Mod 7: {}".format((file_len-1)%7))
    print ("Mod 8: {}".format((file_len-1)%8))
if((file_len-1)%7==0):
    if(DEBUG == 1):
        print ("%7%")
    text = dec7(bin_in)
    print (text)
elif((file_len-1)%8==0):
    if(DEBUG == 1):
        print ("%8%")
    text = dec8(bin_in)
    print (text)
else:
    print("incorrect # of bits")
file.close()
if(DEBUG == 1):
    print("end")
