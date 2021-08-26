import os
import pyttsx3
pyttsx3.speak("hello we welcome u to the world of python, tell me how can i help u")
while True:
    p=input("tell us which program u want to run:  ")
    if ("don't" in p) or ("didn't" in p) or ("dont" in p) or ("didnt" in p) or ("shouldn't" in p) or ("shouldnt" in p) or ("wouldn't" in p) or ("wouldnt" in p):
        print("it's ok we understand u")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("chrome" in p):
        os.system("chrome")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("brave" in p):
        os.system("start brave")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("edge" in p):
        os.system("start msedge")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("paint" in p):
        os.system("mspaint")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("calculator" in p) or ("calci" in p)) :
        os.system("calc")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("explorer" in p):
        os.system("explorer")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("character map" in p):
        os.system("charmap")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("cmd" in p) or ("prompt" in p)):
        os.system("cmd") 
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("task" in p) or ("manager" in p)):
        os.system("taskmgr")
    elif (("shut" in p) or ("close" in p) or ("quit" in p) or ("terminate" in p)):
        print("will be waiting for ur visit bye bye!!")
        break
    else:
        print("sorry for the inconvenience can u plz try that again")
