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

d = {'Adidas' : 0, 'Adidas-text' : 1, 'Airness' : 2, 'Citroen' : 3, 'CocaCola' : 4, 'Base' : 5, 'BFGoodrich' : 6, 'Ferrari' : 7, 'Bik' : 8, 'Bouigues' : 9, 'Bridgestone' : 10, 'Bridgestone-text' : 11, 'Carglass' : 12, 'Citroen-text' : 13, 'Cofidis' : 14, 'Dexia' : 15, 'Nike' : 16, 'Kia' : 17, 'Mercedes' : 18, 'Puma' : 19, 'Peugeot' : 20, 'Puma-text' : 21, 'Quick' : 22, 'Reebok' : 23, 'Shell' : 24, 'SNCF' : 25, 'Standard_Liege' : 26, 'TNT' : 27, 'Total' : 28, 'Umbro' : 29, 'US_President' : 30, 'Veolia' : 31, 'VRT' : 32, 'ELeclerc' : 33, 'Gucci' : 34, 'Roche' : 35, 'StellaArtois' : 36}

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

	if not os.path.isfile('./train_imgs/' + content[i].split()[2]):
		shutil.copy('images/' + content[i].split()[2], 'train_imgs/')

print ("Done.")
