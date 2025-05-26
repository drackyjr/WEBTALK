import sys, os
import argparse
import urllib3, urllib
import re

# Modules
from libs.colors import *
from libs.selectChoice import select_choice

Parser = argparse.ArgumentParser(prog='whoUR.py', description='Tool for information gathering')

#this has been use in the future
Parser.add_argument('-d', '--dic-path', help='Dictonaries Path, Example: -d /root/', action='store', default='dicts/', dest='dicPath')
Parser.add_argument('-a', '--dic-adminspage', help='Admin Page dictonary, Example: -a adminspage.txt', action='store', default='adminspage.txt', dest='dicAdminsPage')

Args = Parser.parse_args()

# Dictonaries
dic_adminsPage = Args.dicPath +'/'+ Args.dicAdminsPage

def main():
    print('\n')
    print(B+'__        _______ ____ _____  _    _     _  __  ')
    print(B+'\ \      / / ____| __ )_   _|/ \  | |   | |/ /  ')
    print(R+' \ \ /\ / /|  _| |  _ \ | | / _ \ | |   |   /   ')
    print(B+'  \ V  V / | |___| |_) || |/ ___ \| |___| . \   ')
    print(R+'   \_/\_/  |_____|____/ |_/_/   \_\_____|_|\_\  ')
    print('\n') 
    print(lG+'------------------DRACKYJR---------------------')                                      
    
    
    
    
       

    select_choice()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(lG+'\n---------')
        print(lG+'- PBL -')
        print(lG+'---------\n')
        print(lR+'KBTCOE\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
