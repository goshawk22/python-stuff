from math import sqrt, ceil
from PIL import Image

f = open('kernel/kernel', 'rb')
kernel = f.read()

def get_dimensions(x):
    output = []
    for i in range(1, x + 1):
        if x % i == 0:
            output.append(i)
    center = output[len(output)//2]
    return (x//center, center)


def to_image(kernel, size):
    return Image.frombytes('L', size, kernel).resize((ceil(sqrt(len(kernel))), ceil(sqrt(len(kernel)))))


image = to_image(kernel, get_dimensions(len(kernel)))
image.save("./kernel.png")