import cv2
import numpy as np 
import matplotlib.pyplot as plt
from src.lorenz import Lorenz
img = cv2.imread("./assets/realMadrid.jpeg")


l = Lorenz(0.01,0.02,0.03,10,8/3,28)

l.x_0 = 0.02
l.y_0 = 0.01
print(l.x_0, l.y_0)

encrypted = l.encrypt(img)
decrypted = l.decrypt(encrypted)

cv2.imshow("o", img)
cv2.imshow("e",encrypted)
cv2.imshow("d",decrypted)
cv2.waitKey(0)