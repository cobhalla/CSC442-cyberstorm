import sys
## DEBUG: 1 debug
#         0 normal
DEBUG = 1

num_args = len(sys.argv)

if(num_args > 3):
    print("Invalid arguments")
    exit()

if(sys.argv[1] != "-e" and sys.argv[1] != "-d"):
    print("Please use -e to encrypt and -d to decrypt")
    exit()

def encrypt(user_input, key):
    encoded = ""
    eKey = key.replace(" ","")
    kLen = len(eKey)
    mLen = len(user_input)
    otherchar = 0
    if(DEBUG == 1):
        print ("User Input: {}, E Key: {}".format(user_input,key))
        print ("Key length: {}, Message Length: {}".format(kLen,mLen))
    for i in range(mLen):
        curr_char = user_input[i]
        curr_key_cahr = eKey[(otherchar+i)%kLen]
        curr_char_ord = ord(curr_char)
        curr_key_char_ord = ord(curr_key_cahr)
        if(DEBUG == 1):
            print ("Char: {}, K char: {}".format(curr_char,curr_key_cahr))
            print ("Char ord: {}, K char ord: {}".format(curr_char_ord,curr_key_char_ord))
            print ("i: ".format(int(i)))
        #Capital letter
        if(65 <= curr_char_ord and curr_char_ord <= 90):
            c_ord = curr_char_ord - 65
            key_ord = curr_key_char_ord - 65
            e_char_ord = ((c_ord + key_ord) % 26) + 65
            print("HI:"+chr(e_char_ord))
            e_char = chr(e_char_ord)
            if(DEBUG == 1):
                print ("U: {}".format(e_char))
            encoded += e_char
        elif(97 <= curr_char_ord and curr_char_ord <= 122):
            c_ord = curr_char_ord - 97
            key_ord = curr_key_char_ord - 65
            e_char_ord = ((c_ord + key_ord) % 26) + 97
            e_char = chr(e_char_ord)
            print("HI:"+chr(e_char_ord))
            if(DEBUG == 1):
                print ("L: {}".format(e_char))
            encoded += e_char
        else:
            encoded += curr_char
            otherchar-= 1
    print ("Out: {}".format(encoded))
    return encoded

def decrypt(user_input, key):
    decoded = ""
    dkey = key.replace(" ","")
    kLen = len(eKey)
    mLen = len(user_input)
    otherchar = 0
    if(DEBUG == 1):
        print ("User Input: {}, D Key: {}".format(user_input,key))
        print ("Key length: {}, Message Length: {}".format(kLen,mLen))
        print ("i: ".format(int(i)))
    for i in range(mLen):
        curr_char = user_input[i]
        curr_key_cahr = eKey[(otherchar+i)%kLen]
        curr_char_ord = ord(curr_char)
        curr_key_char_ord = ord(curr_key_cahr)
        if(DEBUG == 1):
            print ("Char: {}, K char: {}".format(curr_char,curr_key_cahr))
            print ("Char ord: {}, K char ord: {}".format(curr_char_ord,curr_key_char_ord))
            print ("i: ".format(int(i)))
        #Upper Letter
        if(65 <= curr_char_ord and curr_char_ord <= 90):
            char_ord = curr_char_ord - 65
            key_ord = curr_key_char_ord - 65
            d_char_ord = ((char_ord - key_ord+26) % 26) + 65
            d_char = chr(d_char_ord)
            if(DEBUG == 1):
                print ("U: {}".format(d_char))
            decoded += d_char
        #Lower Letter
        elif(97 <= curr_char_ord and curr_char_ord <= 122):
            char_ord = curr_char_ord - 97
            key_ord = curr_key_char_ord - 65
            d_char_ord = ((char_ord - key_ord+26) % 26) + 97
            d_char = chr(d_char_ord)
            decoded += d_char
        else:
            decoded += curr_char
            otherchar -= 1
    print ("Out: {}".format(decoded))
    return decoded
print (sys.argv[1])
while True:
    try:
        # user_input = sys.stdin.readlines()
        user_input = input("Please type your message:\n")
        if(sys.argv[1] == "-e"):
            print ("Encrypting:")
            print (encrypt(user_input, sys.argv[2].upper()))

        elif(sys.argv[1] == "-d"):
            print ("Decrypting:")
            print (decrypt(user_input, sys.argv[2].upper()))
    except Exception as e:
        print ("goodbye")
# user_input = sys.stdin.readlines()
# if(sys.argv[1] == "-e"):
#     sys.stdout.write(encrypt(user_input, sys.argv[2].upper()))
#
# elif(sys.argv[1] == "-d"):
#     sys.stdout.write(decrypt(user_input, sys.argv[2].upper()))
