import os
from os import listdir
from os.path import isfile, join

path_to_anns = 'path/to'
file_names = [f for f in listdir(path_to_anns) if isfile(join(path_to_anns, f))]

for i in file_names:
	f = open(i, 'r')
	content = f.read()
	#print content
	f.close()
	hm = content.replace('  ', '\t')
	f2 = open(i, 'w')
	f2.write(hm)
	f2.close()