import os
from colorama import Fore
import time 

count = 0
for folders in os.listdir(os.getcwd()):
        if os.path.isdir(folders):
            count = count + 1
            with open("folders.txt", "a+") as folder_file:
                folder_file.write("{}\n".format(folders))
            print(folders)
print("\nDone, found {} folders.".format(count))
time.sleep(30)            
