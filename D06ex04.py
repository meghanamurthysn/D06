def print_name_e():
	fin = open('roster.txt','r')
	fin1 = open('Names_with_e.txt', 'w')
	for name in fin:
		if 'e' in name.split()[0]:
			fin1.write(name)
#############################################################################
def main():
	print_name_e()

if __name__ == '__main__':
	main()