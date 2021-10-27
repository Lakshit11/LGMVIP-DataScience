# LetsGroMore - Nov2021
# Lakshit RamPrakash Gupta - Data Science Intern
# Task 1.4 - Image to Pencil Sketch with python

# Importing Necessary Libraries
import cv2

# Loading the image
image = cv2.imread('bike.jpg')
cv2.imshow("Original Image", image)

# Converting the image into GrayScale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", grey)

# Inverting the Grey Scale Image
inverted_image = cv2.bitwise_not(grey)
cv2.imshow("Inverted", inverted_image)

# Blurring the image
blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX= 0, sigmaY= 0)

# Creating a function to use the divide method of cv2
def pencil_sketch(x, y):
    return cv2.divide(x, 255 - y, scale = 256)

# Converting the image into pencil sketch
pencil_ = pencil_sketch(grey, blurred_image)
cv2.imshow("Pencil Sketch",pencil_)

# Holding the screen to view the Results
cv2.waitKey(0)
cv2.destroyAllWindows()