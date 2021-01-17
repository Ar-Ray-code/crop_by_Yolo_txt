import subprocess
import sys
import argparse
import warnings
import cv2
import os

warnings.simplefilter('ignore')

def img_save(txt, sample_img_path, output_path, save_count):

	## get abs path
	abs_path = os.path.dirname(os.path.abspath(sample_img_path))
	output_path = abs_path+"/"+output_path

	sample_img = cv2.imread(sample_img_path)
	img_width  = sample_img.shape[1]
	img_height = sample_img.shape[0]

	width    = int(float(txt[3])*img_width)
	height   = int(float(txt[4])*img_height)
	
	cut_x = int((img_width*float(txt[1])) - width /2)
	cut_y = int((img_height*float(txt[2])) - height/2)

	os.makedirs(output_path+str(save_count), exist_ok=True)

	exec_str="for i in "+abs_path+"/*.jpg;do convert -crop "+str(width)+"x"+str(height)+"+"+str(cut_x)+"+"+str(cut_y)+" ${i} "+output_path+str(save_count)+"/$(basename ${i%.jpg})_"+str(save_count)+".jpg;done"
	os.system(exec_str)


## arg------------------------------------------
parser = argparse.ArgumentParser(description="image generator")
parser.add_argument('--input_txt',default=None)
parser.add_argument('--output_folder',default='data')
parser.add_argument('--format',default='jpg')

args = parser.parse_args()

## jpg name
sample_img_txt = os.path.splitext(args.input_txt)[0]+"."+args.format

read_txt_file = open(args.input_txt,'r')

lines = read_txt_file.readlines()

count = 0
for line in lines:
	txt_str = line.split()
	img_save(txt_str, sample_img_txt, args.output_folder, count)
	count = count + 1
	txt_str.clear()

read_txt_file.close()

