#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
	"""Returns True if there is no 'e' in the word else returns None"""
	if not 'e' in word:
		return True
	return

def compute_percent(x,y):
	"""Return the percentage when two numbers are provided as input"""
	return x/y * 100

def print_no_e(word):
	"""Print the word after stripping the extra spaces"""
	print(word.strip())

def read_file():
	"""Read each word from 'words.txt' and determine if the word has an e or not. Print the words which dont have 'e'
	Also compute the percentage of words having no 'e' with the total words in the file and print the same"""
	fin = open('words.txt','r')
	count_word = 0 # To store the count of total words in words.txt
	count_no_e_word = 0 # To store the count of words with no 'e'
	for word in fin:
		count_word += 1
		if has_no_e(word):
			count_no_e_word += 1
			print_no_e(word)
	if count_word > 0 and count_no_e_word > 0:
			print("The percentage of the words in the list that have no 'e' is {}".format(compute_percent(count_no_e_word,count_word)))

##############################################################################
def main():
    read_file()

if __name__ == '__main__':
    main()
