# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################################
def nested_sum(lst):
	sum_item=0
	for item in lst:
		if type(item) == list:
			sum_item += nested_sum(item)
		else: 
			sum_item += item
	return sum_item

##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()