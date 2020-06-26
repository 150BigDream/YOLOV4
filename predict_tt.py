#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo_tt import YOLO
from PIL import Image
import csv
import os

yolo = YOLO()

#['Czech', 'India', 'Japan']
file_dir = "D://data//data//test//India//images//"
for files in os.listdir(file_dir):
    filepath = file_dir + files
    image = Image.open(filepath)
    rows = [files, yolo.detect_image(image)]
    with open('output.csv', "a+", newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(rows)


