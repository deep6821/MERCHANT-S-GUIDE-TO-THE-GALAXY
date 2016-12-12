#!/usr/local/bin/python
#coding=utf-8

import re
import read_file, roman_numerals, get_price, earth_numerals 

def get_answers(info, currency, price):
    for key,value in info.items():
        if(key=='question_line'):
	    for i in value:
	        roman_sum=''
		words_total=''
		material=''
		if re.search(r'^how much is',i) != None:
		    for words in i.split(' '):
		        if currency.has_key(words):
		            valuerance=currency[words]
			    words_total = words_total.join(['',words])
			    words_total = words_total.join(['',' '])
			    roman_sum=roman_sum.join(['',valuerance])
		    earth_sum = earth_numerals.translate_to_earth_numerals(roman_sum)
		    print words_total,'is',earth_sum
		elif re.search(r'^how many Credits is',i) != None:
		    for words in i.split(' '):
		        if currency.has_key(words):
			    valuerance = currency[words]
			    words_total = words_total.join(['',words])
			    words_total = words_total.join(['',' '])
			    roman_sum = roman_sum.join(['',valuerance])

			earth_sum = earth_numerals.translate_to_earth_numerals(roman_sum)
			if price.has_key(words):
			    material_price = price[words]
			    material = words
			    total_price = earth_sum * material_price
		    print words_total,material,'is',int(total_price),'Credits'
		else:
		    print 'I have no idea what you are talking about'


if __name__ == "__main__":
    info = read_file.read_file("mission.txt")
    currency = roman_numerals.translate_to_roman_numerals(info) 
    price = get_price.cal_unit_price(info,currency)
    #print "Info =",info
    #print "Currency =",currency
    #print "Price =",price
    get_answers(info, currency, price)
