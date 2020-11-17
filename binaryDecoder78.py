import sys
def asciiToString(data,datalen):
    stringMessage = ""
    for index in range(0,len(data),datalen):
        temp = data[index:index+datalen]
        temp = int(temp,2)
        print(temp, chr(temp))
        if temp ==8:
            stringMessage = stringMessage[:-1]
        else:
            stringMessage += chr(temp)
    return stringMessage

binData = ""
binData = sys.stdin.readlines()
binData = binData[0][:-1]
'''
if len(binData)%56 == 0:
    print("7-bit:")
    sys.stdout.write(asciiToString(binData,7))
    print("8-bit:")

elif len(binData)%7 == 0:
    print("7-bit:")
    sys.stdout.write(asciiToString(binData,7))
elif len(binData)%8 == 0:
    print("8-bit:")
    sys.stdout.write(asciiToString(binData,8))
    '''
while len(binData)>0:
    sys.stdout.write(asciiToString(binData[0:7],7))
    sys.stdout.write(asciiToString(binData[7:15],8))
    binData = binData[15:]
