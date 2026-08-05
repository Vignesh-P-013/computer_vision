import cv2
import numpy as np
import matplotlib.pyplot as plt
def analyze_histogram("/Users/vignesh/Desktop/opencv/pic.jpg"):
image = cv2.imread("/Users/vignesh/Desktop/opencv/pic.jpg")
color_channels = ('b', 'g', 'r')
plt.figure(figsize=(10, 5))
for i, color in enumerate(color_channels):
histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
plt.plot(histogram, color=color, label=f"{color.upper()} Channel")
plt.xlim([0, 256]) # Pixel intensity range
plt.title("Color Histogram Analysis")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
analyze_histogram("opencv") # Replace with your image file
