#!python3

import glob
import re
import os


dir_name = os.path.dirname(__file__)
regex = re.compile('\w+')

def text_in_dir_stats(root_dir='texts'):
	pattern = os.path.join(root_dir, '**\*.txt')
	dictionary = {}
	for filename in glob.iglob(os.path.join(dir_name, pattern), recursive=True):
		words = regex.findall(open(filename, 'r').read())
		for word in words:
			dictionary[word] = dictionary.get(word, 0) + 1
	return sorted(dictionary.items(), key=lambda x: (x[1],x[0]), reverse=True)