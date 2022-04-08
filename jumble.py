import sys
import anytree as tree

def word_exists(test_word):
	file = open(r"dictionary.txt")
	for line in file:
		word = line.strip()
		if (word == test_word):
			return True
	return False


test_word = input('Enter the word: ')
test_word_list = list(test_word)

rootNodes = []
for i in range(len(test_word)):
	newNode = tree.Node(test_word[i], wordLength = 1)
	rootNodes.append(newNode)

for i in range(len(rootNodes)):
	currentRootNode = rootNodes[i]

	for j in range(len(rootNodes)):     ## j represents word lenth (depth of tree), we generate words
										## for each possible length as a depth layer of the tree
		nodes_of_same_length = tree.search.findall_by_attr(currentRootNode, j, 'wordLength')
		
		for node in nodes_of_same_length:
			letterBank = test_word_list.copy()
			for letterIndex in range(j): ##delete letters of current node from letter bank
				listOf_letters_in_node = list(node.name)
				letterBank.remove(listOf_letters_in_node[letterIndex])
			for letter in letterBank:   ## add remaining letters from letter bank to the node to create
										## each possible new word as new nodes
				newWord = node.name + letter
				newNode = tree.Node(newWord, parent = node, wordLength = j + 1)	


for candidate_word_length in range(len(test_word) + 1):
	for rootNode in rootNodes:
		nodes_of_same_length = tree.search.findall_by_attr(rootNode, candidate_word_length, 'wordLength')
		for node in nodes_of_same_length:
			if word_exists(node.name) and node.name != test_word:
				print(node.name)
			else:
				continue


word_exists(test_word)


