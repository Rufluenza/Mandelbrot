from matplotlib import axes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import os.path as path

from sys import platform

os.login = os.getlogin()
if platform == "win32":
    plt.rcParams['animation.ffmpeg_path'] =(f'C:\\Users\\{os.login}\\Documents\\ffmpeg\\bin\\binffmpeg.exe')
elif platform == "mac":
    plt.rcParams['animation.ffmpeg_path'] ='/Users/{os.login}/Documents/ffmpeg'
elif platform == "linux":
    plt.rcParams['animation.ffmpeg_path'] ='/usr/bin/ffmpeg'

fig = plt.figure()
ax = plt.subplots()
xmin, xmax, ymin, ymax = -1.4, 1.4, -2, 0.8

def mandelbrot( h,w, maxit=100 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ xmin:xmax:h*1j, ymin:ymax:w*1j ] # we define the coordinates.
    c = x+y*1j # we define the complex number c
    z = c # we define the complex number z
    iteration = maxit + np.zeros(z.shape, dtype=int) # we define the number of iterations

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2 # diverge is a boolean array and marks the elements as True for which the condition is fulfilled and False for the other elements
        div_now = diverge & (iteration==maxit) 
        iteration[div_now] = i # set the time of divergence for those elements to the current time
        z[diverge] = 2 # avoid diverging too much

    return iteration

# zoom in on the interesting part of the fractal
# create the zoom effect by changing the coordinates in a loop

# saving the images as a png file but zooming into the fractal ending with a interesting part of the fractal being x = -0.75, y = 0.1, width = 0.005, height = 0.005 but animated so it looks like a zoom effect
# set saavwepath to the path where you want to save the images default is the current directory
# use os.mkdir to create a directory to save the images in C:\\Users\\{os.login}\\Documents\\mandelbrot_video
# first check if the directory exists with os.path.exists

# here we are asking if the user wants to save the images or not
# and we are also making sure that the user gets the directory right regardless of the operating system
ask_save = input('Do you want to save the images? (y/n): ')
ask_save = ask_save.capitalize()

savepath = os.path.abspath("mandelbrot_video.mp4")
# making the image sequence as ims
ims = []
for zoom in range(1, 31):
    # zoom effect
    xmin += 0.0415
    xmax -= 0.0585
    ymin += 0.0325
    ymax -= 0.0675
    im = plt.imshow(mandelbrot(400,400), animated=True)
    ims.append([im])
FFwriter = animation.FFMpegWriter(fps=10)
anim = animation.ArtistAnimation(fig, ims, interval=300, blit=True, repeat_delay=1000)
if ask_save == 'Y':
    plt.show()
    anim.save("mandelbrot.mp4", writer=FFwriter)
    print("Done saved the video to the path: ", savepath)
else:
    plt.show()
