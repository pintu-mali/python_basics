import os
import pyttsx3
pyttsx3.speak("welcome to python")
print()
print("Press 1:To open chrome browser")
print("Press 2:To open brave browser")
print("Press 3:To open notepad")
print()
p=int(input("enter your choice: " ))

if p==1:
	os.system("chrome")
elif p==2:
	os.system("start brave")
elif p==3:
	os.system("notepad")
else:
	print("invalid input")