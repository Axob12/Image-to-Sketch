import cv2
#reading image
img = cv2.imread( <image location> )

scale_percent = 80 # percent of original size
width = int(img.shape[1] * scale_percent / 400)
height = int(img.shape[0] * scale_percent / 400)
dim = (width, height)
resize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#converting BGR image to grayscale
gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

#image inversion
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original Image", resize)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
