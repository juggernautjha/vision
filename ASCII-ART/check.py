import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
# imgpath = input("Enter path to the image (jpeg/png) > ")
parser = argparse.ArgumentParser()
parser.add_argument("--source",type=str, required=True)
parser.add_argument("-height", type = int, required=True)
args = parser.parse_args()
imgpath = args.source
h = args.height
img = cv2.imread(imgpath)
aspect_ratio = img.shape[0]/img.shape[1]
import math
zz = math.floor(aspect_ratio*h/2)
shape = (h,zz)
resized = cv2.resize(img, shape)
# cv2.imshow("Lol",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Grayscale", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def gen_ascii(img):
    res = []
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "=", ",", "."]
    for i in img:
        row = [chars[j//25] for j in i]
        res.append(row)
    return res

res = gen_ascii(gray_image)
for i in res:
    print()
    for j in i:
        print(j, end = "")
print()
    

