import cv2
import numpy as np

# Read the input images and convert them to grayscale
img1 = cv2.imread(r'enter the path for file')
img2 = cv2.imread(r'enter the path for file')

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Calculate the absolute difference between the two images
diff = cv2.absdiff(img1_gray, img2_gray)

# Set a threshold to highlight the differences
_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

# Dilate the threshold image to highlight the different regions
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(thresh, kernel, iterations=1)

# Find contours in the dilated image
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Set a threshold for the minimum contour size (adjust this as needed)
min_contour_size = 500

# Draw the contours on the original images
for contour in contours:
    if cv2.contourArea(contour) > min_contour_size:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Create a composite image by stacking the original images horizontally
composite_image = np.hstack((img1, img2))

# Show the composite image with the highlighted differences
cv2.imshow('Composite Image', composite_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
