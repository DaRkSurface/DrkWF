#!/usr/bin/python3

#####################################################
## DarkWifiFetcher (DrkWF)                         ##
## We all are lazy, we're lazy to get our wifi-    ##
## password; You will like my quick project: DrkWF ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
## Languages: Python, Batch                        ##
#####################################################


# Imports
from dataclasses import is_dataclass
import sys
import os
import errno
import ctypes
from colorama import Fore
import time

# Important Defines
def AnyKey():
    anykey = input(f"\n{Fore.YELLOW}Press enter to continue{Fore.LIGHTWHITE_EX}")

def isRoot(): # Returns a True or False boolean  
    try:
        is_admin = (os.getuid() == 0)	# Unix Systems
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0	# Windows Systems
    if is_admin == True:
        print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Administrator Privilage Accessed")
        time.sleep(0.6)
    else:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Need Administrator/Root Access.")
        time.sleep(1)
        AnyKey()
        clearcmd()
        quit()


def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')



# Code


# Main 
if __name__ == "__main__":
    clearcmd()
    isRoot()
    
