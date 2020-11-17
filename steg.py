import sys

if len(sys.argv) >4:    
    storeType = sys.argv[1][1:]
    mode = sys.argv[2][1:]
    offset = int(sys.argv[3][2:])
    if mode == "B":
        interval = int(sys.argv[4][2:])
        wFile = (sys.argv[5][2:])
        wData = bytearray(open(wFile,"rb").read())
        if storeType == "s":
            hFile = sys.argv[6][2:]
            hData = bytearray(open(hFile,"rb").read())
        else:
            hFile = ""
            hData = ""
    elif mode == "b":
        interval = 1
        wFile = (sys.argv[4][2:])
        wData = bytearray(open(wFile,"rb").read())
        if storeType == "s":
            hFile = sys.argv[5][2:]
            hData = bytearray(open(hFile,"rb").read())
        else:
            hFile = ""
            hData = ""
    
    
senti = bytearray([0x0,0xff,0x0,0x0,0xff,0x0])
if storeType == "s":
    if mode =="B":
        for i in range(0,len(hData)):
            wData[offset] = hData[i]
            offset += interval
        for i in range(0,len(senti)):
            wData[offset] = senti[i]
            offset += interval
        sys.stdout.buffer.write(wData)
    elif mode =="b":
        for i in range(0,len(hData)):
            for j in range(0,8):
                wData[offset] &= 254
                wData[offset] |= ((hData[i] & 128) >> 7)
                hData[i] = (hData[i] << 1)& (2**8 - 1)
                offset += interval
        for i in range(0,len(senti)):
            for j in range(0,8):
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
                for i in range(0,count):
                    sys.stdout.buffer.write(bytes([senti[i]]))
                sys.stdout.buffer.write(bytes([wData[offset]]))
                offset += interval
                count = 0
            else:
                count+= 1
                offset += interval
                
    elif mode =="b":
        count = 0
        while(count!=6 and offset+8<len(wData)):
            data = 0
            for j in range(0,8):
                data |= (wData[offset] & 1)
                if j < 7:
                    data <<= 1
                    offset += interval
            if data != senti[count]:
                for i in range(0,count):
                    sys.stdout.buffer.write(bytes([senti[i]]))
                sys.stdout.buffer.write(bytes([data]))
                #print(data,end=" ")
                offset += interval
                count = 0
            else:
                count+= 1
                offset += interval
        #print(count)
