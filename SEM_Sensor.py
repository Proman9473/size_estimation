import cv2
import matplotlib.pyplot as plt
import tkinter as tk

def read_yolo_annotations(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    annotations = [line.strip().split() for line in lines]
    return annotations

def plot_annotations_with_widths(image_path, annotations, HFW):
    img = cv2.imread(image_path)
    image_width, image_height = img.shape[1], img.shape[0]

    scale_factor_x = (HFW * 1000) / image_width  # Scale factor in X direction (nanometer/pixel)
    scale_factor_y = (HFW * 1000) / image_height  # Scale factor in Y direction (nanometer/pixel)

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), extent=[0, image_width, image_height, 0])

    width = []  # list to store the widths
    height = []  # list to store the heights

    X_positions = []
    Y_positions = []

    for k, annotation in enumerate(annotations):
        class_id, center_x, center_y, box_width, box_height = map(float, annotation)
        center_x_pixels = center_x * image_width
        center_y_pixels = center_y * image_height
        bbox_width_pixels = box_width * image_width
        bbox_height_pixels = box_height * image_height

        X_positions.append(center_x_pixels * scale_factor_x)
        Y_positions.append(center_y_pixels * scale_factor_y)

        bbox_width_real = bbox_width_pixels * scale_factor_x
        bbox_height_real = bbox_height_pixels * scale_factor_y

        width.append(bbox_width_real)  # Add the width to the list
        height.append(bbox_height_real)  # Add the height to the list

        print(f'Object {k+1}: width = {bbox_width_real:.2f} nm, height = {bbox_height_real:.2f} nm')

        # Calculate the coordinates for the bounding box in the upper-left corner format (xmin, ymin)
        xmin = int(center_x_pixels - bbox_width_pixels / 2)
        ymin = int(center_y_pixels - bbox_height_pixels / 2)

        # Draw bounding box and annotate with real-world width and height
        rect = plt.Rectangle((xmin, ymin), bbox_width_pixels, bbox_height_pixels, edgecolor='r', linewidth=1.5, fill=False)
        ax.add_patch(rect)
        ax.text(xmin, ymin-10, f'{bbox_width_real:.2f} nm', color='yellow', fontsize=12)

    plt.title('Image with bounding boxes and sizes')
    plt.axis('off')  # Turn off axis for a cleaner visualization
    plt.show()



    return width, height, X_positions, Y_positions

if __name__ == "__main__":
    image_path = "BS1319_001.tif"  # Replace with the actual image path
    yolo_annotations_path = "BS1319_001.txt"  # Replace with the actual YOLO annotations file path
    HFW = 8.29  # micrometer

    annotations = read_yolo_annotations(yolo_annotations_path)
    width, height, X_positions, Y_positions = plot_annotations_with_widths(image_path, annotations, HFW)

    # Plot histogram of widths
    plt.figure(figsize=(10, 5))
    plt.hist(width, bins=50, color='blue', edgecolor='black')
    plt.title('Histogram of Object Widths')
    plt.xlabel('Width (nm)')
    plt.ylabel('Count')
    plt.show()

    # Plot histogram of heights
    plt.figure(figsize=(10, 5))
    plt.hist(height, bins=50, color='green', edgecolor='black')
    plt.title('Histogram of Object Heights')
    plt.xlabel('Height (nm)')
    plt.ylabel('Count')
    plt.show()

    # Plot histogram of X_positions
    plt.figure(figsize=(10, 5))
    plt.hist(X_positions, bins=50, color='purple', edgecolor='black')
    plt.title('Histogram of Object X Positions')
    plt.xlabel('X Position (nm)')
    plt.ylabel('Count')
    plt.show()

    # Plot histogram of Y_positions
    plt.figure(figsize=(10, 5))
    plt.hist(Y_positions, bins=50, color='orange', edgecolor='black')
    plt.title('Histogram of Object Y Positions')
    plt.xlabel('Y Position (nm)')
    plt.ylabel('Count')
    plt.show()

    # Create the tkinter window
    window = tk.Tk()
    window.title('Object Information')

    # Add the information to the window
    tk.Label(window, text=f"Number of objects: {len(annotations)}").pack()
    tk.Label(window, text=f"X position range: min = {min(X_positions):.2f} nm, max = {max(X_positions):.2f} nm").pack()
    tk.Label(window, text=f"Y position range: min = {min(Y_positions):.2f} nm, max = {max(Y_positions):.2f} nm").pack()

    # Run the tkinter window
    window.mainloop()
