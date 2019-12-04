import cv2 as cv
img = cv.imread('./myphoto.png')
print(img.shape)
scale = 8 * 1024 * 1024 / 24
print("current Size:", img.shape[0] * img.shape[1] / scale)
img = img[:img.shape[1] * 4 // 3, :]
cv.imwrite('./transformed_myphoto.jpg', img)
print(img.shape)
print("transformed Size:", img.shape[0] * img.shape[1] / scale)