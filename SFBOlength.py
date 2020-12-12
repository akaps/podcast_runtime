import dbus
import os
import subprocess
import re
from subprocess import Popen, PIPE
import time

def main():
    # Uncomment to print page content
    #print(sfbo)

    times = []
    i = 0

    #times = sfbo.split()

    file1 = open("sfbo.txt", "r")
    Lines = file1.readlines()

    for line in Lines:
        if ":" in line and ": " not in line:
            times.extend(line)
            if(line.count(":") == 1):
                print("00:", end="")
            line = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', line, flags=re.M)
            print(line)

main()

