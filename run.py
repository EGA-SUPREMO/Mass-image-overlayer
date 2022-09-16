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

def merge_images(template_folder, car_folder, filename_templates, filename_cars):
	global i
	for filename_template in filename_templates:
		for filename_car in filename_cars:
			i += 1
			file_template = template_folder+"/"+filename_template
			file_car = car_folder+"/"+filename_car
			os.system(f"magick -background none '{file_car}' '{file_template}' -layers flatten 'out/{i}_out.png'")

for car_folder in car_folders:
	filename_templates = next(os.walk(dir_templates+car_folder), (None, None, []))[2]
	filename_cars = next(os.walk(dir_cars + car_folder), (None, None, []))[2]

	merge_images(dir_templates+car_folder, dir_cars+car_folder, filename_templates, filename_cars)
	merge_images(dir_other, dir_cars+car_folder, filename_others, filename_cars)
