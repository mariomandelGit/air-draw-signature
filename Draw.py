import numpy as np
import cv2
from collections import deque

# Define the upper and lower boundaries for a color to be considered "Blue"
Lower = np.array([100, 60, 60])
Upper = np.array([140, 255, 255])

# Define a 5x5 kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)