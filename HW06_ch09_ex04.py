#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: He'll coach fall face off.
#       2: Hello chef!
#       3: Cool cocoa coffee!
##############################################################################
# Imports

# Body
def uses_only(word,str):
	for ltr in word:
		if(ltr not in str):
			return False
	return True

def sentence_frame():
	ltr_str = 'acefhlo'
	fin = open('words.txt','r')
	word_lst = fin.read().splitlines()
	for word in word_lst:
		if(uses_only(word,ltr_str)):
			print(word)


##############################################################################
def main():
    sentence_frame()  # Call your function(s) here.

if __name__ == '__main__':
    main()
