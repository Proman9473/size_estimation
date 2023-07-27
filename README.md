# SEM Image Analyzer

This project provides a set of tools for analyzing Scanning Electron Microscope (SEM) images and their corresponding YOLO (You Only Look Once) object detection annotations.

## Files

- `SEM_Sensor.py`: Provides functions for reading YOLO annotations, plotting annotated images, and analyzing object properties.

- `main.py`: Driver program that uses the functions from `SEM_Sensor.py` to analyze all SEM images in a given directory and their corresponding YOLO annotations.

## SEM_Sensor.py

This script provides three main functions:

1. `read_yolo_annotations(file_path)`: Reads a YOLO annotation file from the provided path. Each line of the file is split into individual elements and returned as a list of lists.

2. `plot_annotations_with_widths(image_path, annotations, HFW)`: Takes an image path, a list of YOLO annotations, and the Horizontal Field Width (HFW). Reads the image from the given path, calculates a scale factor for converting pixel coordinates to real-world coordinates in nanometers, and plots the image with bounding boxes around the annotated objects. The real-world width, height, and X and Y positions of each object are also calculated and returned as lists. An annotated image is saved to the current directory.

3. `analyze_image(image_path, yolo_annotations_path, HFW)`: Calls `read_yolo_annotations` and `plot_annotations_with_widths` functions to analyze an image and its YOLO annotations. It also plots histograms for the width, height, and X and Y positions of the objects and saves them to the current directory. Finally, it writes some basic information about the objects (number of objects, minimum and maximum X and Y positions) to a text file and saves it to the current directory.

## main.py

This script does the following:

1. Imports the required libraries and modules, including the `SEM_Sensor` module.

2. Specifies the directory to start searching for .tif images.

3. Recursively traverses the directory, looking for .tif images. For each .tif image found, it checks if a corresponding .txt file (YOLO annotation file) exists.

4. For each image and its corresponding annotation file, it creates a subdirectory in the image's directory to store the results.

5. It calls the `analyze_image` function from `SEM_Sensor` module to analyze the image and its annotations, catch and print any errors that occur during the analysis.

6. It prints the widths, heights, and X and Y positions of the objects detected in the image, as well as the basic information about the objects.

## Requirements

To run the scripts, you need Python 3 and the following libraries:

- `opencv-python`
- `matplotlib`

These can be installed using pip:

```
pip install opencv-python
pip install matplotlib
```

Note: Depending on your Python environment, you may need to use `pip3` instead of `pip`, or use pip within a virtual environment.

## Usage

To use the scripts, follow these steps:

1. Ensure that you have Python 3 and the required libraries installed.

2. Put your SEM images (.tif files) and corresponding YOLO annotations (.txt files) in a directory.

3. Run the `main.py` script, specifying the directory containing your images as the `start_dir`.

4. The script will create a subdirectory for each image in the same directory as the image, containing the results of the analysis.

