import os
import shutil
from PIL import Image

images_dir = './images/'
annot_path = './qset3_internal_and_local.gt'

def convert(sz, bx):
    dw = 1./sz[0]
    dh = 1./sz[1]
    x = dw * (float(bx[0]) + float(bx[2]))/2.0
    y = dh * (float(bx[1]) + float(bx[3]))/2.0
    w = dw * (float(bx[2]) - float(bx[0]))
    h = dh * (float(bx[3]) - float(bx[1]))
    return (x,y,w,h)

with open(annot_path) as f:
	content = f.readlines()

d = {'Adidas' : 0, 'Adidas-text' : 27, 'Airness' : 28, 'Citroen' : 3, 'CocaCola' : 4, 'Base' : 29, 'BFGoodrich' : 30, 'Ferrari' : 7, 'Bik' : 31, 'Bouigues' : 32, 'Bridgestone' : 33, 'Bridgestone-text' : 34, 'Carglass' : 35, 'Citroen-text' : 36, 'Cofidis' : 37, 'Dexia' : 38, 'Nike' : 16, 'Kia' : 39, 'Mercedes' : 40, 'Puma' : 19, 'Peugeot' : 41, 'Puma-text' : 42, 'Quick' : 43, 'Reebok' : 44, 'Shell' : 45, 'SNCF' : 46, 'Standard_Liege' : 47, 'TNT' : 48, 'Total' : 49, 'Umbro' : 50, 'US_President' : 51, 'Veolia' : 52, 'VRT' : 53, 'ELeclerc' : 54, 'Gucci' : 55, 'Roche' : 56, 'StellaArtois' : 57}

if os.path.isdir('labels/') is False:
    os.mkdir('labels/')
if os.path.isdir('train_imgs/') is False:
    os.mkdir('train_imgs/')

print ("Wait a minute...")

for i in range(0, len(content)):
	w, h = Image.open('images/' + content[i].split()[2]).size
	coords = convert((w,h), [float(j) for j in (content[i].split()[5:])])
	ln = str(d[content[i].split()[1]]) + ' ' + str(coords[0]) + ' ' + str(coords[1]) + ' ' + str(coords[2]) + ' ' + str(coords[3]) + '\n'

	if not os.path.isfile('./labels/' + content[i].split()[2][:-4] + '.txt'):
		open('labels/' + content[i].split()[2][0:-4] + '.txt', 'w').write(ln)
	else:
		open('labels/' + content[i].split()[2][0:-4] + '.txt', 'a').write(ln)

print ("Done.")