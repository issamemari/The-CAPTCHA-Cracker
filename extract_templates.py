import numpy as np
from matplotlib import pyplot as plt
import scipy.misc
from os import listdir


def read_image(filename):
    f = open(filename)
    content = f.readlines()
    rows, columns = map(int, content[0].split(' '))
    image_data = np.empty([rows, columns, 3])
    for i, line in enumerate(content[1:]):
        image_data[i, :, :] = np.array([list(map(int, pixel.split(','))) for
                                        pixel in line.split(' ')])
    return image_data


def binarize_image(image_data):
    image_data = image_data.mean(axis=2)
    image_data = (image_data > 127).astype(int)
    return image_data


filenames_input = sorted(map(lambda x: 'input/' + x,
                             filter(lambda x: str.endswith(x, '.txt'),
                                    listdir('input'))))

filenames_output = sorted(map(lambda x: 'output/' + x,
                              filter(lambda x: str.endswith(x, '.txt'),
                                     listdir('output'))))

s = {}
for filename_input, filename_output in zip(filenames_input, filenames_output):
    image_data = read_image(filename_input)
    image_data_binarized = binarize_image(image_data)

    f_output = open(filename_output)
    truth = f_output.readlines()[0][:-1]
    split_indices = [-1] + \
        list(np.where(image_data_binarized.sum(axis=0) == 30)[0])

    j = 0
    for start_index, end_index in zip(split_indices[::1][:-1], split_indices[1::1]):
        if start_index + 1 != end_index:
            letter_image_data = image_data_binarized[11:-9,
                                                     start_index + 1:end_index]
            s[truth[j]] = letter_image_data
            j += 1

print(s)