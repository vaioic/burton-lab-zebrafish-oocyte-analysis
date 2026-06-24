import numpy as np
import skimage
from matplotlib import pyplot as plt
from openslide import OpenSlide

slide = OpenSlide("../data/265317.svs")

print(f"Total levels: {slide.level_count}")
print(f"Dimensions: {slide.dimensions}")

image = np.asarray(slide.read_region((0, 0), 0, (29880, 28817)))

print(type(image))
print(image.dtype)


image_ds = image[::8, ::8, :]

plt.imshow(image_ds)
plt.show()
