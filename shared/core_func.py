import json
from pathlib import Path

import numpy as np
import pandas as pd
import skimage
from cellpose import io, models
from matplotlib import pyplot as plt
from oic_toolkit import display, segment
from openslide import OpenSlide


def read_image(fpath):

    
    slide = OpenSlide(fpath)

    image = np.asarray(slide.read_region((0, 0), 0, (slide.dimensions)))
                       
    return image

def process_image(file_path, output_path):

    if isinstance(file_path, str):
        file_path = Path(file_path)
    elif isinstance(file_path, Path):
        pass
    else:
        raise TypeError(f"File path must be a str or Path. Instead it is a {type(file_path)}.")
    
    if isinstance(output_path, str):
        output_path = Path(output_path)
    elif isinstance(output_path, Path):
        pass
    else:
        raise TypeError(f"Output path must be a str or Path. Instead it is a {type(output_path)}.")
    
    if not output_path.exists():
        output_path.mkdir(parents=True)

    image = read_image(file_path)

    ROI = display.get_ROI(image, downsample_factor=8)

    with open((output_path / "ROI.json"), "w") as f:
        json.dump(ROI, f, indent=4)
    
    all_data = []

    for index, region in enumerate(ROI):

        cropped = image[region["ymin"]:region["ymax"], region["xmin"]:region["xmax"], :3]

        # target_rgb = (169, 61, 107)
        target_rgb = (231, 86, 99)

        mask = segment.match_color(cropped, target_rgb, radius=40)

        mask = skimage.morphology.opening(mask, skimage.morphology.disk(6))
        mask = skimage.morphology.remove_small_holes(mask, max_size=50)   

        labels = segment.separate_objects(mask)

        data = skimage.measure.regionprops_table(
            labels, 
            properties=(
                "label",
                "centroid",
                "area",
                "eccentricity",)
        )

        df = pd.DataFrame(data)

        df.insert(0, "ROI_ID", index)
        df["ROI_ymin"] = region["ymin"]
        df["ROI_ymax"] = region["ymax"]
        df["ROI_xmin"] = region["xmin"]
        df["ROI_xmax"] = region["xmax"]

        all_data.append(df)

        save_output_image(output_path / f"ROI_{index}.png", 
                          cropped,
                          labels,
                          data)


    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv((output_path / "measured_data.csv"), index=False)

def save_output_image(output_filename, image, labels, props):

    fig, ax = plt.subplots(figsize=(10, 10))

    ov = skimage.segmentation.mark_boundaries(image, labels, mode="thick")
    
    ax.imshow(ov)

    for idx, _ in enumerate(props["centroid-1"]):
        plt.text(
            props["centroid-1"][idx],
            props["centroid-0"][idx],
            str(int(props["label"][idx])),
            color="yellow",
            fontsize=2,
            weight="bold",
            ha="center",
            va="center"
        )
    
    plt.axis("off")
    plt.savefig(output_filename,
                bbox_inches="tight",
                dpi=300)
    
    plt.close(fig)
