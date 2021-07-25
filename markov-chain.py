import sys
from random import randrange
import argparse

class ProbTree:
	class Node:
		def __init__(self) -> None:
			self.next: dict[str, 'Node'] = {}

		def append(self, letter: str) -> 'Node':
			return self.next.setdefault(letter, self.__class__())

		def choose_next_letter(self) -> tuple(str, 'Node'):
			rand_letter = self.next.keys()[randrange(len(self.next.keys()))]
			return rand_letter, self.next[rand_letter]


	EOW = '$'
	RAND_GEN_LIMIT = 1000

	def __init__(self) -> None:
		self.root = self.Node()
	
	def extend(self, word: str) -> None:
		node = self.root
		for letter in range(len(word)):
			node = node.append(letter)
		node.append(self.EOW)

	def generate(self, length_limit: int) -> str:
		node_stack, letter_stack, prev_node, iterations= [], [], None, 0
		letter, node = self.root.choose_next_letter()
		node_stack.append(node)
		while letter != self.EOW:
			iterations += 1
			letter_stack.append(letter)
			if iterations > self.RAND_GEN_LIMIT:
				print('Gen limit reached!')
				return 
			if len(letter_stack) >= length_limit:
				prev_node = node_stack.pop()
				letter_stack.pop()
				node = node_stack[-1]
			letter, node = node.choose_next_letter()
			while node == prev_node:
				prev_node = node_stack.pop()
				letter_stack.pop()
				node = node_stack[-1]
				letter, node = node.choose_next_letter()
			prev_node = None
			node_stack.append(node)
		return ''.join(letter_stack)
		
	def get_words(self, length_limit: int, rounds: int) -> set[str]:
		rand_words = set()
		for _ in range(rounds):
			word = self.generate(length_limit)
			if word: 
				rand_words.add(word)
		return rand_words



def markov(wordlist: list[str], word_length_lim: int, rounds: int) -> set[str]:
	markov_chain = ProbTree(word_length_lim)
	for word in wordlist:
		markov_chain.extend(word)
	return markov_chain.get_words(length_limit=word_length_lim, rounds=rounds)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(add_help=True, description = "Markov Chain word generator", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""
Example:
./markov-chain.py rockyou.txt -l 10 -i 10000
	""")
	parser.add_argument('wordlist', action='store', help='Path to wordlist file')
	parser.add_argument('-l', action='store', help='Word length limit')
	parser.add_argument('-i', action='store', help='Iterations')

	if len(sys.argv) < 3:
		parser.print_help()
		sys.exit(1)

	options = parser.parse_args()

	with open(options.wordlist, 'r') as in_file:
		wordlist = in_file.readlines
	
	pw_list = markov(wordlist=wordlist, word_length_lim=int(options.l), rounds=int(options.i))

	with open('./pw_list.txt', 'w') as out_file:
		out_file.write('\n'.join(pw_list))

	sys.exit(1)