import os
import sys
import subprocess

dir_images="/home/trabajo/Pictures/Venta de carros/"
dir_templates="/home/trabajo/Pictures/Venta de carros/Templates/"
dir_cars="/home/trabajo/Pictures/Venta de carros/Carros/"

car_templates = os.listdir(dir_templates)
car_folders = os.listdir(dir_cars)

filename_templates = next(os.walk(dir_corolla_se_templates), (None, None, []))[2]
filename_cars = next(os.walk(dir_corolla_se_cars), (None, None, []))[2]

i=0

for filename_template in filename_templates:
	for filename_car in filename_cars:
		i += 1
		file_template = dir_corolla_se_templates+filename_template
		file_car = dir_corolla_se_cars+filename_car
		#os.system(f"magick -background none '{file_car}' '{file_template}' -layers flatten '{i}_out.png'")
