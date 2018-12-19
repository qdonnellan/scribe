from scipy.sparse import lil_matrix


def generate_pixel_array(shape):
    """
    Generate a pixel array with the given shape.
    """
    return lil_matrix(shape)


def get_pixel(coordinates, shape):
    """
    Given an x and y (both between 0 and 1) return the corresponding
    pixel in an image with the given shape.
    """
    numRows = shape[0] - 1
    numCols = shape[1] - 1

    m = int(round(numRows * coordinates.x))
    n = int(round(numCols * coordinates.y))
    return (m, n)


def paint_pixel(coordinates, pixel_array):
    """
    Given an x and y and an array of pixels, paint the pixel at (x, y).
    A pixel is either painted ("1") or unpainted ("0").
    """
    shape = pixel_array.get_shape()
    m, n = get_pixel(coordinates, shape)
    pixel_array[m, n] = 1
    return pixel_array
