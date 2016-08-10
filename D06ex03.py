def print_name_e():
	fin = open('roster.txt','r')
	for name in fin:
		if 'e' in name.split()[0]:
			print(name)
#############################################################################
def main():
	print_name_e()

if __name__ == '__main__':
	main()