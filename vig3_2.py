alpha = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0987654321.,?!+='":;@#$%*'''
aLen = len(alpha)
keyword = ''' HanGiNgG4rd3ns'''
kLen = len(keyword)
msg='''"k/U4Zc CJLbx5"A-}Dq{o,p(PM^y)>lQBY%2Kz`[F.'rXd~vE*=s081_G#?96jVmHR3TeS<@+]f:gOhW;w!a7Inu|i&$Nt'''

#print (msg)
def decrypt():
    decoded = ""
    mLen = len(msg)
    print("Length",mLen)
    skipChar = 0
    #decoded = ""print(h,keyword[h])
    for i in range(0,mLen):
        curr_key_cahr = keyword[((i-skipChar)%kLen)]
        curr_key_ord = alpha.index(str(curr_key_cahr))
        #print(i,h,curr_key_cahr,curr_key_ord)
        curr_char = msg[i]
        if(curr_char not in alpha):
        #if(curr_char == '[' or curr_char == ']' or curr_char == '{' or curr_char == '}' or curr_char == '-'):
            decoded += curr_char
            skipChar+=1
            #print(curr_char,"a")
        else:
            curr_char_ord = int(alpha.index(str(curr_char)))
            cypher_char_ord = (curr_char_ord - curr_key_ord) % aLen
            #print(curr_char,curr_char_ord,"b")
            cypherChar = alpha[cypher_char_ord]
            #print ("Cypher:",cypherChar)
            decoded += cypherChar
    #print(decoded)
    return decoded
print(decrypt())
