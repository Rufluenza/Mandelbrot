from matplotlib import axes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\ruben\\Documents\\ffmpeg\\binffmpeg.exe'
fig, ax = plt.subplots()
xmin, xmax, ymin, ymax = -1.4, 1.4, -2, 0.8

def mandelbrot( h,w, maxit=50 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ xmin:xmax:h*1j, ymin:ymax:w*1j ] # we define the coordinates.
    c = x+y*1j # we define the complex number c
    z = c # we define the complex number z
    divtime = maxit + np.zeros(z.shape, dtype=int) # we define the number of iterations

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2 # diverge is a boolean array and marks the elements as True for which the condition is fulfilled and False for the other elements
        div_now = diverge & (divtime==maxit) 
        divtime[div_now] = i # set the time of divergence for those elements to the current time
        z[diverge] = 2 # avoid diverging too much

    return divtime

# zoom in on the interesting part of the fractal
# create the zoom effect by changing the coordinates in a loop

# savepath = os.path.dirname('mandelbrot_images')

# making the image sequence as ims
ims = []
# saving the images as a png file but zooming into the fractal ending with a interesting part of the fractal being x = -0.75, y = 0.1, width = 0.005, height = 0.005 but animated so it looks like a zoom effect

savepath = "C:\\code\\python\\mandelbrot-bulb\\mandelbrot_images\\animation.mp4"

for zoom in range(30):
    # zoom effect
    if (xmin, xmax, ymin, ymax) == 0:
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



    # saving the images in a folder called mandelbrot_images
    # plt.imsave(os.path.dirname('mandelbrot_images/mandelbrot_{zoom}.png'), mandelbrot(400,400), cmap='hot')
"""
calculate the zoom to the point x=180, y=160
xmin = -1.4
xmax = 1.4
ymin = -2
ymax = 0.8
xres = 400
yres = 400

using a for loop we need to stop at x=180, y=160
we need to calculate the zoom factor
zoom factor = (xmax - xmin) / xres = 

"""
# we calculate xmin and xmax
# (-1.4-1.4)/400 = -0.0035 # which is the zoom factor to get to the middle of the image
# we need to zoom in on the point x=180, y=160
# if -0.0035 is the middle which is 200 then we need to zoom in on 180
# we take 90% of 0.0035 which is 0.00315 and add it to the xmin and subtract it from the xmax 
# now we do the same for the y axis
# we take 90% of 0.0025 which is 0.00225 and add it to the ymin and subtract it from the ymax