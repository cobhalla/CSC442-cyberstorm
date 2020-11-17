from pynput.keyboard import Controller, Key
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout


keyboard = Controller()

pword = input()
timings = input()

print("Password:",pword)
print("Timings",timings)

#Splitting the password and saving the actual password
pword = pword.split(",")
pword = pword[:len(pword) // 2 +1]
pword = "".join(pword)
print("Trimed Password:",pword)

#Splitting key press and interval times
timings = timings.split(",")
timings = [float(a) for a in timings]
keyPress = timings[:len(timings) // 2 +1]
keyInterval = timings[len(timings) // 2 +1:]
keyInterval = keyInterval+[0]

#fake typing with key press and key interval times
print("Fake typing:")
for index in range(len(pword)):
    keyboard.press(pword[index])
    sleep(keyPress[index])
    keyboard.release(pword[index])
    sleep(keyInterval[index])
keyboard.press(Key.enter)
keyboard.release(Key.enter)

tcflush(stdout, TCIFLUSH)
