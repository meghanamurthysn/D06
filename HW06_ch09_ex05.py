#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, str_inp):
	for ltr in str_inp:
		if ltr not in word:
			return False
	return True

def count_uses(fin, str_inp):
	count = 0
	for word in fin:
		if uses_all(word, str_inp):
			count += 1
	return(count)

def read_file():
	fin = open('words.txt','r')
	print("Number of words that use all aeiou: {}".format(count_uses(fin, 'aeiou')))
	fin.seek(0,0)
	print("Number of words that use all aeiouy: {}".format(count_uses(fin, 'aeiouy')))

##############################################################################
def main():
    read_file()  # Call your function(s) here.

if __name__ == '__main__':
    main()
