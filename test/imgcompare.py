#!/usr/bin/python

import cv2 as cv
from matplotlib import pyplot as plt
from numpy import *

PLOT_FRAMES = 341

plt.gcf().set_size_inches(18.5, 10.5)
 
tpl_img = cv.imread("tpl.jpg", 1)

color = ('b', 'g', 'r')

tpl_hist = [None] * 3
j = 0;
for i, col in enumerate(color):
    tpl_hist[i] = cv.calcHist([tpl_img], [i], None, [256], [0, 256])
    plt.subplot(PLOT_FRAMES + i)
    plt.plot(tpl_hist[i], color = col)
    plt.xlim([0, 256])

plt.subplot(PLOT_FRAMES + j * 4 + 3)
# plt.imshow(tpl_img)
plt.imshow(cv.cvtColor(tpl_img, cv.COLOR_BGR2RGB))

src_img = cv.imread("src.jpg", 1)

src_hist = [None] * 3
j = 1
for i, col in enumerate(color):
    src_hist[i] = cv.calcHist([src_img], [i], None, [256], [0, 256])
    plt.subplot(PLOT_FRAMES + j * 4 + i)
    plt.plot(src_hist[i], color = col)
    plt.xlim([0, 256])

plt.subplot(PLOT_FRAMES + j * 4 + 3)
# plt.imshow(src_img)
plt.imshow(cv.cvtColor(src_img, cv.COLOR_BGR2RGB))

axes = plt.subplot(313)
# value for compare hist
compare_score = [None] * 3
# x/y range
plt.axis([0, 5, -0.5, 1.2])
# x point for up picture
socre_x_position = [0.5, 1.8, 3.2, 4.5]
# hidden x lable
plt.xticks(())
for i, col in enumerate(color):
    compare_score[i] = cv.compareHist(src_hist[i], tpl_hist[i], cv.cv.CV_COMP_CORREL)
    plt.plot([0, socre_x_position[i]], [compare_score[i], compare_score[i]], color = col)
    plt.scatter(socre_x_position[i], compare_score[i], marker = 'o', color = col)
    print compare_score[i]

score = min(compare_score)
plt.plot([0, socre_x_position[i + 1]], [score, score], linestyle = 'dashed', color = 'y')
plt.scatter(socre_x_position[i + 1], score, marker = 'x', color = 'y')
print "result score: %f" % score

plt.show()
