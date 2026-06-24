import matplotlib.pyplot as plt
import numpy as np


def histogram_plot(image: np.ndarray) -> None:
    """Plot the histogram of the image."""
    plt.figure(figsize=(10, 5))
    plt.title("Histogram of Pixel Intensities")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    if len(image.shape) == 2:  # Grayscale image
        plt.hist(image.ravel(), bins=256, range=(0, 255), color='black')
    else:  # Color image
        colors = ("r", "g", "b")
        for i, color in enumerate(colors):
            plt.hist(image[:, :, i].ravel(), bins=256, range=(0, 255), color=color, alpha=0.5, label=f'{color.upper()} channel')
    plt.xlim([0, 255])
    plt.legend()
    plt.show()