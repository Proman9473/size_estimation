%% Load image
imagefile = 'C:\Users\MahdiKhalili\Desktop\4.tif';
img = imread(imagefile);

% Get image dimensions
image_size = size(img);
image_width = image_size(2); % Width is the second dimension

%% Read XML file
xmlfile = 'C:\Users\MahdiKhalili\Desktop\4.xml';
xDoc = xmlread(xmlfile);

% Get all "object" elements
allObjects = xDoc.getElementsByTagName('object');

%% Image parameters
HFW = 4.14; % micrometer

% Scale factor (nanometer/pixel), 1 micrometer = 1000 nanometers
scale_factor = (HFW * 1000) / image_width;

%% Calculate real-world bounding box sizes and visualize
figure, imshow(img), title('Image with bounding boxes and widths')
hold on

for k = 0:allObjects.getLength-1
    thisObject = allObjects.item(k);
    
    % Get bounding box element
    bbox = thisObject.getElementsByTagName('bndbox');
    bbox = bbox.item(0);
    
    % Get bounding box coordinates (pixels)
    xmin = str2double(bbox.getElementsByTagName('xmin').item(0).getFirstChild.getData);
    ymin = str2double(bbox.getElementsByTagName('ymin').item(0).getFirstChild.getData);
    xmax = str2double(bbox.getElementsByTagName('xmax').item(0).getFirstChild.getData);
    ymax = str2double(bbox.getElementsByTagName('ymax').item(0).getFirstChild.getData);
    
    % Calculate bounding box size (pixels)
    bbox_width = xmax - xmin;
    bbox_height = ymax - ymin;
    
    % Convert bounding box size to real-world units (nanometers)
    bbox_width_real = bbox_width * scale_factor;
    
    % Print real-world size to console
    fprintf('Object %d: width = %.2f nm\n', k+1, bbox_width_real);
    
    % Draw bounding box and annotate with real-world width
    rectangle('Position', [xmin, ymin, bbox_width, bbox_height], 'EdgeColor', 'r')
    text(xmin, ymin-10, sprintf('%.2f nm', bbox_width_real), 'Color', 'yellow', 'FontSize', 12)
end

hold off
