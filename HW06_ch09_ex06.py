#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words: 0
##############################################################################
# Imports

# Body
def is_abecedarian(word):
	count = 0
	for ltr in word:
		count += 1
		if(count == 1):
			index_alph = ord(ltr)
		elif(index_alph > ord(ltr)):
			return False
		else:
			index_alph = ord(ltr)
	return True

def num_abecedarian():
	fin = open('words.txt','r')
	num_abecedarian_words = 0
	for word in fin:
		if is_abecedarian(word):
			num_abecedarian_words += 1
	print("The number of abecedarian words in the file are: {}".format(num_abecedarian_words))

##############################################################################
def main():
    num_abecedarian()

if __name__ == '__main__':
    main()
