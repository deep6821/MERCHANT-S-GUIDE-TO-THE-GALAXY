#!/usr/local/bin/python
#coding=utf-8

import os
import read_file, roman_numerals, get_price, merchant_galaxy

def main():
    info = read_file.read_file("mission.txt")
    currency = roman_numerals.translate_to_roman_numerals(info)
    price = get_price.cal_unit_price(info, currency)
    merchant_galaxy.get_answers(info, currency, price)


if __name__ == "__main__":
    main()
