# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 03:28:52 2020

@author: Rob
"""

valid_passports = []
file = open('input.txt', 'r')
stuff = ''
passports = []
for line in file:
	if line != '\n':
		stuff += line
	if line == '\n':
		if 'byr' in stuff and 'iyr' in stuff and 'eyr' in stuff and 'hgt' in stuff and 'hcl' in stuff and 'ecl' in stuff and 'pid' in stuff:
			stuff = stuff.replace('\n', ' ')
			valid_passports.append(stuff)
		stuff = ''

file.close()
#158
def checkBirthYear(string):
	byr = ''
	start = string.find('byr:')+4
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			byr += i
	byr = int(byr)
	return 1920 <= byr <= 2002
#171
def checkIssueYear(string):
	iyr = ''
	start = string.find('iyr:')+4
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			iyr += i
	iyr = int(iyr)
	return 2010 <= iyr <= 2020
#155
def checkExpYear(string):
	eyr = ''
	start = string.find('eyr:')+4
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			eyr += i
	eyr = int(eyr)
	return 2020 <= eyr <= 2030
#162
def checkHeight(string):
	height=''
	start = string.find('hgt:')+4
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			height +=i
	if height[-2:] == 'in':
		height = height.replace('in', '')
		height = int(height)
		return 59 <= height <= 76
	if height[-2:] == 'cm':
		height = height.replace('cm', '')
		height = int(height)
		return 150 <= height <= 193
	return False
#158
def checkHairColor(string):
	haircolor=''
	start = string.find('hcl:')+4
	if string[start] != '#':
		return False
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			haircolor += i
	return True
#152
def checkEyeColor(string):
	ecl = ''
	start = string.find('ecl:')+4
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			ecl += i
	if (ecl == 'amb' or ecl == 'blu' 
	or ecl =='brn' or ecl =='gry' or ecl == 'grn' 
	or ecl =='hzl' or ecl == 'oth'):
		return True
	else:
		return False
#165
def checkPID(string):
	pid = ''
	start = string.find('pid:')+4
	for i in string[start:]:
		if i == ' ' or i == '':
			break
		else:
			pid += i
	if len(pid) == 9:
		return True
	else:
		return False

valid = 0
for i in valid_passports:
	if (checkBirthYear(i) == True
	and checkIssueYear(i) == True
	and checkExpYear(i) == True
	and checkHeight(i) == True
	and checkHairColor(i) == True
	and checkEyeColor(i) == True
	and checkPID(i) == True):
		valid +=1

print(valid)