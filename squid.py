import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

"""
Creates a .png with a rainbow on a squid sillhouette.
"""
img = np.array(cv.imread('squid.png'))
#img = np.array(cv.imread('squid.jpg'))
#crops image to right size
img = img[63:,:]
#plt.imshow(img)
#plt.show()

#get flag image and resize
rainbow = np.array(cv.imread('rainbow.jpg'))
#rainbow = cv.rotate(rainbow,cv.ROTATE_90_CLOCKWISE)
rainbow = cv.flip(rainbow, 1)
rainbow = cv.resize(rainbow, (508, 531), interpolation=cv.INTER_AREA)
rainbow = cv.cvtColor(rainbow, cv.COLOR_BGR2RGB)

#plt.imshow(rainbow)
#plt.show()
jpg = np.flip(img, axis=2)


red, green, blue = jpg[:, :, 0], jpg[:, :, 1], jpg[:, :, 2] #changes here

fig, ax = plt.subplots(1,2, figsize = (10, 10))
# r = ax[0].imshow(red, cmap='winter')
# fig.colorbar(r, ax = ax[0], shrink = 0.8)
# g = ax[1].imshow(green, cmap='winter')
# fig.colorbar(g, ax = ax[1], shrink = 0.8)
# b = ax[2].imshow(blue, cmap='winter')
# fig.colorbar(b, ax = ax[2], shrink = 0.8)
#plt.show()

img_thresh_r = np.logical_and(red >= 0, red < 240)
img_thresh_g = np.logical_and(green >= 0, green <= 255)
img_thresh_b = np.logical_and(blue >= 0, blue < 240)
img_thresh_rgb = np.logical_and(img_thresh_r,img_thresh_g,img_thresh_b)

mask_r = cv.inRange(red, 12, 240)
mask_g = cv.inRange(green, 0, 255)
mask_b = cv.inRange(blue, 0, 240)
r_squid = cv.bitwise_and(rainbow, rainbow, mask=mask_r)

ax[0].imshow(mask_r)
# ax[4].imshow(mask_g)
# ax[5].imshow(mask_b)
ax[1].imshow(r_squid)
plt.show()
# uncomment to write to file
# cv.imwrite('test.png', cv.cvtColor(r_squid, cv.COLOR_BGR2RGB))

#convert from BGR to BGRA
bgra = cv.cvtColor(r_squid, cv.COLOR_BGR2RGBA)
#slice alpha channel
alpha = bgra[:,:,3]
#set alpha channel to 0 where BGR=0
alpha[np.all(bgra[:,:,0:3] == (0,0,0), 2)] = 0
#write to file
cv.imwrite('rainbow_squid.png',bgra)
