import numpy as np


def translate(image: np.ndarray, rows: int, cols: int) -> np.ndarray:
    """Translate the image by rows pixels down and cols pixels to the right."""
    output = np.zeros((image.shape[0]+rows, image.shape[1]+cols, image.shape[2]), dtype=image.dtype)
    output[rows:, cols:] = image
    return output[:image.shape[0], :image.shape[1]]


def rotate(image: np.ndarray, angle: float, center: tuple = None) -> np.ndarray:
    """Rotate the image by the given angle (in degrees) around the specified center.
    
    Reference: https://stackoverflow.com/questions/695080/how-do-i-rotate-an-image
    """
    if center is None:
        center = (image.shape[1] / 2, image.shape[0] / 2)
    a = np.cos(np.radians(angle))
    b = np.sin(np.radians(angle))
    M = np.array([[a, b], [-b, a]])
    output = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Apply the rotation matrix to the pixel coordinates (j, i) relative to the center
            new_coords = M @ np.array([j - center[0], i - center[1]])
            # Add the center back to the new coordinates
            new_coords += np.array(center)
            # TODO: Add comparison with https://docs.opencv.org/5.0/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#rotation  # noqa: E501
            new_j, new_i = int(new_coords[0]), int(new_coords[1])
            if 0 <= new_i < image.shape[0] and 0 <= new_j < image.shape[1]:
                output[i, j] = image[new_i, new_j]
    return output