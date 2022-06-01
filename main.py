import cv2
import numpy as np 
import skimage
import matplotlib.pyplot as plt
from src.lorenz_keys import *
from src.distribution import get_color_distribution
img = cv2.imread("./assets/realMadrid.jpeg")

height = img.shape[0] 
width =  img.shape[1]

x_keys, y_keys, z_keys = lorenz_keys_euler(0.01,0.02,0.03,10,8/3,28, height*width, 0.01)


x_shuffling_keys = [(int(x_keys[i]*pow(10,15))%width) for i in range(len(x_keys))]
x_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
x_shuffling_indexes = [x_shuffling_keys[i] for i in sorted(x_shuffling_indexes)]


y_shuffling_keys = [(int(y_keys[i]*pow(10,15))%height) for i in range(len(y_keys))]
y_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
y_shuffling_indexes = [y_shuffling_keys[i] for i in sorted(y_shuffling_indexes)]

#encryption
encrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 
k = 0

for i in range(height):
    for j in range(width):
        key = int((z_keys[k]*pow(10, 15))%255)
        encrypted_img[i, j] = img[i, j]^key
        k += 1

#shuffling
encrypted_shuffled_img = np.zeros(shape=[height, width,3], dtype=np.uint8)

for i in range(height):
    k = 0
    for j in range(width):
        encrypted_shuffled_img[i][j] = encrypted_img[y_shuffling_indexes[k]][j] 
        k += 1


for i in range(height):
    k = 0
    for j in range(width):
        encrypted_shuffled_img[i][j] = encrypted_img[i][x_shuffling_indexes[k]]
        k += 1

## decryption 
x_keys, y_keys, z_keys = lorenz_keys_euler(0.01,0.02,0.03,10,8/3,28, height*width, 0.01)

x_shuffling_keys = [(int(x_keys[i]*pow(10,15))%width) for i in range(len(x_keys))]
x_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
x_shuffling_indexes = [x_shuffling_keys[i] for i in sorted(x_shuffling_indexes)]


y_shuffling_keys = [(int(y_keys[i]*pow(10,15))%height) for i in range(len(y_keys))]
y_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
y_shuffling_indexes = [y_shuffling_keys[i] for i in sorted(y_shuffling_indexes)]

decrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 
k = 0

for i in range(height):
     k = 0
     for j in range(width):
         decrypted_img[y_shuffling_indexes[k]][j] = encrypted_shuffled_img[i][j]
         k += 1

k = 0
for i in range(height):
     k = 0
     for j in range(width):
         decrypted_img[i][x_shuffling_indexes[k]] = encrypted_shuffled_img[i][j]
         k += 1

k = 0
for i in range(height):
    for j in range(width):
        key = int((z_keys[k]*pow(10, 15))%255)
        decrypted_img[i, j] = decrypted_img[i, j]^key
        k += 1



cv2.imshow("original",img)
cv2.imshow("encrypted",encrypted_shuffled_img)
cv2.imshow("decypted",decrypted_img)

cv2.waitKey(0)


e_text = " - encrypted"
o_text = " - original"
d_text = "- decrypted"

blue_histogram, red_histogram, green_histogram = get_color_distribution(img)


print("entropy of original",skimage.measure.shannon_entropy(img))
print("entropy without shuffling",skimage.measure.shannon_entropy(encrypted_img))

print("entropy with shuffling",skimage.measure.shannon_entropy(encrypted_shuffled_img))


fig, axes =   plt.subplots(3,3)

axes[0,0].set_title("Blue Color Distribution"+o_text)
axes[0,0].hist(blue_histogram,color="darkblue")
 
axes[1,0].set_title("Green Color Distribution"+o_text)
axes[1,0].hist(green_histogram,color="green")

axes[2,0].set_title("Red Color Distribution"+o_text)
axes[2,0].hist(red_histogram,color="red")

blue_histogram, red_histogram, green_histogram = get_color_distribution(encrypted_shuffled_img)

axes[0,1].set_title("Blue Color Distribution"+e_text)
axes[0,1].hist(blue_histogram,color="darkblue")
 
axes[1,1].set_title("Green Color Distribution"+e_text)
axes[1,1].hist(green_histogram,color="green")

axes[2,1].set_title("Red Color Distribution"+e_text)
axes[2,1].hist(red_histogram,color="red")

blue_histogram, red_histogram, green_histogram = get_color_distribution(decrypted_img)

axes[0,2].set_title("Blue Color Distribution"+d_text)
axes[0,2].hist(blue_histogram,color="darkblue")
 
axes[1,2].set_title("Green Color Distribution"+d_text)
axes[1,2].hist(green_histogram,color="green")

axes[2,2].set_title("Red Color Distribution"+d_text)
axes[2,2].hist(red_histogram,color="red")

plt.tight_layout()
plt.show()


cv2.imwrite("./assets/encrypted.png",encrypted_shuffled_img)
cv2.imwrite("./assets/decrypted.png",decrypted_img)
