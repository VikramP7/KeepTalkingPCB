import math
import numpy as np
from PIL import Image
import sys
import random
import copy


def GetPath():
    """Prompts the user to provide a path to an image file"""
    badImagePath = True
    path = ""
    while badImagePath:
        badImagePath = False
        path = input("What is the path for your image (include extension): ")
        try:
            image = Image.open(path)
            image.close()
        except TypeError:
            badImagePath = True
            print("File not parsable.")
        except FileNotFoundError:
            badImagePath = True
            print("No file found at path.")
    return path


def ReturnDitheredImage(path, width=-1, height=-1, allowTranspose=False, returnBWToo=False):
    """
    Uses the provided path to parse an image file. Then it's scaled it to fit width and height.
    Finally the scaled image is converted to bitmap unsigned ints for lcd.

    :param path: (String) The path to the image file
    :param width: (int) width of result image in pixels
    :param height: (int) height of result image in pixels
    :return: A string of a 2D c array for pasting into lcd program
    """

    # print(len(imgArr))
    # print(len(imgArr[0]))

    # open image and convert to 3d array
    image = Image.open(path)
    imgArr = np.asarray(image)
    image.close()

    imageHeight = len(imgArr)
    imageWidth = len(imgArr[0])

    if width == -1:
        width = imageWidth
    if height == -1:
        height = imageHeight

    width = min(width, imageWidth)
    height = min(height, imageHeight)

    imageRatio = imageWidth / imageHeight
    displayRatio = width / height
    transpose = (displayRatio > 1) ^ (
        imageRatio > 1
    )  # XOR as only if they differ then transpose
    if transpose and allowTranspose:
        imgArr = np.transpose(imgArr, (1, 0, 2))
        imageHeight = len(imgArr)
        imageWidth = len(imgArr[0])

    # set result image
    widthFactor = math.floor(imageWidth / width)
    heightFactor = math.floor(imageHeight / height)

    resizeImg = []
    resizeImgAveCount=[]
    for x in range(0, height):
        resizeImg.append([])
        resizeImgAveCount.append([])
        for y in range(0, width):
            resizeImg[x].append(0.0)
            resizeImgAveCount[x].append(0)
    
    # Better Down scaling
    for y in range(imageHeight):
        for x in range(imageWidth):
            smallX = min(round(x*(width/imageWidth)), width-1)
            smallY = min(round(y*(height/imageHeight)), height-1)
            try:
                for rgb in range(3):
                    resizeImg[smallY][smallX] += imgArr[y][x][rgb]
            except IndexError:
                resizeImg[smallY][smallX] += imgArr[y][x]
            resizeImgAveCount[smallY][smallX] += 1
    
    for y in range(height):
        for x in range(width):
            resizeImg[y][x] = resizeImg[y][x]/(resizeImgAveCount[y][x]*3.0 * 255.0)

    if BWToo:
        resizeImgNoDither = copy.deepcopy(resizeImg)

    kernelFloydSteinberg=[[   0,    0, 7/16],
                          [3/16, 5/16, 1/16]]
    
    kernelJarvis=[[0,0,0,7,5],
                  [3,5,7,5,3],
                  [1,3,5,3,1]]
    
    for y in range(len(kernelJarvis)):
        for x in range(len(kernelJarvis[y])):
            kernelJarvis[y][x] /= 48
    
    kernelRandom = []
    for y in range(2):
        kernelRandom.append([])
        for x in range(3):
            kernelRandom[y].append(random.random())
    kernelRandom[0][0]=0
    kernelRandom[0][1]=0

    kernel = kernelJarvis
    zeroOffset=2

    # Dithering Algorithm:
    for y in range(0, height - zeroOffset):
        for x in range(0, width - zeroOffset):
            oldPixel = resizeImg[y][x]
            newPixel = round(resizeImg[y][x])
            quantError = (oldPixel - newPixel)
            for kernelY in range(len(kernel)):
                for kernelX in range(len(kernel[kernelY])):
                    resizeImg[y+kernelY][x+kernelX-zeroOffset] += quantError * kernel[kernelY][kernelX]
            """
            resizeImg[y][x + 1] = resizeImg[y][x + 1] + (quantError * (1 / 16))
            resizeImg[y + 1][x - 1] = resizeImg[y + 1][x - 1] + (quantError * (3 / 16))
            resizeImg[y + 1][x] = resizeImg[y + 1][x] + (quantError * (5 / 16))
            resizeImg[y + 1][x + 1] = resizeImg[y + 1][x + 1] + (quantError * (1 / 16))
            """

    # round to binary
    threshold = 0.5
    for y in range(0, height):
        for x in range(0, width):
            #threshold = (0.2+random.random()*0.8)
            resizeImg[y][x] = 0 if resizeImg[y][x] > threshold else 1
            if returnBWToo:
                resizeImgNoDither[y][x] = 0 if resizeImgNoDither[y][x] > threshold else 1

    if returnBWToo:
        return resizeImg, resizeImgNoDither

    return resizeImg

def saveImage(image, fileName):
    npImage = (np.asarray(image)^1)* 255

    display = Image.fromarray(npImage.astype(np.uint8))
    display.save(fileName)


if __name__ == "__main__":
    n = len(sys.argv)
    path = ""
    width = 324 #128
    height = 244 #64
    BWToo = False
    if n == 2:
        path = sys.argv[1]
        width = -1
        height = -1
    elif n >= 4:
        path = sys.argv[1]
        try:
            width = int(sys.argv[2])
            height = int(sys.argv[3])
        except (TypeError, IndexError):
            print("Error With width-height arguments")
            print("Please use \"ImageGen.py [path] [width] [height] [saveBW]\"")
            print("Or use \"ImageGen.py [path]\" for default parameters")
        if n > 4:
            BWToo = True
    else:
        path = GetPath()
        width = -1
        height = -1

    print("Image Path: ", path)
    print("Display Width: ", ("Original" if width == -1 else width))
    print("Display Height: ", ("Original" if height == -1 else height))

    if BWToo:
        ditheredImage, BWImage = ReturnDitheredImage(path, width, height, returnBWToo=True)
        saveImage(ditheredImage, path[:path.index('.')]+"_display.png")
        saveImage(BWImage, path[:path.index('.')]+"_BWdisplay.png")
    else:
        ditheredImage = ReturnDitheredImage(path, width, height, returnBWToo=False)
        saveImage(ditheredImage, path[:path.index('.')]+"_display.png")

    # print(bitmap)
