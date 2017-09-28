import numpy as np
import cv2
import math

im = np.zeros((1000,1000), np.uint8)

# for i in range(400, 600):
# 	for j in range(400, 600):

# 		im[i][j] = 200

def circle(h, k, radius):

	for i in range(1000):
		for j in range(1000):
			r = math.sqrt(((i-h)**2) + ((j-k)**2))

			if r == radius:
				im[i][j] = 255

circle(500, 500, 300)
cv2.imshow("zeros", im),cv2.waitKey(0)
cv2.destroyAllWindows()