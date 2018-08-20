import os
from pprint import pprint
import xml.etree.ElementTree as ET

contstr = open('trainval.txt', 'r').read()
content = contstr.split('\n')
ans = str()
for i in range(len(content)-1):
	tree = ET.parse('Annotations/' + content[i] + '.xml')
	root = tree.getroot()
	mins = root.findall('.//xmin')
	maxs = root.findall('.//xmax')
	for j in range(len(mins)):
		if int(mins[j].text) > int(maxs[j].text):
			print mins[j].text, maxs[j].text
			contstr = contstr.replace(content[i]+'\n', '')
			break
open('hhhhhhhhhhh.txt', 'w').write(contstr)