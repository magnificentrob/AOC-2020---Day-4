# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:14:26 2020

@author: Rob
"""

valid_passports = 0
file = open('input.txt', 'r')
stuff = ''
passports = []
for line in file:
	if line != '\n':
		stuff += line
	if line == '\n':
		if 'byr' in stuff and 'iyr' in stuff and 'eyr' in stuff and 'hgt' in stuff and 'hcl' in stuff and 'ecl' in stuff and 'pid' in stuff:
			valid_passports +=1
		stuff = ''
file.close()

print(valid_passports)