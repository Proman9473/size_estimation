import os
import sys

# add the path where your SEM_Sensor.py resides
sys.path.append(r"SEM_Sensor path")

from SEM_Sensor import analyze_image, read_yolo_annotations, plot_annotations_with_widths

# Start directory
start_dir = r"images main dir"

# Traverse directory recursively
for root, dirs, files in os.walk(start_dir):
    for file in files:
        # Check if the file is a .tif image
        if file.endswith(".tif"):
            image_path = os.path.join(root, file)

            # Check if the corresponding .txt file exists
            annotation_file = file.split('.')[0] + '.txt'
            if annotation_file in files:
                annotation_path = os.path.join(root, annotation_file)

                # Create a subdirectory for the image results
                result_dir = os.path.join(root, file.split('.')[0])
                os.makedirs(result_dir, exist_ok=True)

                # Change the current directory to the result directory
                os.chdir(result_dir)

                # Analyze the image
                try:
                    annotations = read_yolo_annotations(annotation_path)
                    width, height, X_positions, Y_positions = plot_annotations_with_widths(image_path, annotations, HFW=8.29)
                    width, height, X_positions, Y_positions, object_info = analyze_image(image_path, annotation_path, HFW=8.29)
                    print("Widths in nm: ", width)
                    print("Heights in nm: ", height)
                    print("X positions in nm: ", X_positions)
                    print("Y positions in nm: ", Y_positions)
                    print(object_info)
                except Exception as e:
                    print(f"Failed to analyze image {image_path}. Error: {e}")
