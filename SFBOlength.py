import sys
import subprocess
import re
from subprocess import Popen, PIPE
import time

def load_data(uri, file_name):
    podcast_details = subprocess.check_output('w3m -dump https://open.spotify.com/show/5z3G1urniqVGKCNZSQXhX0', shell=True)
    file = open(file_name, 'rw')
    file.writelines(podcast_details)
    file.close()

def main():
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

"""
    # Convert BPM into int
    # sfbo = int(sfbo)

    h = 0
    m = 0
    s = 0
    for i in range(len(times)):

        if(times[i].count(":") == 2):
            h += int(times[i].split(":")[0])
            m += int(times[i].split[":"][1].lstrip().split(":")[2])
            s += int(times[i].split[":"][2].lstrip())
        else:
            m += int(times[i].split(":")[0])
            s += int(times[i].split[":"][2].lstrip())

        print(times[i])

    print(h, m, s)

    # Return BPM
    #return BPM
    """

if __name__ == "__main__":
    main()
