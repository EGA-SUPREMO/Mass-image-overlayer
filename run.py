import os
import sys
import subprocess
import random

dir_images="/home/trabajo/Pictures/Venta de carros/"
dir_templates=dir_images+"Plantillas Nombres/"
dir_cars=dir_images+"Carros/"
dir_other=dir_images+"Otros"

directions=["SouthEast", "SouthWest", "NorthEast", "NorthWest"]

filename_others = next(os.walk(dir_other), (None, None, []))[2]

template_folders = os.listdir(dir_templates)
car_folders = os.listdir(dir_cars)

i=0

def remove_extension(text):
	sep = '.'
	return text.split(sep, 1)[0]

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

def getSmallerSizesOfCarsForTemplates(file):
	w = getWidth(file) * 0.5
	h = getHeight(file) * 0.2
	return w, h

def get_biggest_size_for_template(template_file, car_file):

	max_width = getWidth(car_file)
	max_height = getHeight(car_file)

	w, h = getSmallerSizesOfCarsForTemplates(car_file)

	ratio = getRatio(template_file)
	h_template = getHeightByWidth(w, ratio)
	w_template = getWidthByHeight(h, ratio)

	if w_template > max_width:
		w_template = max_width
		h = getHeightByWidth(w_template, ratio)

	if h_template > max_height:
		h_template = max_height
		w = getWidthByHeight(h_template, ratio)

	if h_template>h:
		return w, h_template
	
	return w_template, h


def merge_images(template_folder, car_folder, filename_templates, filename_cars, dir_out, rotation):
	global i

	car_model = os.path.basename(car_folder)

	for filename_car in filename_cars:
		random_filename_others = random.sample(filename_templates, min(len(filename_templates), 2))
		for filename_template in random_filename_others:
			i += 1
			file_template = template_folder+"/"+filename_template
			file_car = car_folder+"/"+filename_car

			w, h = get_biggest_size_for_template(file_template, file_car)
			w = round(w)
			h = round(h)

			print(i)
			random_dir = random.sample(directions, 1)
			output_name = remove_extension(filename_car)
			os.system(f"magick -background none -gravity {random_dir[0]} '{file_car}' {rotation} \\( '{file_template}' -geometry {w}x{h}! \\) -composite 'out{dir_out}{car_model}/{i}_{output_name}.png'")

for car_folder in car_folders:
	filename_templates = next(os.walk(dir_templates+car_folder), (None, None, []))[2]
	filename_cars = next(os.walk(dir_cars + car_folder), (None, None, []))[2]

	merge_images(dir_templates+car_folder, dir_cars+car_folder, filename_templates, filename_cars, "/Javier/", "")
	merge_images(dir_templates+car_folder, dir_cars+car_folder, filename_templates, filename_cars, "/", "-flop")
