import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
#%matplotlib inline 
#%config InlineBackend.figure_format='retina'

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints, max_iterations=200, infinity_border=10):
	image = np.zeros((ppoints, qpoints))
	p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]

	c = p + 1j * q
	z = np.zeros_like(c)

	for k in range(max_iterations):
		z = z**2 + c
		mask = (np.abs(z) > infinity_border) & (image == 0)
		image[mask] = k
		z[mask] = np.nan

	return -image.T
	
rc('animation', html = 'html5')

fig = plt.figure(figsize=(7, 7))
max_frames = 200
max_zoom = 300
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
images = []

def init():
	return plt.gca()

def animate(i):
	if i > max_frames // 2:
		plt.imshow(images[max_frames//2 - i], 'flag')
		return
	
	p_center, q_center = -0.793191078177363, 0.16093721735804
	zoom = (i / max_frames * 2) ** 3 * max_zoom + 1
	scalefactor = 1 / zoom
	pmin_ = (pmin - p_center) * scalefactor + p_center
	qmin_ = (qmin - q_center) * scalefactor + q_center
	pmax_ = (pmax - p_center) * scalefactor + p_center
	qmax_ = (qmax - q_center) * scalefactor + q_center
	image = mandelbrot(pmin_, pmax_, 500, qmin_, qmax_, 500)
	plt.imshow(image, 'flag')
	images.append(image)

	return plt.gca()
	
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=max_frames, interval=50)	
ani.save('mandelbrot.html', fps = 15)
