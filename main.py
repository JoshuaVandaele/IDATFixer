import pyPngEdited as png  # https://github.com/drj11/pypng
import os

try:
    os.mkdir("input")
    os.mkdir("output")
except:
	pass
else:
	print("Created input and output directories.")


for filename in os.listdir("input"):
	image = png.Reader("input/"+filename) 
	data = image.read()

	print("\n-== "+filename+" ==-")

	w = png.Writer(**data[3])
	with open("output/"+filename,"wb") as f:
		w.write(f, image.read()[2])