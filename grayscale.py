#Shiv K.
#Aug 1, 2024
#The second way to do it, using OpenCV

import cv2

# This is to load the input image
image = cv2.imread('/Users/shiv/Downloads/sample.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# This line is to use the function to turn the image into grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)  

# A window will pop up as the orignial image, then as aney key is pressed, the grayscale-image window will pop up, then another key pressed will break and reset the code.
cv2.destroyAllWindows()
