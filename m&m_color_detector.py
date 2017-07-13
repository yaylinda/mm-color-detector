import cv2
import numpy as np
import imutils

'''
|   red     |
----------------
| 99,34,38  | 
| 80,25,30  |
| 116,54,57 |
| 123,57,59 |


----------------------------------
green | 103,170,103 | 90,151,92
      | 108,175,108 | 99,165,101
----------------------------------
blue  | 0-125-255 | 125-0-255
----------------------------------

'''

boundaries = [
    #  B.   G.   R.    B.    G.   R.    
	([25, 20, 80], [70, 70, 130]) # red
]

# image = cv2.imread("pics/test.png")
image_orig = cv2.imread("pics/IMG_1684.JPG")
image_gray = cv2.cvtColor(image_orig, cv2.COLOR_BGR2GRAY)
image_gray = cv2.medianBlur(image_gray,5)
image = cv2.imread("pics/IMG_1684.JPG")

# loop over the boundaries
# for (lower, upper) in boundaries:
for n in range(0, len(boundaries)):

	print "processing " + str(n)



	(lower,upper) = boundaries[n]


	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# print lower
	# print upper
 
	# find the colors within the specified boundaries and apply the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	output_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

	# show the images
	cv2.imwrite('output_' + str(n) + '.bmp', np.hstack([image, output]))


	ret, thresh = cv2.threshold(output_gray, 127, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	cv2.drawContours(output, contours, -1, (0,255,0), 3)
	
	cv2.imwrite('output_cont_' + str(n) + '.bmp', output)


	
	# print 'finding circles...'
	# circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=5,minRadius=0,maxRadius=0)
	# print circles

	# circles = np.uint16(np.around(circles))
	# for i in circles[0,:]:
	#     # draw the outer circle
	#     cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
	#     # draw the center of the circle
	#     cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

	# cv2.imwrite('output_' + str(n) + '.bmp', image_gray, image)


	# print '[' + str(n) + '] - ' + 'num circles detected: ' + str(len(circles[0]))






























