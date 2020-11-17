import sys
import os
import shutil 
if not os.path.exists('files/'):
    os.makedirs('files/')
    
# Command line arguements
if len(sys.argv) >3:    
    storeType = sys.argv[1][1:]
    mode = sys.argv[2][1:]
    wFile = (sys.argv[3][2:])
    wData = bytearray(open(wFile,"rb").read())

hFile = ""
#hData = bytearray(open(wFile,"rb").read())
    

if storeType == "r":
    if mode == "B":
        offsetList = [512,1024,2048,4096,256]
        intervalList = [1,2,4,8,12,16,20,24,32]
    else:
        offsetList = [257,513,1025,2049,4097,1024]
        intervalList = [1,2,3,4]
senti = bytearray([0x0,0xff,0x0,0x0,0xff,0x0])

for x in offsetList:
    for y in intervalList:
        offset = x
        interval = y
        fileName = 'files/Off'+str(offset)+'_Int'+str(interval)+'.txt'
        file = open(fileName,'wb')
        file.close()
        file = open(fileName,'ab')
        if storeType == "s":
            if mode =="B":
                for i in range(0,len(hData)):
                    # Replacing values at index offset with hidden file index data
                    wData[offset] = hData[i]
                    offset += interval
                for i in range(0,len(senti)):
                    # Replacing values at index offset with senti index data
                    wData[offset] = senti[i]
                    offset += interval
                sys.stdout.buffer.write(wData)
            elif mode =="b":
                for i in range(0,len(hData)):
                    for j in range(0,8):
                        # Replacing the least significant bit of wrapper file with offset with hidden file index bit
                        wData[offset] &= 254
                        wData[offset] |= ((hData[i] & 128) >> 7)
                        hData[i] = (hData[i] << 1)& (2**8 - 1)
                        offset += interval
                for i in range(0,len(senti)):
                    for j in range(0,8):
                        # Replacing the least significant bit of wrapper file with offset with senti index bit
                        wData[offset] &= 254
                        wData[offset] |= ((senti[i] & 128) >> 7)
                        senti[i] = (senti[i] << 1)& (2**8 - 1)
                        offset += interval
                sys.stdout.buffer.write(wData)
                
        elif storeType == "r":
            if mode =="B":
                count = 0
                while(count!=6 and offset<len(wData)):
                    if wData[offset] != senti[count]:
                        #checking with senti data, if equals increments the count value and breaks the loop if it matches all senti values
                        for i in range(0,count):
                            #sys.stdout.buffer.write(bytes([senti[i]]))
                            file.write(bytes([senti[i]]))
                        #else write the values to output buffer
                        #sys.stdout.buffer.write(bytes([wData[offset]]))
                        file.write(bytes([wData[offset]]))
                        offset += interval
                        count = 0
                    else:
                        count+= 1
                        offset += interval
                        
            elif mode =="b":
                count = 0
                while(count!=6 and ((offset+8*interval)<len(wData))):
                    data = 0
                    for j in range(0,8):
                        #taking the last bit from wrapper file after offset and constructing the byte
                        data |= (wData[offset] & 1)
                        if j < 7:
                            data <<= 1
                            offset += interval
                    if data != senti[count]:
                        for i in range(0,count):
                            #checking with senti data, if equals increments the count value and breaks the loop if it matches all senti values
                            #sys.stdout.buffer.write(bytes([senti[i]]))
                            file.write(bytes([senti[i]]))
                        #sys.stdout.buffer.write(bytes([data]))
                        file.write(bytes([data]))
                        offset += interval
                        count = 0
                    else:
                        count+= 1
                        offset += interval
        else:
            print("Please provide type (-s or -r)")
        file.close()
