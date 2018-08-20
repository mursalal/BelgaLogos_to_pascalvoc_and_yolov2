import os
import xml.etree.cElementTree as ET
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from lxml import etree
from PIL import Image

annot_path = './qset3_internal_and_local.gt'

dones = set()

def prettify(elem):
	rough_string = ElementTree.tostring(elem, 'utf8')
	root = etree.fromstring(rough_string)
	return etree.tostring(root, pretty_print=True)

def add_obj(ii):
	obje = Element("object")
	SubElement(obje, 'name').text = ii.split()[1].lower()
	SubElement(obje, 'pose').text = 'Unspecified'
	SubElement(obje, 'truncated').text = '0'
	SubElement(obje, 'difficult').text = '0'

	bndbox = SubElement(obje, "bndbox")
	SubElement(bndbox, 'xmin').text = ii.split()[5]
	SubElement(bndbox, 'ymin').text = ii.split()[6]
	SubElement(bndbox, 'xmax').text = ii.split()[7]
	SubElement(bndbox, 'ymax').text = ii.split()[8]
	return obje

with open(annot_path) as f:
	content = f.readlines()

if os.path.isdir('Annotations/') is False:
    os.mkdir('Annotations/')

for i in range(0, len(content)):
	if content[i].split()[2] not in dones:
		f = open('Annotations/' + content[i].split()[2][:-4] + '.xml', 'w')
		annotation = Element('annotation')
		annotation.set('verified', 'no')
		SubElement(annotation, "folder").text = 'Annotations'
		SubElement(annotation, "filename").text = content[i].split()[2]
		source = SubElement(annotation, "source")
		SubElement(source, "database").text = 'Unknown'
		size_part = SubElement(annotation, 'size')
		width = SubElement(size_part, 'width')
		height = SubElement(size_part, 'height')
		w, h = Image.open('images/' + content[i].split()[2]).size
		width.text = str(w)
		height.text = str(h)
		SubElement(size_part, 'depth').text = '3'
		SubElement(annotation, 'segmented').text = '0'

		annotation.append(add_obj(content[i]))

		for j in range(0, len(content)):
			if i != j and content[i].split()[2] == content[j].split()[2]:
				print i, j
				vr = add_obj(content[j])
				annotation.append(vr)

		prettifyResult = prettify(annotation)
		f.write(prettifyResult.decode('utf8'))
		f.close()
		dones.add(content[i].split()[3])


annots = open('hhhhh.txt', 'r').readlines()
for i in annots:
	f = open('Annotations/' + i[:-1], 'r')
	content = f.read()
	f.close()
	hm = content.replace('  ', '\t')
	f2 = open('Annotations/' + i[:-1], 'w')
	f2.write(hm)
	f2.close()
