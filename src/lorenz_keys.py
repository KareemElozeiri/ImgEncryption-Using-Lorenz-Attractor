from black import main
from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt 
'''
takes: initial conditions x_0, y_0, z_0 
system parameters a,b, r
outputs: x, y, z chaotic sequences
uses: euler numerical method to calculate the sequences
'''


def lorenz_keys_euler(x_0,y_0,z_0,a,b,r,steps_num, dt):
    
    x_keys = np.empty(steps_num+1)
    y_keys = np.empty(steps_num+1)
    z_keys = np.empty(steps_num+1)

    x_keys[0] = x_0
    y_keys[0] = y_0
    z_keys[0] = z_0



    for i in range(steps_num):
        x_keys[i+1] = x_keys[i] + a*(y_keys[i]-x_keys[i]) * dt
        y_keys[i+1] = y_keys[i] + (-x_keys[i]*z_keys[i]+r*x_keys[i]-y_keys[i]) * dt       
        z_keys[i+1] = z_keys[i] + (x_keys[i]*y_keys[i] - b * z_keys[i]) * dt 

    return x_keys, y_keys, z_keys

'''
takes: initial conditions x_0, y_0, z_0 
system parameters a,b, r
outputs: x, y, z chaotic sequences
uses: runge kuta second order numerical method to calculate the sequences
'''
def lorenz_keys_rungeKuta(x_0,y_0,z_0,a,b,r,steps_num, dt):
    x_keys = np.empty(steps_num+1)
    y_keys = np.empty(steps_num+1)
    z_keys = np.empty(steps_num+1)

    for i in range(steps_num):
        s_x_1 = a*(y_keys[i]-x_keys[i])
        s_y_1 = -x_keys[i]*z_keys[i] + r * x_keys[i] - y_keys[i]
        s_z_1 = x_keys[i]*y_keys[i] - b* z_keys[i]

        s_x_2 =  a*((y_keys[i]+dt*s_y_1)-(x_keys[i]+dt*s_x_1))
        s_y_2 = -(x_keys[i]+dt*s_x_1)*(z_keys[i]+dt*s_z_1) + r * (x_keys[i]+dt*s_x_1) - (y_keys[i]+dt*s_y_1)
        s_z_2 = (x_keys[i]+dt*s_x_1)*(y_keys[i]+dt*s_y_1) - b* (z_keys[i]+dt*s_z_1)

        x_keys[i+1] = x_keys[i] + dt * (s_x_1+s_x_2)/2
        y_keys[i+1] = y_keys[i] + dt * (s_y_1+s_y_2)/2
        z_keys[i+1] = z_keys[i] + dt * (s_z_1+s_z_2)/2  

    return x_keys, y_keys, z_keys 



if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x_key, y_key, z_key = lorenz_keys_rungeKuta(1.2,1.3,1.6,10,8/3,28, 100000, 0.001)
    ax.plot(x_key,y_key,z_key)
    plt.show()

