#!/usr/local/bin/python
#coding=utf-8

import re
import read_file, roman_numerals, earth_numerals

def cal_unit_price(info,currency):
    price={}
    for key,value in info.items():
        if(key=='condition_line'):
            for condition in value:
	        roman_sum=''
		earth_sum=''
		value_number=0
		for temp in ['Silver','Gold','Iron']:
		    if re.search(temp,condition) != None:
		        sentense = condition.split(temp)
			for i in sentense[0].split(' '):
			    if i:
			        roman = currency[i]
				roman_sum = roman_sum.join(['',roman])
				earth_sum = earth_numerals.translate_to_earth_numerals(roman_sum)

			for i in sentense[1].split(' '):
			    if i.isdigit():
			        value_number = float(i)
			price[temp] = value_number / earth_sum
    return price

if __name__ == "__main__":
    info = read_file.read_file("mission.txt")
    currency = roman_numerals.translate_to_roman_numerals(info)
    print cal_unit_price(info, currency)
