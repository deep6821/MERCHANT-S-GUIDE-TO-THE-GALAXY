#!/usr/local/bin/python
#coding=utf-8

import read_file

def translate_to_roman_numerals(info):
    translate_to_roman=[[],[],[],[],[],[],[]]
    currency={}
    
    for key,value in info.items():
        if(key=='condition_roman'):
	    for index,number in enumerate(value):
	        translate_to_roman[index]=number.split()
    
    for i in translate_to_roman:
        if i:
	    currency[i[0]]=i[2]
    return currency


if __name__ == "__main__":
    input_file = "mission.txt"
    info = read_file.read_file(input_file)
    print translate_to_roman_numerals(info)
