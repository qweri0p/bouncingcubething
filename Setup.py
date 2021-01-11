import platform
import os
OperatingSys = platform.system()
if OperatingSys == "Linux":
    os.system("clear")
elif OperatingSys == "Windows":
    os.system("cls")
print("Would you like to install pygame? [y/n]")
pygameSetup = input()
if pygameSetup == ("y") or pygameSetup == ("yes"):
    if OperatingSys == "Linux":
        os.system("pip3 install pygame")
    else:
        os.system("pip install pygame")