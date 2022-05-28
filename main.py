import cv2
import numpy as np 
import matplotlib.pyplot as plt
from src.lorenz_keys import *
from src.distribution import get_color_distribution
img = cv2.imread("Lenna.png")

height = img.shape[0] 
width =  img.shape[1]

x_keys, y_keys, z_keys = lorenz_keys_euler(0.01,0.02,0.03,10,8/3,28, height*width, 0.01)

encrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 
k = 0

for i in range(height):
    for j in range(width):
        key = int((z_keys[k]*pow(10, 15))%256)
        encrypted_img[i, j] = img[i, j]^key
        k += 1


x_keys, y_keys, z_keys = lorenz_keys_euler(0.01,0.02,0.03,10,8/3,28, height*width, 0.01)
decrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 
k = 0

for i in range(height):
    for j in range(width):
        key = int((z_keys[k]*pow(10, 15))%256)
        decrypted_img[i, j] = encrypted_img[i, j]^key
        k += 1



cv2.imshow("original",img)
cv2.imshow("encrypted",encrypted_img)
cv2.imshow("decypted",decrypted_img)

cv2.waitKey(0)


e_text = " - encrypted"
o_text = " - original"

blue_histogram, red_histogram, green_histogram = get_color_distribution(img)


fig, axes =   plt.subplots(3,2)

axes[0,0].set_title("Blue Color Distribution"+o_text)
axes[0,0].hist(blue_histogram,color="darkblue")
 
axes[1,0].set_title("Green Color Distribution"+o_text)
axes[1,0].hist(green_histogram,color="green")

axes[2,0].set_title("Red Color Distribution"+o_text)
axes[2,0].hist(red_histogram,color="red")

blue_histogram, red_histogram, green_histogram = get_color_distribution(encrypted_img)

axes[0,1].set_title("Blue Color Distribution"+e_text)
axes[0,1].hist(blue_histogram,color="darkblue")
 
axes[1,1].set_title("Green Color Distribution"+e_text)
axes[1,1].hist(green_histogram,color="green")

axes[2,1].set_title("Red Color Distribution"+e_text)
axes[2,1].hist(red_histogram,color="red")

plt.tight_layout()
plt.show()
