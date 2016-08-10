#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, str_forbid):
    """ return True if word NOT forbidden"""
    lst = list()
    lst.extend(str_forbid)
    for item in lst:
        if item in word:
            return False
    else:
        return True


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    input_str = input("Enter a string of forbidden letters: ")
    fin = open('words.txt','r')
    for word in fin:
        if avoids(word.strip(), input_str):
            print(word.strip())


def forbidden_param(str_param):
    """ return count of words NOT forbidden by param"""
    fin = open('words.txt','r')
    count_no_param = 0
    for word in fin:
        if avoids(word.strip(), str_param):
            count_no_param += 1
    return(count_no_param)


def find_five():
    fin = open('words.txt','r')
    count_lst = list()
    ltr_lst = list()
    allwords = fin.read()
    for ltr in (range(ord('a'),ord('z')+1)):
        ltr_cnt = allwords.count(chr(ltr))
        count_lst.append(ltr_cnt)
        ltr_lst.append(chr(ltr))
    min_ltr_str = ''
    print(count_lst)
    print(ltr_lst)
    for i in range(5):
        min_cnt = min(count_lst)
        print(min_cnt)
        min_idx = count_lst.index(min_cnt)
        min_ltr_str += ltr_lst[min_idx]
        count_lst.pop(min_idx)    
        ltr_lst.pop(min_idx)
    print(min_ltr_str, forbidden_param(min_ltr_str))

##############################################################################
def main():
    find_five()
    # Your final submission should only call five_five

if __name__ == '__main__':
    main()
