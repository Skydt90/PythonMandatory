import glob
import os
import sys

# returns a finalized list of required reading sorted naturally
def traverseReposAndGetRequiredReading():
    directory_list = glob.glob("/Users/Christian/Desktop/Python Mandatory/Repositories/*/*.md")
    reading_set = set()
    finalized_list = list()
    string_flag = "## Required reading"
    string_flag2 = "##"
    
    for filename in directory_list:                                     # loops all files from glob list
        file = open(filename, "r")
        for line in file:                                               # loops every line in the file
            if line.startswith(string_flag):                            # flag1 triggers 'add loop'   
                for line in file:
                    if not line.startswith(string_flag2):               # add lines until flag2 is found
                        reading_set.add((line.replace("* [", "", 1)))   # add line w/o first two special chars
                    else:
                        break
    reading_set = [lines.capitalize() for lines in reading_set]         # capitalize first letter in set
    
    for line in sorted(reading_set):                                    # sorts the set and loops each line
        line = ("* [" + line)                                           # appends special chars again for md format
        finalized_list.append(line.rstrip())                            # strips string of trailing whitespace
    del(finalized_list[0])                                              # deletes blank line at first index
    return finalized_list