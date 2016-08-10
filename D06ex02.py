import random
def random_file():
	fin = open('Random_Number_File.txt','w')
	for n in range(10):
		rand_num = random.random()
		fin.write(str(rand_num)+"\n")
	fin.close()
#############################################################################
def main():
	random_file()

if __name__ == '__main__':
	main()