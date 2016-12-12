#!/usr/local/bin/python
#coding=utf-8

import re

def read_file(file_name):
    condition_line=[]
    question_line=[]
    condition_roman=[]
    info={'condition_roman':condition_roman,'condition_line':condition_line,'question_line':question_line}

    with open(file_name) as txt_file:
        for line in  txt_file:
            judge = re.search(r'\?$',line)
	    if judge:
	        question_line.append(line)
	    else: 
	        condition_line.append(line)

        for condition_case in condition_line[:]:
            if re.search(r'[IXVLCDM]$',condition_case) != None:
	        condition_line.remove(condition_case)
	        condition_roman.append(condition_case)

    return info


if __name__ == "__main__":
    print read_file("mission.txt")
