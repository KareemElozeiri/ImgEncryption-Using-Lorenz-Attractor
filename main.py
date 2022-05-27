import cv2
import numpy as np 
from src.lorenz_keys import *

img = cv2.imread("Lenna.png")

height = img.shape[0] 
width =  img.shape[1]

x_keys, y_keys, z_keys = lorenz_keys_euler(0.01,0.02,0.03,10,8/3,28, height*width, 0.01)

encrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 
k = 0

for i in range(height):
    for j in range(width):
        key = int((z_keys[k]*pow(10, 5))%256)
        encrypted_img[i, j] = img[i, j]^key
        k += 1

decrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 
k = 0

for i in range(height):
    for j in range(width):
        key = int((z_keys[k]*pow(10, 5))%256)
        decrypted_img[i, j] = encrypted_img[i, j]^key
        k += 1


cv2.imshow("original",img)
cv2.imshow("encrypted",encrypted_img)
cv2.imshow("decypted",decrypted_img)

cv2.waitKey(0)
