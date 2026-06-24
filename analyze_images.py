import numpy as np
import skimage
from cellpose import io, models
from matplotlib import pyplot as plt
from oic_toolkit import display, segment
from openslide import OpenSlide

# model = models.CellposeModel(gpu=True, model_type='cpsam_v2')

slide = OpenSlide("../data/265317.svs")

print(f"Total levels: {slide.level_count}")
print(f"Dimensions: {slide.dimensions}")

image = np.asarray(slide.read_region((0, 0), 0, (29880, 28817)))

print(type(image))
print(image.dtype)

ROI = display.get_ROI(image, downsample_factor=8)

for region in ROI:

    cropped = image[region["ymin"]:region["ymax"], region["xmin"]:region["xmax"], :3]

    target_rgb = (169, 61, 107)

    mask = segment.match_color(cropped, target_rgb, radius=30)

    mask = skimage.morphology.opening(mask, skimage.morphology.disk(5))

    mask = skimage.morphology.remove_small_holes(mask, max_size=50)
    

    ov = skimage.segmentation.mark_boundaries(cropped, mask, mode="thick")

    plt.imshow(ov)
    plt.show()

# Make a mask of the purple objects, then use cellpose to split them (or maybe watershed?)


