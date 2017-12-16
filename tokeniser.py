# -*- coding: utf-8 -*-

#Class 3
import sys
for line in sys.stdin.readlines ():
	token_id = 1
	tokens=line.split( )
	print(tokens)

	# sent_id = 3 
	# text = y 40 C. w. 	
	print ("# text = "+line)
	for i in range(len(tokens)):
		l1=['_']*8
		print('%d\t%s' % (token_id, tokens[i]) +'\t'.join(l1))
		token_id += 1
#nano tokeniser.py
#head corpus/wiki.txt


