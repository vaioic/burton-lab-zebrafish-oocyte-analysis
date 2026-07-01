import numpy as np
import pandas as pd
import skimage
from cellpose import io, models
from matplotlib import pyplot as plt
from oic_toolkit import display, segment
from openslide import OpenSlide

from shared import core_func

# model = models.CellposeModel(gpu=True, model_type='cpsam_v2')

# slide = OpenSlide("../data/265317.svs")

# print(f"Total levels: {slide.level_count}")
# print(f"Dimensions: {slide.dimensions}")

# image = np.asarray(slide.read_region((0, 0), 0, (29880, 28817)))

# print(type(image))
# print(image.dtype)

core_func.process_image("../data/265317.svs", "../processed/20260701_dev")

# Make a mask of the purple objects, then use cellpose to split them (or maybe watershed?)


