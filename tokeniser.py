# -*- coding: utf-8 -*-

#Class 3
import sys
sent_id =1
for line in sys.stdin.readlines ():
	token_id = 1
	line = line.strip()
	if line == "":
		continue
	tokens=line.split( )
	#print(tokens)

	# sent_id = 3 
	# text = y 40 C. w. 	
	print ("# text = "+line)
	print ("# sent_id = %d" % sent_id)
	for i in range(len(tokens)):
		l1=['_']*8
		print('%d\t%s' % (token_id, tokens[i]) +'\t'.join(l1))
		token_id += 1
	sent_id+=1
	print()
#nano tokeniser.py
#head corpus/wiki.txt


