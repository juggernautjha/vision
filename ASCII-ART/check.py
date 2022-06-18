import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = input("Enter path to the image (jpeg/png) > ")
img = cv2.imread(imgpath)
shape = (64,32)
resized = cv2.resize(img, shape)
# cv2.imshow("Lol",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
    

