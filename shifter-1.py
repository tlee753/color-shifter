from PIL import Image
import numpy
import skimage.filters
import math
img = Image.open('cool.png').convert('L')
arr = numpy.array(img)
# print(arr)
# print()
# arr = numpy.round(arr)
# # arr = arr.astype(int)

dualtone = numpy.zeros((arr.shape[0], arr.shape[1], 3), dtype=numpy.uint8)

for i in range(int(arr.shape[0])):
    for j in range(arr.shape[1]):
        arr[i, j] = int(arr[i, j]/32)*32

        if arr[i, j] == 0:
            # dualtone[i, j, 0] = 179
            # dualtone[i, j, 1] = 163
            # dualtone[i, j, 2] = 105
            dualtone[i, j, 0] = 54
            dualtone[i, j, 1] = 69
            dualtone[i, j, 2] = 79
        elif arr[i, j] == 32:
            dualtone[i, j, 0] = 195
            dualtone[i, j, 1] = 185
            dualtone[i, j, 2] = 146
            # dualtone[i, j, 0] = 96
            # dualtone[i, j, 1] = 96
            # dualtone[i, j, 2] = 96
        elif arr[i, j] == 64:
            dualtone[i, j, 0] = 201
            dualtone[i, j, 1] = 192
            dualtone[i, j, 2] = 160
        elif arr[i, j] == 96:
            dualtone[i, j, 0] = 206
            dualtone[i, j, 1] = 199
            dualtone[i, j, 2] = 173
        elif arr[i, j] == 128:
            dualtone[i, j, 0] = 212
            dualtone[i, j, 1] = 206
            dualtone[i, j, 2] = 187
        elif arr[i, j] == 160:
            dualtone[i, j, 0] = 217
            dualtone[i, j, 1] = 214
            dualtone[i, j, 2] = 201
        elif arr[i, j] == 192:
            dualtone[i, j, 0] = 223
            dualtone[i, j, 1] = 221
            dualtone[i, j, 2] = 214
        elif arr[i, j] == 224:
            dualtone[i, j, 0] = 228
            dualtone[i, j, 1] = 228
            dualtone[i, j, 2] = 228
        else:
            print('dumb error')

# for i in range(int(arr.shape[0]*1/2), arr.shape[0]):
    # for j in range(arr.shape[1]):
    #     arr[i, j] = int(arr[i, j]/32)*32

    #     if arr[i, j] == 0:
    #         # dualtone[i, j, 0] = 179
    #         # dualtone[i, j, 1] = 163
    #         # dualtone[i, j, 2] = 105
    #         dualtone[i, j, 0] = 54
    #         dualtone[i, j, 1] = 69
    #         dualtone[i, j, 2] = 79
    #     elif arr[i, j] == 32:
    #         # dualtone[i, j, 0] = 195
    #         # dualtone[i, j, 1] = 185
    #         # dualtone[i, j, 2] = 146
    #         dualtone[i, j, 0] = 96
    #         dualtone[i, j, 1] = 96
    #         dualtone[i, j, 2] = 96
    #     elif arr[i, j] == 64:
    #         dualtone[i, j, 0] = 201
    #         dualtone[i, j, 1] = 192
    #         dualtone[i, j, 2] = 160
    #     elif arr[i, j] == 96:
    #         dualtone[i, j, 0] = 206
    #         dualtone[i, j, 1] = 199
    #         dualtone[i, j, 2] = 173
    #     elif arr[i, j] == 128:
    #         dualtone[i, j, 0] = 212
    #         dualtone[i, j, 1] = 206
    #         dualtone[i, j, 2] = 187
    #     elif arr[i, j] == 160:
    #         dualtone[i, j, 0] = 217
    #         dualtone[i, j, 1] = 214
    #         dualtone[i, j, 2] = 201
    #     elif arr[i, j] == 192:
    #         dualtone[i, j, 0] = 223
    #         dualtone[i, j, 1] = 221
    #         dualtone[i, j, 2] = 214
    #     elif arr[i, j] == 224:
    #         dualtone[i, j, 0] = 228
    #         dualtone[i, j, 1] = 228
    #         dualtone[i, j, 2] = 228
    #     else:
    #         print('dumb error')

# dualtone = skimage.filters.gaussian(dualtone, multichannel=False)
dual = Image.fromarray(dualtone, 'RGB')
dual.save("dual.png")

# print(arr)
# img = Image.fromarray(arr, 'L')
# img.save('greyscale.png')
