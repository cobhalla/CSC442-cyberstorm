from sys import stdin, stdout

key = bytearray(open("key3","rb").read())
mesg = bytearray(stdin.buffer.read())
for i in range(0,len(mesg)):
    temp = bytes([mesg[i]^key[i%len(key)]])
    stdout.buffer.write(temp)
