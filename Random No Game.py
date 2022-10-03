import numbers
import random as rm
import threading
import time
class numbers(threading.Thread):
    
    def __init__(self):
        self.list = ['1', '2', '3', '4','5']
        self.computer = []
        self.user = []
        super().__init__()

    def run(self):
        print("Selection starts")
        while (len(self.list) != 0):

            n = rm.choice(self.list)
            self.list.remove(n)
            self.computer.append(n)
            time.sleep(10)

        if(len(self.user)> len(self.computer)):
            print("User wins")
        else:
            print("computer wins")

M=numbers()

M.start()

while(len(M.list)!=0):
    print(M.list)
    p=input("Enter your No :- ")
    if p in M.list:
        M.user.append(p)
        M.list.remove(p)
        time.sleep(5)
    else:
        print("Wrong No choosen")

if(len(M.user)> len(M.computer)):
            print("User wins")
else:
            print("computer wins")
