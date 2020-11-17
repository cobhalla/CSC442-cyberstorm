import calendar
import time
import sys
import hashlib

inputTime = sys.stdin.readlines()
epoch = int(time.mktime(time.strptime(inputTime[0].replace('"','').rstrip(),"%Y %m %d %H %M %S")))
#print("Epoch: ",epoch)
if len(inputTime) > 1:
    now = inputTime[1].split(":")
    now = int(time.mktime(time.strptime(now[1][1:],"%Y %m %d %H %M %S")))
else:
    now = int(time.time())

#print("Now: ",now)
diff = ((now - epoch)//60)*60
#print("Diff:",diff)
hashValue = hashlib.md5(str(diff).encode()).hexdigest()
result = hashlib.md5(str(hashValue).encode()).hexdigest()
print(result)
code = list("aa00")
count1 = 0
count2 = 0
for i in range(0,len(result)):
    if ord(result[i]) > 96 and ord(result[i]) < 123 and count1<2:
        code[count1] = result[i]
        count1+=1
    if ord(result[len(result)-i-1]) > 47 and ord(result[len(result)-i-1]) < 58 and count2<2:
        code[count2+2] = result[len(result)-i-1]
        count2+=1
    if count1+count2 >3:
        break
middle = [code[1],code[2]]
print("Time lock code:",''.join(code))
print("The XXXXYZ:",''.join(out),''.join(middle))
