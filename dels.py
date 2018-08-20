import os
import shutil

names = open('trainval.txt', 'r').read().split('\n')

for i in names:
	if os.path.isfile('train_imgs/' + i + '.jpg'):
		shutil.copy('train_imgs/' + i + '.jpg', 'imgs_2450/')
