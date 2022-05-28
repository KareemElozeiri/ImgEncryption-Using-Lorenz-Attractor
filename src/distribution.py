'''
shows the distribution of colors for the given image 
'''
import cv2 
def get_color_distribution(img):
    blue_histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
    red_histogram = cv2.calcHist([img], [1], None, [256], [0, 256])
    green_histogram = cv2.calcHist([img], [2], None, [256], [0, 256]) 

    return blue_histogram, red_histogram, green_histogram
