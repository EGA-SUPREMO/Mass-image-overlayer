import os
import sys
import subprocess

dir_images="/home/trabajo/Pictures/Venta de carros/"
dir_templates=dir_images+"Plantillas Nombres/"
dir_cars=dir_images+"Carros/"
dir_other=dir_images+"Otros"

filename_others = next(os.walk(dir_other), (None, None, []))[2]

template_folders = os.listdir(dir_templates)
car_folders = os.listdir(dir_cars)

i=0

def getWidth(file):
	return float(subprocess.run(['magick', file, '-auto-orient', '-format', '%w', 'info:'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

def getHeight(file):
	return float(subprocess.run(['magick', file, '-auto-orient', '-format', '%h', 'info:'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

def getRatio(file):
	return float(subprocess.run(['magick', file, '-auto-orient', '-format', '%[fx:w/h]', 'info:'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

def getWidthByHeight(height, ratio):
	return height*ratio

def getHeightByWidth(width, ratio):
	return width/ratio

def getRatio(file):
	return subprocess.run(['magick', file, '-auto-orient', '-format', '%[fx:w/h]', 'info:'], stdout=subprocess.PIPE).stdout.decode('utf-8')

def getSmallerSizesOfCarsForTemplates(file):
	w = getWidth(file) * 0.1
	h = getHeight(file) * 0.2
	return w, h

def get_biggest_size_for_name(w, h, template_file)
	getSmallerSizesOfCarsForTemplates('inn.jpeg')

print(getWidth('int.png'))
print(getHeight('int.png'))

print(getWidth('inn1.jpeg'))
print(getHeight('inn1.jpeg'))

def merge_images(template_folder, car_folder, filename_templates, filename_cars):
	global i
	for filename_template in filename_templates:
		for filename_car in filename_cars:
			i += 1
			file_template = template_folder+"/"+filename_template
			file_car = car_folder+"/"+filename_car
			#os.system(f"magick -background none '{file_car}' '{file_template}' -layers flatten 'out/{i}_out.png'")

for car_folder in car_folders:
	filename_templates = next(os.walk(dir_templates+car_folder), (None, None, []))[2]
	filename_cars = next(os.walk(dir_cars + car_folder), (None, None, []))[2]

	merge_images(dir_templates+car_folder, dir_cars+car_folder, filename_templates, filename_cars)
	merge_images(dir_other, dir_cars+car_folder, filename_others, filename_cars)
