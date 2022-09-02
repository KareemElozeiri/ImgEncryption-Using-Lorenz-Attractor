import numpy as np 
from typing import Tuple
class Lorenz:
    def __init__(self,x_0:float=0, y_0:float=0, z_0:float=0, a:float=0, b:float=0, r:float=0, dt:float=0.01):
        self.__steps_num = 0
        self.__x_0 = x_0 
        self.__y_0 = y_0 
        self.__z_0 = z_0
        self.__a = a 
        self.__b = b 
        self.__r = r 
        self.__dt = dt 
    

    
    def __lorenz_keys_euler(self) -> Tuple[list, list, list]:
        
        x_keys = np.empty(self.__steps_num+1)
        y_keys = np.empty(self.__steps_num+1)
        z_keys = np.empty(self.__steps_num+1)

        x_keys[0] = self.__x_0
        y_keys[0] = self.__y_0
        z_keys[0] = self.__z_0



        for i in range(self.__steps_num):
            x_keys[i+1] = x_keys[i] + self.__a * (y_keys[i]-x_keys[i]) * self.__dt
            y_keys[i+1] = y_keys[i] + (-x_keys[i] * z_keys[i] + self.__r * x_keys[i]-y_keys[i]) * self.__dt       
            z_keys[i+1] = z_keys[i] + (x_keys[i]*y_keys[i] - self.__b * z_keys[i]) * self.__dt 

        return x_keys, y_keys, z_keys
    

    def __lorenz_keys_rungeKuta(self)-> Tuple[list, list, list]:
        x_keys = np.empty(self.__steps_num+1)
        y_keys = np.empty(self.__steps_num+1)
        z_keys = np.empty(self.__steps_num+1)

        for i in range(self.__steps_num):
            s_x_1 = self.__a*(y_keys[i]-x_keys[i])
            s_y_1 = -x_keys[i]*z_keys[i] + self.__r * x_keys[i] - y_keys[i]
            s_z_1 = x_keys[i]*y_keys[i] - self.__b* z_keys[i]

            s_x_2 =  self.__a*((y_keys[i]+self.__dt*s_y_1)-(x_keys[i]+self.__dt*s_x_1))
            s_y_2 = -(x_keys[i]+self.__dt*s_x_1)*(z_keys[i]+self.__dt*s_z_1) + self.__r * (x_keys[i]+self.__dt*s_x_1) - (y_keys[i]+self.__dt*s_y_1)
            s_z_2 = (x_keys[i]+self.__dt*s_x_1)*(y_keys[i]+self.__dt*s_y_1) - self.__b* (z_keys[i]+self.__dt*s_z_1)

            x_keys[i+1] = x_keys[i] + self.__dt * (s_x_1+s_x_2)/2
            y_keys[i+1] = y_keys[i] + self.__dt * (s_y_1+s_y_2)/2
            z_keys[i+1] = z_keys[i] + self.__dt * (s_z_1+s_z_2)/2  

        return x_keys, y_keys, z_keys 
    

    def __shuffle_img(self, img:np.array, x_keys, y_keys)->np.array:
        height = img.shape[0] 
        width =  img.shape[1]
        shuffled_img = np.zeros(shape=[height, width,3], dtype=np.uint8)

        x_shuffling_keys = [(int(x_keys[i]*pow(10,15))%width) for i in range(len(x_keys))]
        x_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
        x_shuffling_indexes = [x_shuffling_keys[i] for i in sorted(x_shuffling_indexes)]


        y_shuffling_keys = [(int(y_keys[i]*pow(10,15))%height) for i in range(len(y_keys))]
        y_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
        y_shuffling_indexes = [y_shuffling_keys[i] for i in sorted(y_shuffling_indexes)]


        for i in range(height):
            k = 0
            for j in range(width):
                shuffled_img[i][j] = img[y_shuffling_indexes[k]][j] 
                k += 1


        for i in range(height):
            k = 0
            for j in range(width):
                shuffled_img[i][j] = img[i][x_shuffling_indexes[k]]
                k += 1
        
        return shuffled_img


    def __reshuffle_img(self, img:np.array, x_keys, y_keys)->np.array:
        height = img.shape[0] 
        width =  img.shape[1]
        reshuffled_img = np.zeros(shape=[height, width,3], dtype=np.uint8)

        x_shuffling_keys = [(int(x_keys[i]*pow(10,15))%width) for i in range(len(x_keys))]
        x_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
        x_shuffling_indexes = [x_shuffling_keys[i] for i in sorted(x_shuffling_indexes)]


        y_shuffling_keys = [(int(y_keys[i]*pow(10,15))%height) for i in range(len(y_keys))]
        y_shuffling_indexes = np.unique(x_shuffling_keys, return_index=True)[1]
        y_shuffling_indexes = [y_shuffling_keys[i] for i in sorted(y_shuffling_indexes)]
        
        k = 0

        for i in range(height):
            k = 0
            for j in range(width):
                reshuffled_img[y_shuffling_indexes[k]][j] = img[i][j]
                k += 1

        k = 0
        for i in range(height):
            k = 0
            for j in range(width):
                reshuffled_img[i][x_shuffling_indexes[k]] = img[i][j]
                k += 1


        return reshuffled_img

    def encrypt(self, img:np.array, shuffle=True)-> np.array:
        height = img.shape[0] 
        width =  img.shape[1]
        self.__steps_num = height*width

        encrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 

        x_keys, y_keys, z_keys = self.__lorenz_keys_euler()

        k = 0
        for i in range(height):
            for j in range(width):
                key = int((z_keys[k]*pow(10, 15))%255)
                encrypted_img[i, j] = img[i, j]^key
                k += 1

        if shuffle:
            return self.__shuffle_img(encrypted_img, x_keys, y_keys)

        return encrypted_img

    def decrypt(self, img:np.array, shuffled=True) -> np.array:
        height = img.shape[0] 
        width =  img.shape[1]
        self.__steps_num = height*width

        decrypted_img = np.zeros(shape=[height,width, 3], dtype=np.uint8) 

        x_keys, y_keys, z_keys = self.__lorenz_keys_euler()


        if shuffled:
            decrypted_img = self.__reshuffle_img(img, x_keys, y_keys)

        k = 0
        for i in range(height):
            for j in range(width):
                key = int((z_keys[k]*pow(10, 15))%255)
                decrypted_img[i, j] = decrypted_img[i, j]^key
                k += 1


        return decrypted_img