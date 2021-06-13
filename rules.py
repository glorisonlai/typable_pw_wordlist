import sys

# Rule to append number of specified length to password
def add_numbers(length: int, in_file: str, out_file: str):
	with open(out_file, 'w') as write_file:
		with open(in_file, 'r') as read_file:
			for line in read_file.readlines:
				line = line.strip('\n')
				for i in range(10**length):
					number = ('0' * length + str(i))[:length]
					write_file.write(number)


if __name__ == '__main__':
	in_file = sys.argv[1]
	out_file = sys.argv[2]
	length = int(sys.argv[3])

	add_numbers(length, in_file, out_file)
