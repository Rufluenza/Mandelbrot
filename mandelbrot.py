from matplotlib import axes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import subprocess

os.login = os.getlogin()

plt.rcParams['animation.ffmpeg_path'] =(f'C:\\Users\\{os.login}\\Documents\\ffmpeg\\bin\\binffmpeg.exe')
fig = plt.figure()
ax = plt.subplots()
xmin, xmax, ymin, ymax = -1.4, 1.4, -2, 0.8

def mandelbrot( h,w, maxit=100 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ xmin:xmax:h*1j, ymin:ymax:w*1j ] # we define the coordinates.
    c = x+y*1j # we define the complex number c
    z = c # we define the complex number z
    iteration = maxit + np.zeros(z.shape, dtype=int) # we define the number of iterations

# c = x + y*1j

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2 # diverge is a boolean array and marks the elements as True for which the condition is fulfilled and False for the other elements
        div_now = diverge & (iteration==maxit) 
        iteration[div_now] = i # set the time of divergence for those elements to the current time
        z[diverge] = 2 # avoid diverging too much

    return iteration

# zoom in on the interesting part of the fractal
# create the zoom effect by changing the coordinates in a loop

# savepath = os.path.dirname('mandelbrot_images')



# saving the images as a png file but zooming into the fractal ending with a interesting part of the fractal being x = -0.75, y = 0.1, width = 0.005, height = 0.005 but animated so it looks like a zoom effect
# set saavwepath to the path where you want to save the images default is the current directory
# use os.mkdir to create a directory to save the images in C:\\Users\\{os.login}\\Documents\\mandelbrot_video
# first check if the directory exists with os.path.exists

ask_save = input('Do you want to save the images? (y/n): ')
if ask_save == 'y':
    if os.path.exists(f'C:\\Users\\{os.login}\\Documents\\mandelbrot_video'):
        print('Directory exists')
    else:
        os.mkdir(f"C:\\Users\\{os.login}\\Documents\\mandelbrot_video")
        print('Directory created')
    savepath = (f"C:\\Users\\{os.login}\\Documents\\mandelbrot_video\\mandelbrot.mp4")
    

    # making the image sequence as ims
    ims = []
    for zoom in range(30):
        # zoom effect
        if xmin or xmax or ymin or ymax <= 0:
            break
        xmin += zoom * 0.00415
        xmax -= zoom * 0.00585
        ymin += zoom * 0.00325
        ymax -= zoom * 0.00675
        im = ax.imshow(mandelbrot(400,400), animated=True)
        if zoom == 0:
            ax.imshow(mandelbrot(400,400))
        else:
            ims.append([im])
    FFwriter = animation.FFMpegWriter()
    ani = animation.ArtistAnimation(fig, ims, interval=300, blit=True, repeat_delay=1000)
    ani.save(savepath, writer=FFwriter)
    print("Done saved the video to the path: ", savepath)

else:
    plt.imshow(mandelbrot(1000,1000))
    plt.show()

    
