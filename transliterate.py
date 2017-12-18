import sys

table = {
	'ا':'a',
	'ب':'b',
	'ت':'t',
	'ث':'th',
	'ج':'j',
	'ح':'h',
	'خ':'kh',
	'د':'d',
	'ذ':'dh',
	'ر':'r',
	'ز':'z',
	'س':'s',
	'ش':'m',
	'ص':'ss',
	'ض':'dhh',
	'ط':'thh',
	'ظ':'dz',
	'ع':"'a",
	'غ':'gh',
	'ف':'f',
	'ق':'g',
	'ك':'k',
	'ل':'l',
	'م':'m',
	'ن':'n',
	'ه':'hh',
	'و':'w',
	'ي':'ye'

}

for line in sys.stdin.readlines():
	line = line.strip()
	if line == '':
		print()
		continue	
	if line [0]=='#':
		print(line)
		continue
	
	row = line.split('\t')
	form = row[1]
	translit=form
	for c in translit:
		if c in table:
			translit=translit.replace(c,table[c])	
	row[9]='Translit='+translit
	print('\t'.join(row))

