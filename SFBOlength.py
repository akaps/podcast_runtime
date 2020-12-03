import sys
import subprocess
import re
from subprocess import Popen, PIPE
import time

MINUTES_REGEX = r'^ *(\d){1,2}:(\d){2}$'
HOURS_REGEX = r'^ *(\d){1,2}:(\d){2}:(\d){2}$'

def load_data(uri, file_name):
    podcast_details = subprocess.check_output('w3m -dump https://open.spotify.com/show/5z3G1urniqVGKCNZSQXhX0', shell=True)
    file = open(file_name, 'rw')
    file.writelines(podcast_details)
    file.close()

def pretty_print_time(total_time):
    hrs = total_time // 360
    total_time %= 360
    min = total_time // 60
    sec = total_time % 60
    print("total runtime: {:d}:{:02d}:{:02d}".format(hrs, min, sec))

def calculate_time(lines):
    total_time = 0 #calculate in seconds
    for line in lines:
        if re.match(MINUTES_REGEX, line):
            min, sec = re.match(MINUTES_REGEX, line).groups()
            total_time += int(min) * 60 + int(sec)
        if re.match(HOURS_REGEX, line):
            hr, min, sec = re.match(HOURS_REGEX, line).groups()
            total_time += int(hr) * 360 + int(min) * 60 + int(sec)
    return total_time

def main():
    file = open("sfbo.txt", "r")
    lines = file.readlines()
    file.close()

    pretty_print_time(calculate_time(lines))

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
