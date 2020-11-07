from PIL import Image
import math
import operator
from functools import reduce


def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return type(result)

if __name__ == '__main__':
    img1 = "./1.png"  # 指定图片路径
    img2 = "./1.png"
    result = image_contrast(img1,img2)
    print(result)