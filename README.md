# crop_by_Yolo_txt
Crop the image using YOLO's txt information

## Requirement

- Python3
- OpenCV

## Usage

`$ python3 crop_img.py --input_txt <target picture's text path(for darknet)>  `

#### Options

- --input_txt(default=None) : Specify the text file for darknet. Image information (width, height, target folder) is obtained by --input_txt.

- --output_folder(default="data") : Specify the output destination folder. Folders are numbered according to the bounding box number. (Example: data0, data1 ...)
- --format : Specify the extension of the image.